import numpy as np
import json

# 读取上传的 .npy 文件
npy_file_path = 'preds_unlabel_train_2.npy'  # 请替换为你的文件路径
data = np.load(npy_file_path, allow_pickle=True)

# 将数据转换为列表，确保可以以 JSONL 格式写入
records = data.tolist()

# 输出为 JSONL 格式
jsonl_file_path = 'preds_unlabel_train_2.jsonl'  # 输出文件路径
with open(jsonl_file_path, 'w') as jsonl_file:
    for record in records:
        jsonl_file.write(json.dumps(record) + '\n')

print(f"文件已成功转换为 {jsonl_file_path}")
