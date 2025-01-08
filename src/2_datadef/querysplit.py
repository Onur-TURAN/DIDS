import pandas as pd
import matplotlib.pyplot as plt

file_path = '../../data/Modified_SQL_Dataset.csv'
data = pd.read_csv(file_path)

column_descriptions = {
    'Query': 'The SQL query being analyzed for potential SQL injection.',
    'Label': 'Indicates whether the query is malicious (1) or benign (0).'
}

column_summary = pd.DataFrame(list(column_descriptions.items()), columns=['Column', 'Description'])
print(column_summary)

def check_component(query, component):
    return 1 if component in query.upper() else 0

data['SELECT'] = data['Query'].apply(lambda x: check_component(x, 'SELECT'))
data['UNION'] = data['Query'].apply(lambda x: check_component(x, 'UNION'))
data['OR'] = data['Query'].apply(lambda x: check_component(x, 'OR'))
data['AND'] = data['Query'].apply(lambda x: check_component(x, 'AND'))

print(data.head())

column_summary.to_csv('column_summary.csv', index=False)
data.to_csv('updated_sql_dataset.csv', index=False)

def plot_component_distribution(data):
    components = ['SELECT', 'UNION', 'OR', 'AND']
    counts = [data[component].sum() for component in components]

    plt.figure(figsize=(10, 6))
    plt.bar(components, counts, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Components')
    plt.ylabel('Count')
    plt.title('Distribution of SQL Query Components')
    plt.show()

# Grafiği oluştur ve göster
plot_component_distribution(data)