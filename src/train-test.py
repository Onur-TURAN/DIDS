import pandas as pd
from sklearn.model_selection import train_test_split

# Veriyi yükle
data = pd.read_csv('../data/Modified_SQL_Dataset.csv')

# Veriyi karıştır (shuffle)
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Özellikler ve hedef değişkeni ayır
X = data['Query']
y = data['Label']

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Eğitim ve test setlerini kontrol et
print("Eğitim seti boyutu:", X_train.shape)
print("Test seti boyutu:", X_test.shape)

# Eğitim ve test setlerini CSV dosyalarına kaydet
train_data = pd.DataFrame({'Query': X_train, 'Label': y_train})
test_data = pd.DataFrame({'Query': X_test, 'Label': y_test})

train_data.to_csv('../data/train_data.csv', index=False)
test_data.to_csv('../data/test_data.csv', index=False)