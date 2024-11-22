import copy
import random
import logging
import hashlib
import warnings
import argparse
import time

from tqdm import tqdm
from flops import TransformerHparams

warnings.filterwarnings("ignore")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class Particle(object):
    def __init__(self, gene_param=None):
        self.fitness = 0.0
        self.gene_param = gene_param
        self.velocity = {}  # Velocity for each parameter
        self.pbest = None  # Best position of this particle

        if not self.gene_param:
            self.hash = 0
        else:
            self.update_hash()
            self.pbest = copy.deepcopy(self.gene_param)
            for param in gene_param:
                self.velocity[param] = 0  # Initialize velocity to zero

    def update_hash(self):
        gene_string = str(self.gene_param["intermediate_size"]) + \
                      str(self.gene_param["vocab_size"]) + \
                      str(self.gene_param["attention_heads"]) + \
                      str(self.gene_param["hidden_dim"]) + \
                      str(self.gene_param["n_layers"])
        self.hash = hashlib.md5(gene_string.encode("UTF-8")).hexdigest()

    def update_velocity(self, gbest, w=0.5, c1=1.5, c2=1.5):
        # Update velocity based on inertia, cognitive component, and social component
        for param in self.gene_param:
            r1, r2 = random.random(), random.random()
            cognitive = c1 * r1 * (self.pbest[param] - self.gene_param[param])
            social = c2 * r2 * (gbest[param] - self.gene_param[param])
            self.velocity[param] = w * self.velocity[param] + cognitive + social

    def update_position(self, search_space):
        # Update the particle's position based on its velocity
        for param in self.gene_param:
            new_value = self.gene_param[param] + int(self.velocity[param])
            # Clip the new position to be within the search space bounds
            possible_choices = search_space[param]
            if new_value < min(possible_choices):
                new_value = min(possible_choices)
            elif new_value > max(possible_choices):
                new_value = max(possible_choices)
            else:
                new_value = min(possible_choices, key=lambda x: abs(x - new_value))
            self.gene_param[param] = new_value
        self.update_hash()


class PSO_search():
    def __init__(self, args, search_space):
        self.args = args
        self.search_space = search_space
        self.desired_length = args.population_size
        self.population = []
        self.best_particle = None  # Global best particle

    def initialization(self):
        for _ in range(self.args.population_size):
            gene_param = {key: random.choice(self.search_space[key]) for key in self.search_space}
            particle = Particle(gene_param)
            self.population.append(particle)
            if not self.best_particle or particle.fitness > self.best_particle.fitness:
                self.best_particle = copy.deepcopy(particle)

    def fitness(self, particle):
        vocab_size = particle.gene_param["vocab_size"]
        attention_heads = particle.gene_param["attention_heads"]
        hidden_dim = particle.gene_param["hidden_dim"]
        intermediate_size = particle.gene_param["intermediate_size"]
        n_layers = particle.gene_param["n_layers"]
        model = TransformerHparams(hidden_dim, n_layers, 514, vocab_size, intermediate_size, attention_heads)
        flops = model.get_infer_flops()
        params = model.get_params()


        size_diff = abs(self.args.target_size - params) * 4 / 1e6
        # print(self.args.target_size)
        # print(params)
        # print(size_diff)
        particle.fitness = flops / 1e9 - size_diff

        # Update personal best position (pBest)
        if not particle.pbest or particle.fitness > self.fitness_value(particle.pbest):
            particle.pbest = copy.deepcopy(particle.gene_param)

        # Update global best position (gBest)
        if not self.best_particle or particle.fitness > self.best_particle.fitness:
            self.best_particle = copy.deepcopy(particle)

    def fitness_value(self, gene_param):
        # Evaluate fitness for a given gene_param
        vocab_size = gene_param["vocab_size"]
        attention_heads = gene_param["attention_heads"]
        hidden_dim = gene_param["hidden_dim"]
        intermediate_size = gene_param["intermediate_size"]
        n_layers = gene_param["n_layers"]
        model = TransformerHparams(hidden_dim, n_layers, 514, vocab_size, intermediate_size, attention_heads)
        flops = model.get_infer_flops()
        params = model.get_params()
        size_diff = abs(self.args.target_size - params) * 4 / 1e6
        return flops / 1e9 - size_diff

    def generation(self):
        for particle in self.population:
            # Update velocity and position for each particle
            particle.update_velocity(self.best_particle.gene_param)
            particle.update_position(self.search_space)
            self.fitness(particle)


def main():
    start_time = time.time()

    parser = argparse.ArgumentParser()

    parser.add_argument("--population_size", default=50, type=int)
    parser.add_argument("--generation_size", default=100, type=int)
    parser.add_argument("-t", "--target_size", default=3, type=float)

    args = parser.parse_args()
    search_space = {
        "vocab_size": [*range(1000, 51000, 1000)],
        "attention_heads": [1, 2, 4, 8],
        "hidden_dim": [*range(16, 769, 16)],
        "intermediate_size": [*range(32, 3072, 32)],
        "n_layers": [*range(1, 13)]
    }

    args.target_size = args.target_size * 1e6 / 4
    logger.info("***Start PSO search for %d generations, %d population, target model size %d MB***" %
                (args.generation_size, args.population_size, args.target_size * 4 / 1e6))

    searcher = PSO_search(args, search_space)
    searcher.initialization()
    for gen in tqdm(range(args.generation_size), desc="Searching"):
        searcher.generation()

    logger.info("the best one:")
    logger.info(searcher.best_particle.gene_param)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"代码运行时间: {elapsed_time:.5f} 秒")

if __name__ == "__main__":
    main()
