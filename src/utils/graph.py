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
    file_path = '../../data/updated_sql_dataset.csv'
    df = load_data(file_path)

    target_column = df['Label']
    query_column = df['Query']
    select_column = df['SELECT']
    union_column = df['UNION']
    or_column = df['OR']
    and_column = df['AND']

    scatter_plot(target_column, 'Index', 'Label', 'Scatter Plot of Label Column', '../../data/data_vsl/scatter_label_column.png')
    box_plot(target_column, 'Label', 'Box Plot of Label Column', '../../data/data_vsl/boxplot_label_column.png')
    bar_plot(target_column, 'Index', 'Label', 'Bar data_vsl of Label Column', '../../data/data_vsl/bardata_vsl_label_column.png')
    pie_plot(target_column, 'Pie Plot of Label Column', '../../data/data_vsl/pieplot_label_column.png')
    histogram_plot(target_column, 'Label', 'Frequency', 'Histogram of Label Column', '../../data/data_vsl/histogram_label_column.png')

    scatter_plot(select_column, 'Index', 'SELECT', 'Scatter Plot of SELECT Column', '../../data/data_vsl/scatter_select_column.png')
    box_plot(select_column, 'SELECT', 'Box Plot of SELECT Column', '../../data/data_vsl/boxplot_select_column.png')
    bar_plot(select_column, 'Index', 'SELECT', 'Bar data_vsl of SELECT Column', '../../data/data_vsl/bardata_vsl_select_column.png')
    pie_plot(select_column, 'Pie Plot of SELECT Column', '../../data/data_vsl/pieplot_select_column.png')
    histogram_plot(select_column, 'SELECT', 'Frequency', 'Histogram of SELECT Column', '../../data/data_vsl/histogram_select_column.png')

    scatter_plot(union_column, 'Index', 'UNION', 'Scatter Plot of UNION Column', '../../data/data_vsl/scatter_union_column.png')
    box_plot(union_column, 'UNION', 'Box Plot of UNION Column', '../../data/data_vsl/boxplot_union_column.png')
    bar_plot(union_column, 'Index', 'UNION', 'Bar data_vsl of UNION Column', '../../data/data_vsl/bardata_vsl_union_column.png')
    pie_plot(union_column, 'Pie Plot of UNION Column', '../../data/data_vsl/pieplot_union_column.png')
    histogram_plot(union_column, 'UNION', 'Frequency', 'Histogram of UNION Column', '../../data/data_vsl/histogram_union_column.png')

    scatter_plot(or_column, 'Index', 'OR', 'Scatter Plot of OR Column', '../../data/data_vsl/scatter_or_column.png')
    box_plot(or_column, 'OR', 'Box Plot of OR Column', '../../data/data_vsl/boxplot_or_column.png')
    bar_plot(or_column, 'Index', 'OR', 'Bar data_vsl of OR Column', '../../data/data_vsl/bardata_vsl_or_column.png')
    pie_plot(or_column, 'Pie Plot of OR Column', '../../data/data_vsl/pieplot_or_column.png')
    histogram_plot(or_column, 'OR', 'Frequency', 'Histogram of OR Column', '../../data/data_vsl/histogram_or_column.png')

    scatter_plot(and_column, 'Index', 'AND', 'Scatter Plot of AND Column', '../../data/data_vsl/scatter_and_column.png')
    box_plot(and_column, 'AND', 'Box Plot of AND Column', '../../data/data_vsl/boxplot_and_column.png')
    bar_plot(and_column, 'Index', 'AND', 'Bar data_vsl of AND Column', '../../data/data_vsl/bardata_vsl_and_column.png')
    pie_plot(and_column, 'Pie Plot of AND Column', '../../data/data_vsl/pieplot_and_column.png')
    histogram_plot(and_column, 'AND', 'Frequency', 'Histogram of AND Column', '../../data/data_vsl/histogram_and_column.png')