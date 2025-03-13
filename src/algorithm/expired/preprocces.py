import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def save_plot(fig, file_path):
    fig.savefig(file_path)

def plot_missing_values(data, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis', ax=ax)
    ax.set_title('Missing Values Heatmap')
    save_plot(fig, file_path)

def plot_noisy_data(data, column, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=data[column], ax=ax)
    ax.set_title(f'Box Plot of {column} for Noisy Data Detection')
    save_plot(fig, file_path)

def plot_outliers(data, column, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=data[column], ax=ax)
    ax.set_title(f'Box Plot of {column} for Outlier Detection')
    save_plot(fig, file_path)

if __name__ == "__main__":
    file_path = '../../data/updated_sql_dataset.csv'
    df = load_data(file_path)

    plot_missing_values(df, '../../data/4_preprocces/missing_values_heatmap.png')

    noisy_columns = ['Label', 'SELECT', 'UNION', 'OR', 'AND']
    for column in noisy_columns:
        plot_noisy_data(df, column, f'../../data/4_preprocces/noisy_data_{column}.png')

    outlier_columns = ['Label', 'SELECT', 'UNION', 'OR', 'AND']
    for column in outlier_columns:
        plot_outliers(df, column, f'../../data/4_preprocces/outliers_{column}.png')