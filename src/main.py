from data_cleaning import load_and_clean_data
from visualization import plot_app_usage, plot_notifications

df = load_and_clean_data('data/smartphone_usage.csv')

plot_app_usage(df)
plot_notifications(df)
