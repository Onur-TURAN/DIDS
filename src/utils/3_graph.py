import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def save_plot(fig, file_path):
    fig.savefig(file_path)

def scatter_plot(data, x_label, y_label, title, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(range(len(data)), data, color='skyblue')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    save_plot(fig, file_path)

def box_plot(data, y_label, title, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(data)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    save_plot(fig, file_path)

def bar_plot(data, x_label, y_label, title, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(range(len(data)), data, color='skyblue')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    save_plot(fig, file_path)

def pie_plot(data, title, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(data.value_counts(), labels=data.value_counts().index, autopct='%1.1f%%')
    ax.set_title(title)
    save_plot(fig, file_path)

def histogram_plot(data, x_label, y_label, title, file_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=20, color='skyblue')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    save_plot(fig, file_path)

if __name__ == "__main__":
    file_path = '..\..\data\Modified_SQL_Dataset.csv'
    df = load_data(file_path)

    target_column = df['Label']
    x1_column = df['Query']
#----------------------------------------patates-----------------------------------
    scatter_plot(target_column, 'Index', 'Label', 'Scatter Plot of Label Column', '../../data/graph/scatter_label_column.png')
    box_plot(target_column, 'Label', 'Box Plot of Label Column', '../../data/graph/boxplot_label_column.png')
    bar_plot(target_column, 'Index', 'Label', 'Bar Graph of Label Column', '../../data/graph/bargraph_label_column.png')
    pie_plot(target_column, 'Pie Plot of Label Column', '../../data/graph/pieplot_label_column.png')
    histogram_plot(target_column, 'Label', 'Frequency', 'Histogram of Label Column', '../../data/graph/histogram_label_column.png')
#----------------------------------------sogan-------------------------------------
    scatter_plot(x1_column, 'Index', 'Query', 'Scatter Plot of Query Column', '../../data/graph/scatter_query_column.png')
    box_plot(x1_column, 'Query', 'Box Plot of Query Column', '../../data/graph/boxplot_query_column.png')
    bar_plot(x1_column, 'Index', 'Query', 'Bar Graph of Query Column', '../../data/graph/bargraph_query_column.png')
    pie_plot(x1_column, 'Pie Plot of Query Column', '../../data/graph/pieplot_query_column.png')
    histogram_plot(x1_column, 'Query', 'Frequency', 'Histogram of Query Column', '../../data/graph/histogram_query_column.png')