import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını okuma
df = pd.read_csv('..\..\data\Modified_SQL_Dataset.csv')

# Hedef sütunu ve X1 sütununu seçme
target_column = df['Label']
x1_column = df['Query']  # X1 sütunu olarak Query sütunu seçilmiştir

# 3.1.1 Scatter Plot Graph of Target Column Name
plt.figure(figsize=(10, 6))
plt.scatter(range(len(target_column)), target_column, color='skyblue')
plt.xlabel('Index')
plt.ylabel('Label')
plt.title('Scatter Plot of Label Column')
plt.savefig('../../data/graph/scatter_label_column.png')

# 3.1.2 Box Plot Graph of Target Column Name
plt.figure(figsize=(10, 6))
plt.boxplot(target_column)
plt.ylabel('Label')
plt.title('Box Plot of Label Column')
plt.savefig('../../data/graph/boxplot_label_column.png')

# 3.1.3 Bar Graph of Target Column Name
plt.figure(figsize=(10, 6))
plt.bar(range(len(target_column)), target_column, color='skyblue')
plt.xlabel('Index')
plt.ylabel('Label')
plt.title('Bar Graph of Label Column')
plt.savefig('../../data/graph/bargraph_label_column.png')

# 3.1.4 Pie Plot Graph of Target Column Name
plt.figure(figsize=(10, 6))
plt.pie(target_column.value_counts(), labels=target_column.value_counts().index, autopct='%1.1f%%')
plt.title('Pie Plot of Label Column')
plt.savefig('../../data/graph/pieplot_label_column.png')

# 3.1.5 Histogram Plot Graph of Target Column Name
plt.figure(figsize=(10, 6))
plt.hist(target_column, bins=20, color='skyblue')
plt.xlabel('Label')
plt.ylabel('Frequency')
plt.title('Histogram of Label Column')
plt.savefig('../../data/graph/histogram_label_column.png')

# 3.2.1 Scatter Plot Graph of X1
plt.figure(figsize=(10, 6))
plt.scatter(range(len(x1_column)), x1_column, color='skyblue')
plt.xlabel('Index')
plt.ylabel('Query')
plt.title('Scatter Plot of Query Column')
plt.savefig('../../data/graph/scatter_query_column.png')

# 3.2.2 Box Plot Graph of X1
plt.figure(figsize=(10, 6))
plt.boxplot(x1_column)
plt.ylabel('Query')
plt.title('Box Plot of Query Column')
plt.savefig('../../data/graph/boxplot_query_column.png')

# 3.2.3 Bar Graph of X1
plt.figure(figsize=(10, 6))
plt.bar(range(len(x1_column)), x1_column, color='skyblue')
plt.xlabel('Index')
plt.ylabel('Query')
plt.title('Bar Graph of Query Column')
plt.savefig('../../data/graph/bargraph_query_column.png')

# 3.2.4 Pie Plot Graph of X1
plt.figure(figsize=(10, 6))
plt.pie(x1_column.value_counts(), labels=x1_column.value_counts().index, autopct='%1.1f%%')
plt.title('Pie Plot of Query Column')
plt.savefig('../../data/graph/pieplot_query_column.png')

# 3.2.5 Histogram Plot Graph of X1
plt.figure(figsize=(10, 6))
plt.hist(x1_column, bins=20, color='skyblue')
plt.xlabel('Query')
plt.ylabel('Frequency')
plt.title('Histogram of Query Column')
plt.savefig('../../data/graph/histogram_query_column.png')