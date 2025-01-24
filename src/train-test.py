import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('../data/2_preproc_alldata.csv')

data = data.sample(frac=1, random_state=42).reset_index(drop=True)

X = data[['Query', 'SELECT', 'UNION', 'OR', 'AND']]
y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("Eğitim seti boyutu:", X_train.shape)
print("Test seti boyutu:", X_test.shape)

train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

train_data.to_csv('../data/traindata.csv', index=False)
test_data.to_csv('../data/test.csv', index=False)
