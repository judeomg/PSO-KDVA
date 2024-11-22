# PSO-KDVA: A Lightweight Software Vulnerability Assessment Model Using Particle Swarm Optimization and Knowledge Distillation

This repository contains the implementation of **PSO-KDVA**, which includes fine-tuning a teacher model, compressing a student model, and performing architecture space search using Particle Swarm Optimization (PSO) for software vulnerability assessment (SVA). It also provides datasets and tools to facilitate research in SVA.

---

## File Structure and Descriptions

### Main Components

#### `CodeBERT/sva/compress/`
This folder contains scripts for compressing the teacher model into a lightweight student model using techniques such as knowledge distillation:
- **`BPE_1000.json`** and **`BPE_6000.json`**: Byte Pair Encoding (BPE) vocabulary files used for tokenization.
- **`distill.py`**: Implements the knowledge distillation process for model compression.
- **`lstm_baseline.py`**: A baseline model using LSTM for comparison.
- **`models.py`**: Contains model definitions for the student model.
- **`run.py`**: Main script for training and evaluating the compressed student model.
- **`utils.py`**: Utility functions used throughout the compression process.

#### `CodeBERT/sva/finetune/`
This folder includes scripts for fine-tuning the teacher model for software vulnerability assessment tasks:
- **`main.py`**: Main script for fine-tuning the teacher model.
- **`model.py`**: Contains model definitions for the teacher model.
- **`run2.py`**: Alternative script for running experiments with different configurations.
- **`utils.py`**: Utility functions for model fine-tuning.
- **`LICENSE`**: Licensing information for the project.
- **`README.md`**: A detailed explanation of the fine-tuning module.

#### `data/`
This folder contains the dataset used for software vulnerability assessment:
- **Dataset Details**: Includes vulnerability data formatted for training, validation, and testing purposes.
- The dataset supports tasks such as vulnerability classification, severity prediction, and more.

#### Root Directory
- **`pso.py`**: This script performs **architecture space search** using the Particle Swarm Optimization algorithm. **It must be run first** to determine the optimal architecture before proceeding with fine-tuning or compression.
- **`ga.py`**: Implements Genetic Algorithm for optimization.
- **`flops.py`**: Calculates the Floating Point Operations Per Second (FLOPS) for evaluating model efficiency.

---

## Installation and Requirements

1. **Clone the repository:**
   ```bash
   git clone https://github.com/judeomg/PSO-KDVA.git
   cd PSO-KDVA
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the dataset:**
   Place the dataset files in the `data/` directory following the expected format.

---

## Usage

### Step 1: Architecture Space Search
1. Run the `pso.py` script to perform architecture space search:
   ```bash
   python pso.py
   ```
   This script uses the Particle Swarm Optimization algorithm to search for the optimal model architecture based on performance and efficiency.

### Step 2: Fine-Tuning the Teacher Model
1. Navigate to the `finetune/` directory:
   ```bash
   cd CodeBERT/sva/finetune
   ```

2. Run the fine-tuning script:
   ```bash
   python main.py
   ```

### Step 3: Compressing the Student Model
1. Navigate to the `compress/` directory:
   ```bash
   cd CodeBERT/sva/compress
   ```

2. Run the distillation script:
   ```bash
   python distill.py
   ```

---

## Project Goals

1. **Architecture Space Search**: Use PSO to find optimal model architectures for SVA.
2. **Fine-Tuning a Teacher Model**: Train a robust teacher model for SVA tasks.
3. **Compressing a Student Model**: Reduce model size while maintaining high performance using knowledge distillation.
4. **SVA Dataset**: Provide a high-quality dataset for evaluating vulnerability assessment models.

---

Feel free to contribute or raise issues for further improvements!

---
