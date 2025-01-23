import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import argparse

parser = argparse.ArgumentParser(description='Yeni verileri girin.')
parser.add_argument('--queries', nargs='+', help='SQL sorguları', required=True)
parser.add_argument('--selects', nargs='+', type=int, help='SELECT değerleri', required=True)
parser.add_argument('--unions', nargs='+', type=int, help='UNION değerleri', required=True)
parser.add_argument('--ors', nargs='+', type=int, help='OR değerleri', required=True)
parser.add_argument('--ands', nargs='+', type=int, help='AND değerleri', required=True)

args = parser.parse_args()

new_data = pd.DataFrame({
    'Query': args.queries,
    'SELECT': args.selects,
    'UNION': args.unions,
    'OR': args.ors,
    'AND': args.ands
})

vectorizer = TfidfVectorizer()
X_query = vectorizer.fit_transform(new_data['Query'])

X_other = new_data[['SELECT', 'UNION', 'OR', 'AND']].values

X_combined = np.hstack((X_query.toarray(), X_other))

model = joblib.load('random_forest_model.pkl')

predictions = model.predict(X_combined)

new_data['Prediction'] = predictions
print(new_data)
