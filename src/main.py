import pandas as pd 
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import time
import matplotlib.pyplot as plt

#data = pd.read_csv('../data/train.csv')  # Correctly define 'data'
data = pd.read_csv('../data/traindata.csv')
features = data.columns.tolist()


for feature in features:
    if data[feature].isin([0, 1]).all():
        count_1 = (data[feature] == 1).sum()
        count_0 = (data[feature] == 0).sum()
    # general Plot graph code
        plt.figure(figsize=(6, 4))
        plt.bar(['0', '1'], [count_0, count_1], color=['blue', 'orange'])
        plt.title(f"Distribution of Feature '{feature}'")
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.savefig(f'../data/plot/{feature}_distribution.png') 
    
        print(f"Feature '{feature}': 1s = {count_1}, 0s = {count_0}")



vectorizer = TfidfVectorizer()

X_query = vectorizer.fit_transform(data['Query'])
X_other = data.iloc[:, 2:]
X = np.hstack((X_query.toarray(), X_other))

y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(),
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier()
}
# genereal Train and evaluate each model 
for name, model in models.items():
    start_time = time.time()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    end_time = time.time()
    elapsed_time = end_time - start_time
    joblib.dump(model, f'{name.replace(" ", "_").lower()}_model.pkl')
    print(f"Model '{name}' trained and saved in {elapsed_time:.2f} seconds.")
