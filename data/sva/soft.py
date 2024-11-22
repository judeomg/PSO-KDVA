import json

# 读取soft文件和preds文件
with open('soft_unlabel_train.jsonl', 'r') as soft_file, open('preds_unlabel_train.jsonl', 'r') as preds_file:
    soft_data = [json.loads(line) for line in soft_file]
    preds_data = [json.loads(line) for line in preds_file]

# 检查长度是否一致
if len(soft_data) != len(preds_data):
    print("两个文件的长度不一致，无法进行替换")
else:
    # 逐行替换soft_label列
    new_data = []
    for soft_entry, preds_entry in zip(soft_data, preds_data):
        new_entry = soft_entry.copy()  # 不修改原数据，复制一份
        new_entry['soft_label'] = preds_entry
        new_data.append(new_entry)

    # 将修改后的数据保存到新文件
    with open('soft_unlabel_train_replaced.jsonl', 'w') as output_file:
        for entry in new_data:
            output_file.write(json.dumps(entry) + '\n')

print("替换完成，文件已保存为 soft_unlabel_train_replaced.jsonl")
