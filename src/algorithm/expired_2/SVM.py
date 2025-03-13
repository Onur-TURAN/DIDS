import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import matplotlib.pyplot as plt

data = pd.read_csv('../../data/traindata.csv')

X = data[['Query', 'SELECT', 'UNION', 'OR', 'AND']]
y = data['Label']

vectorizer = TfidfVectorizer()
X_query = vectorizer.fit_transform(X['Query'])

X_other = X[['SELECT', 'UNION', 'OR', 'AND']].values
X_combined = pd.concat([pd.DataFrame(X_query.toarray()), pd.DataFrame(X_other, columns=['SELECT', 'UNION', 'OR', 'AND'])], axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

model = SVC()

start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()

y_pred = model.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary')
recall = recall_score(y_test, y_pred, average='binary')
f1 = f1_score(y_test, y_pred, average='binary')
training_time = end_time - start_time

metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Score': [accuracy, precision, recall, f1]
})

plt.figure(figsize=(10, 6))
plt.bar(metrics['Metric'], metrics['Score'], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('SVM Performance Metrics')
plt.savefig('../../data/graph/svm.png')
