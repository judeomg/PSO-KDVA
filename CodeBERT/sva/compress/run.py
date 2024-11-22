# import subprocess
# #
# #sva 50MB模型 评估
# command = [
#     'python', 'distill.py',
#     '--do_eval',
#     '--train_data_file=../../../data\\sva\\soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data\\sva\\test.jsonl',
#     '--model_dir=../checkpoint',
#     '--size', '50',
#     '--attention_heads', '16',
#     '--hidden_dim', '480',
#     '--intermediate_size', '576',
#     '--n_layers', '6',
#     '--vocab_size', '6000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '20',
#     '--seed', '123456'
# ]
#
# with open('../logs\\eval_50.log', 'a', encoding='utf-8') as log_file:
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#     for line in process.stdout:
#         print(line, end="")
#         log_file.write(line)
#     process.wait()


import subprocess

# sva 50MB模型 训练
# command = [
#     'python', 'distill.py',
#     '--do_train',
#     '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data/sva/valid.jsonl',
#     '--model_dir=../checkpoint',
#     '--size', '50',
#     '--attention_heads', '16',
#     '--hidden_dim', '480',
#     '--intermediate_size', '576',
#     '--n_layers', '6',
#     '--vocab_size', '6000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '40',
#     '--seed', '123456'
# ]
#
# with open('../logs/train_50.log', 'a', encoding='utf-8') as log_file:
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#     for line in process.stdout:
#         print(line, end="")
#         log_file.write(line)
#     process.wait()






# 3mb train
import subprocess
# 定义命令，将命令行参数转化为 Python 列表
command = [
    'python', 'distill.py',
    '--do_train',
    '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
    '--eval_data_file=../../../data/sva/valid.jsonl',
    '--model_dir', '../checkpoint',
    '--size', '3',
    '--attention_heads', '8',
    '--hidden_dim', '96',
    '--intermediate_size', '64',
    '--n_layers', '12',
    '--vocab_size', '1000',
    '--block_size', '400',
    '--train_batch_size', '16',
    '--eval_batch_size', '64',
    '--learning_rate', '1e-4',
    '--epochs', '100',
    '--seed', '123456'
]

# 打开日志文件，使用追加模式 'a'
with open('../logs/train_3.log', 'a', encoding='utf-8') as log_file:
    # 执行命令并捕获输出
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')

    # 实时读取输出
    for line in process.stdout:
        # 输出到控制台
        print(line, end="")
        # 写入日志文件（追加模式）
        log_file.write(line)

    # 等待进程结束
    process.wait()






# 3mb eval
# import os
# import subprocess
#
# # 创建日志目录（如果不存在）
# log_dir = "../logs"
# os.makedirs(log_dir, exist_ok=True)
#
# # 定义命令，将命令行参数转换为 Python 列表
# command = [
#     'python', 'distill.py',
#     '--do_eval',
#     '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data/sva/test.jsonl',
#     '--model_dir', '../checkpoint',
#     '--size', '3',
#     '--attention_heads', '8',
#     '--hidden_dim', '96',
#     '--intermediate_size', '64',
#     '--n_layers', '12',
#     '--vocab_size', '1000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '20',
#     '--seed', '123456'
# ]
#
# # 日志文件路径
# log_file_path = os.path.join(log_dir, 'eval_3.log')
#
# # 打开日志文件，使用追加模式 'a'
# with open(log_file_path, 'a', encoding='utf-8') as log_file:
#     # 执行命令并捕获输出
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#
#     # 实时读取输出
#     for line in process.stdout:
#         # 输出到控制台
#         print(line, end="")
#         # 写入日志文件（追加模式）
#         log_file.write(line)
#
#     # 等待进程结束
#     process.wait()






#25mb  train
# import os
# import subprocess

