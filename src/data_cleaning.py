import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    df = df.dropna()

    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])

    return df
