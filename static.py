import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

if not os.path.exists("graph"):
    os.makedirs("graph")

# CSV dosyasını yükle
data = pd.read_csv("data/test.csv")

# Veri çerçevesini incele
print(data.info())
print(data.describe())

# İlk 5 satırı görüntüle
print(data.head())

# Sınıflandırma için etiket sayısını görselleştir
plt.figure(figsize=(8, 5))
sns.countplot(x='Label', data=data)
plt.title('Distribution of Labels')
plt.savefig("graph/label_distribution.png")
plt.show()

# Sorgu uzunluklarını hesapla ve görselleştir
data['query_length'] = data['Query'].apply(len)

plt.figure(figsize=(10, 6))
sns.histplot(data['query_length'], bins=20, kde=True)
plt.title('Distribution of Query Lengths')
plt.xlabel('Query Length')
plt.ylabel('Frequency')
plt.savefig("graph/query_length_distribution.png")
plt.show()
