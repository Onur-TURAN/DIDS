import pandas as pd

df = pd.read_csv('../../data/definedata.csv')

# özet tablo için bunlar yeterli olabilir, ama fazlası gerekebilir bakmak lazım
summary = pd.DataFrame({
    'Column Name': df.columns,
    'Data Type': df.dtypes,
    'Non-Null Count': df.notnull().sum(),
    'Unique Values': df.nunique(),
    'Example Value': df.iloc[0]
})

# exportt
summary.to_excel('summary_table.xlsx', index=False)

print("Özet tablo oluşturuldu ve 'summary_table.xlsx' dosyasına kaydedildi.")