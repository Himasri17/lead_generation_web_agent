import os
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def save_ranked_data(df, output_path):
    # Ensure output directory exists (important for Streamlit Cloud)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
