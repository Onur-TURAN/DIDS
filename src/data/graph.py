import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Veri setini yükleyin
df = pd.read_csv('../../data/definedata.csv')

# Kayıt dizinini oluşturun
output_dir = '../../data/graph2/'
os.makedirs(output_dir, exist_ok=True)

# Scatter Plot: 1 olan sütunların dağılımı ile Label'i 1 olanların karşılaştırılması
if 'Label' in df.columns:
    plt.figure(figsize=(10, 5))
    for column in df.columns[2:]:
        if df[column].sum() > 0:
            sns.scatterplot(x=df[column], y=df['Label'])
    plt.title('Scatter Plot of Columns with 1 Values vs Label')
    plt.xlabel('Columns with 1 Values')
    plt.ylabel('Label')
    plt.savefig(os.path.join(output_dir, 'scatter_plot.png'))
    plt.close()
else:
    print("Error: 'Label' column not found in the DataFrame.")

# Count Plot: Her sütunun kaç 1 ve 0 olduğunu gösterir
for column in df.columns[2:]:
    plt.figure(figsize=(10, 5))
    ax = sns.countplot(x=column, data=df)
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), 
                    textcoords='offset points')
    plt.title(f'Count Plot for {column}')
    plt.savefig(os.path.join(output_dir, f'count_plot_{column}.png'))
    plt.close()

# Pie Chart: En çok 1 olan 5 sütun ve en çok 0 olan 5 sütun
top_5_ones = df[df.columns[2:]].sum().sort_values(ascending=False).head(5)
top_5_zeros = (len(df) - df[df.columns[2:]].sum()).sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 5))
top_5_ones.plot(kind='pie', autopct='%1.1f%%', title='Top 5 Columns with Most 1s')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'top_5_ones_pie_chart.png'))
plt.close()

plt.figure(figsize=(10, 5))
top_5_zeros.plot(kind='pie', autopct='%1.1f%%', title='Top 5 Columns with Most 0s')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'top_5_zeros_pie_chart.png'))
plt.close()

# Histogram: Label'i 1 olanlar ile diğer sütunlarda sıfır olanların bağıntısı
for column in df.columns[2:]:
    plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x=column, hue='Label', multiple='stack', bins=2)
    plt.title(f'Histogram for {column} by Label')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, f'histogram_{column}.png'))
    plt.close()

# Heatmap: Label sütunundaki değeri 1 olanların sayısı ile diğer sütunlardaki 1 ve 0 sayılarının grafiği
label_1_df = df[df['Label'] == 1]
numeric_columns = label_1_df.select_dtypes(include=['number']).columns
correlation_matrix = label_1_df[numeric_columns].corr()
plt.figure(figsize=(15, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Label 1 Rows')
plt.savefig(os.path.join(output_dir, 'correlation_matrix_heatmap.png'))
plt.close()