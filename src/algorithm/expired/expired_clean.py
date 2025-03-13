import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def clean_missing_values(df):
    df_filled = df.fillna(df.mean(numeric_only=True))
    return df_filled
#gptreferans
def clean_noisy_data(df):
    threshold = 100  # Örnek eşik değeri
    df_cleaned = df[df.applymap(lambda x: isinstance(x, (int, float)) and x < threshold or not isinstance(x, (int, float)))]
    return df_cleaned

def detect_outliers(df):
    z_scores = np.abs((df - df.mean(numeric_only=True)) / df.std(numeric_only=True))
    outliers = (z_scores > 3).any(axis=1)
    return df[outliers], df[~outliers]

if __name__ == "__main__":
    file_path = '../../data/Modified_SQL_Dataset.csv'
    df = load_data(file_path)

    # missingclean
    print("Table 4.1 Sample Dataset before Cleaning Missing Values")
    print(df.head())
    df_cleaned_missing = clean_missing_values(df)
    print("Table 4.2 Sample Dataset after Cleaning Missing Values")
    print(df_cleaned_missing.head())
    save_data(df_cleaned_missing, '../../data/cleaningprocess/cleaned_missing_values.csv')

    # noisyclean
    print("Table 4.3 Sample Dataset before Cleaning Noisy Data")
    print(df_cleaned_missing.head())
    df_cleaned_noisy = clean_noisy_data(df_cleaned_missing)
    print("Table 4.4 Sample Dataset after Cleaning Noisy Data")
    print(df_cleaned_noisy.head())
    save_data(df_cleaned_noisy, '../../data/cleaningprocess/cleaned_noisy_data.csv')

    # outlierclean
    print("Table 4.5 Sample Dataset before Outlier Detection")
    print(df_cleaned_noisy.head())
    outliers, df_no_outliers = detect_outliers(df_cleaned_noisy)
    print("Table 4.6 Outliers Detected")
    print(outliers.head())
    print("Table 4.7 Sample Dataset after Removing Outliers")
    print(df_no_outliers.head())
    save_data(df_no_outliers, '../../data/cleaningprocess/cleaned_no_outliers.csv')