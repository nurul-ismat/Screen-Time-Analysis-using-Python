import pandas as pd
import plotly.express as px
import os

def load_and_clean_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(file_path)
    df = df.dropna()
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def plot_app_usage(df):
    fig = px.bar(df, x='App', y='ScreenTime(minutes)', color='App',  # Updated column names
                 title="App Usage by Category", template='plotly_dark')
    fig.show()

def plot_notifications(df):
    if 'notifications' in df.columns and 'opens' in df.columns:
        fig = px.scatter(df, x='notifications', y='opens', color='App',
                         size='ScreenTime(minutes)', title="Notifications vs App Opens")
        fig.show()
    else:
        print("Columns 'notifications' and 'opens' not found in the data.")

try:
    df = load_and_clean_data('..\\data\\smartphone_usage.csv')
    print("Data loaded successfully. Columns:", df.columns.tolist())
    # Visualize
    plot_app_usage(df)
    plot_notifications(df)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")