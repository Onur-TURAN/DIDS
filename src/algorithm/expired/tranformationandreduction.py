import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, KBinsDiscretizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.decomposition import PCA

def load_data(file_path):
    return pd.read_csv(file_path)

def save_plot(fig, file_path):
    fig.savefig(file_path)

def normalize_data(data):
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    return pd.DataFrame(normalized_data, columns=data.columns)

def feature_selection(data, target):
    selector = SelectKBest(score_func=chi2, k=3)
    selected_features = selector.fit_transform(data, target)
    return pd.DataFrame(selected_features, columns=['SELECT', 'UNION', 'OR'])

def discretize_data(data):
    discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
    discretized_data = discretizer.fit_transform(data)
    return pd.DataFrame(discretized_data, columns=data.columns)

def reduce_dimensionality(data):
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(data)
    return pd.DataFrame(reduced_data, columns=['PC1', 'PC2'])

if __name__ == "__main__":
    file_path = '../../data/updated_sql_dataset.csv'
    df = load_data(file_path)

    normalized_df = normalize_data(df[['SELECT', 'UNION', 'OR', 'AND']])
    normalized_df.to_csv('../../data/cleaningprocess/normalized_data.csv', index=False)

    selected_features_df = feature_selection(df[['SELECT', 'UNION', 'OR', 'AND']], df['Label'])
    selected_features_df.to_csv('../../data/cleaningprocess/selected_features.csv', index=False)

    discretized_df = discretize_data(df[['SELECT', 'UNION', 'OR', 'AND']])
    discretized_df.to_csv('../../data/cleaningprocess/discretized_data.csv', index=False)

    reduced_df = reduce_dimensionality(df[['SELECT', 'UNION', 'OR', 'AND']])
    reduced_df.to_csv('../../data/cleaningprocess/reduced_data.csv', index=False)