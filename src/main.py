import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import time

data = pd.read_csv('../data/train.csv')
data_backup = pd.read_csv('../backup_data/Modified_SQL_Dataset.csv')
""" FALSE parameter and wrong check line
vectorizer = TfidfVectorizer()
X_query = vectorizer.fit_transform(data['Query'])

X_other = np.array([pd.read_csv(file).columns.values for file in data_backup])
print(X_other)

"""

X = np.hstack((X_query.toarray(), X_other))

y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(),
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier()
}

for name, model in models.items():
    start_time = time.time()
    model.fit(X_train, y_train)
    end_time = time.time()
    elapsed_time = end_time - start_time
    joblib.dump(model, f'{name.replace(" ", "_").lower()}_model.pkl')
    print(f"Model '{name}' trained and saved in {elapsed_time:.2f} seconds.")
