import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import matplotlib.pyplot as plt

data = pd.read_csv('../../data/updated_sql_dataset_v2.csv')

features = ['Query', 'Label', 'SELECT', 'UNION', 'OR', 'AND']
X = data[features]
y = data['Label']

vectorizer = TfidfVectorizer()
X_query = vectorizer.fit_transform(X['Query'])

X_other = X.drop(columns=['Query', 'Label'])
X_combined = pd.concat([pd.DataFrame(X_query.toarray()), X_other.reset_index(drop=True)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()

start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()

y_pred = model.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
training_time = end_time - start_time

metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Score': [accuracy, precision, recall, f1]
})

# Grafik oluştur
plt.figure(figsize=(10, 6))
plt.bar(metrics['Metric'], metrics['Score'], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('Decision Tree Performance Metrics')
plt.savefig('../../data/graph/DecisionTreeClassifier_metrics.png')