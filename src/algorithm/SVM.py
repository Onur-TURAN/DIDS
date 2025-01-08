import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import matplotlib.pyplot as plt

# Veriyi yükle
data = pd.read_csv('../../data/train_data.csv')

# Özellikler ve hedef değişkeni ayır
X = data['Query']
y = data['Label']

# Metin verilerini sayısal değerlere dönüştür
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM modelini oluştur
model = SVC()

# Modeli eğit ve süreyi ölç
start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()

# Tahmin yap
y_pred = model.predict(X_test)

# Performans metriklerini hesapla
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
training_time = end_time - start_time

# Performans metriklerini ve eğitim süresini bir DataFrame'e ekle
metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Score': [accuracy, precision, recall, f1]
})

# Grafik oluştur
plt.figure(figsize=(10, 6))
plt.bar(metrics['Metric'], metrics['Score'], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('SVM Performance Metrics')
plt.savefig('../../data/graph/svm.png')