# # 创建日志目录（如果不存在）
# log_dir = "../logs"
# os.makedirs(log_dir, exist_ok=True)
#
# # 定义命令，将命令行参数转换为 Python 列表
# command = [
#     'python', 'distill.py',
#     '--do_train',
#     '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data/sva/valid.jsonl',
#     '--model_dir', '../checkpoint',
#     '--size', '25',
#     '--attention_heads', '16',
#     '--hidden_dim', '432',
#     '--intermediate_size', '128',
#     '--n_layers', '6',
#     '--vocab_size', '1000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '50',
#     '--seed', '123456'
# ]
#
# # 日志文件路径
# log_file_path = os.path.join(log_dir, 'train_25.log')
#
# # 打开日志文件，使用追加模式 'a'
# with open(log_file_path, 'a', encoding='utf-8') as log_file:
#     # 执行命令并捕获输出
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#
#     # 实时读取输出
#     for line in process.stdout:
#         # 输出到控制台
#         print(line, end="")
#         # 写入日志文件（追加模式）
#         log_file.write(line)
#
#     # 等待进程结束
#     process.wait()







# import os
# import subprocess
#
# # 创建日志目录（如果不存在）
# log_dir = "../logs"
# os.makedirs(log_dir, exist_ok=True)
#
# # 定义命令，将命令行参数转换为 Python 列表
# command = [
#     'python', 'distill.py',
#     '--do_eval',
#     '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data/sva/test.jsonl',
#     '--model_dir', '../checkpoint',
#     '--size', '25',
#     '--attention_heads', '16',
#     '--hidden_dim', '432',
#     '--intermediate_size', '128',
#     '--n_layers', '6',
#     '--vocab_size', '1000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '20',
#     '--seed', '123456'
# ]
#
# # 日志文件路径
# log_file_path = os.path.join(log_dir, 'eval_25.log')
#
# # 打开日志文件，使用追加模式 'a'
# with open(log_file_path, 'a', encoding='utf-8') as log_file:
#     # 执行命令并捕获输出
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#
#     # 实时读取输出
#     for line in process.stdout:
#         # 输出到控制台
#         print(line, end="")
#         # 写入日志文件（追加模式）
#         log_file.write(line)
#
#     # 等待进程结束
#     process.wait()






#  baseline  train
# import os
# import subprocess
#
# # 创建日志目录（如果不存在）
# log_dir = "../logs"
# os.makedirs(log_dir, exist_ok=True)
#
# # 定义命令，将命令行参数转换为 Python 列表
# command = [
#     'python', 'lstm_baseline.py',
#     '--do_train',
#     '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data/sva/valid.jsonl',
#     '--model_dir', '../checkpoint',
#     '--hidden_dim', '300',
#     '--n_layers', '1',
#     '--vocab_size', '1000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '30',
#     '--seed', '123456'
# ]
#
# # 日志文件路径
# log_file_path = os.path.join(log_dir, 'train_baseline.log')
#
# # 打开日志文件，使用追加模式 'a'
# with open(log_file_path, 'a', encoding='utf-8') as log_file:
#     # 执行命令并捕获输出
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#
#     # 实时读取输出
#     for line in process.stdout:
#         # 输出到控制台
#         print(line, end="")
#         # 写入日志文件（追加模式）
#         log_file.write(line)
#
#     # 等待进程结束
#     process.wait()






#baseline  eval
import os
import subprocess

# 创建日志目录（如果不存在）
# log_dir = "../logs"
# os.makedirs(log_dir, exist_ok=True)
#
# # 定义命令，将命令行参数转换为 Python 列表
# command = [
#     'python', 'lstm_baseline.py',
#     '--do_eval',
#     '--train_data_file=../../../data/sva/soft_unlabel_train.jsonl',
#     '--eval_data_file=../../../data/sva/test.jsonl',
#     '--model_dir', '../checkpoint',
#     '--hidden_dim', '300',
#     '--n_layers', '1',
#     '--vocab_size', '1000',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '1e-4',
#     '--epochs', '20',
#     '--seed', '123456'
# ]
#
# # 日志文件路径
# log_file_path = os.path.join(log_dir, 'eval_baseline.log')
#
# # 打开日志文件，使用追加模式 'a'
# with open(log_file_path, 'a', encoding='utf-8') as log_file:
#     # 执行命令并捕获输出
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
#
#     # 实时读取输出
#     for line in process.stdout:
#         # 输出到控制台
#         print(line, end="")
#         # 写入日志文件（追加模式）
#         log_file.write(line)
#
#     # 等待进程结束
#     process.wait()



