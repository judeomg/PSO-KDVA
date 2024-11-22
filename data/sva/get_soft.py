import pandas as pd

# Load the files
preds_file_path = 'preds_unlabel_train.jsonl'
unlabel_file_path = 'unlabel_train.jsonl'

# Reading both files
preds_df = pd.read_json(preds_file_path, lines=True)
unlabel_df = pd.read_json(unlabel_file_path, lines=True)

# Add the "soft_label" vector (entire row) from preds_df to unlabel_df
unlabel_df["soft_label"] = preds_df.values.tolist()

# Save the updated dataframe to a new file
output_file_path = 'soft_unlabel_train.jsonl'
unlabel_df.to_json(output_file_path, orient='records', lines=True)

print(f"Updated file saved at: {output_file_path}")
