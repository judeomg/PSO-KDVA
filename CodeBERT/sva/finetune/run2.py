# import subprocess
#
# # 定义命令，将命令行参数转化为 Python 列表
# command = [
#     'python', 'main.py',
#     '--do_train',
#     '--train_data_file=../../../data/sva/label_train.jsonl',
#     '--eval_data_file=../../../data/sva/valid.jsonl',
#     '--epoch', '30',
#     '--block_size', '400',
#     '--train_batch_size', '16',
#     '--eval_batch_size', '64',
#     '--learning_rate', '2e-5',
#     '--max_grad_norm', '1.0',
#     '--evaluate_during_training',
#     '--seed', '123456'
# ]
#
# # 打开日志文件，使用追加模式 'a'
# with open('../logs/train.log', 'a', encoding='utf-8') as log_file:
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






import subprocess

# 定义命令，将命令行参数转化为 Python 列表
command = [
    'python', 'main.py',
    '--do_eval',
    '--train_data_file=../../../data/sva/label_train.jsonl',
    '--eval_data_file=../../../data/sva/test.jsonl',
    '--block_size', '400',
    '--eval_batch_size', '64',
    '--seed', '123456'
]



# 打开日志文件，使用追加模式 'a'
with open('../logs/eval.log', 'a', encoding='utf-8') as log_file:
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
