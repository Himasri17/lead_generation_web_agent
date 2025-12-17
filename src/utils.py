import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def save_ranked_data(df, output_path):
    df.to_csv(output_path, index=False)
