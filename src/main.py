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
# Removed unused import of Counter

#data = pd.read_csv('../data/train.csv')  # Correctly define 'data'
data_backup = pd.read_csv('../data/definedata.csv')
features = data_backup.columns.tolist()
import matplotlib.pyplot as plt

for feature in features:
    count_1 = (data_backup[feature] == 1).sum()
    count_0 = (data_backup[feature] == 0).sum()
    
    # Plot the distribution
    plt.figure(figsize=(6, 4))
    plt.bar(['0', '1'], [count_0, count_1], color=['blue', 'orange'])
    plt.title(f"Distribution of Feature '{feature}'")
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.savefig(feature + '_distribution.png') 
    
    print(f"Feature '{feature}': 1s = {count_1}, 0s = {count_0}")



vectorizer = TfidfVectorizer()



X_test = np.array(columns_header)
print(len(X_test))

X_query = vectorizer.fit_transform(data['Text'])  # Assuming 'Text' column exists in 'data'
X_other = np.random.rand(len(data), 5)  # Example placeholder for additional features
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
