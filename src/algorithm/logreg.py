import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from scipy.sparse import hstack
import matplotlib.pyplot as plt

data = pd.read_csv('../../data/updated_sql_dataset_v2.csv')
X = data[['Query', 'SELECT', 'UNION', 'OR', 'AND']]
y = data['Label']

vectorizer = TfidfVectorizer()
X_query = vectorizer.fit_transform(X['Query'])

X_other_features = X[['SELECT', 'UNION', 'OR', 'AND']].values

X_combined = hstack([X_query, X_other_features])

X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

model = LogisticRegression()

start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()

y_pred = model.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
training_time = end_time - start_time

metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Score': [accuracy, precision, recall, f1]
})

plt.figure(figsize=(10, 6))
plt.bar(metrics['Metric'], metrics['Score'], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('Logistic Regression Performance Metrics')
plt.savefig('../../data/graph/logreg.png')
