import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data_backup = pd.read_csv('../data/definedata.csv')
features = data_backup.columns.tolist()


for feature in features:
    count_1 = (data_backup[feature] == 1).sum()
    count_0 = (data_backup[feature] == 0).sum()
    
    plt.figure(figsize=(6, 4))
    plt.bar(['0', '1'], [count_0, count_1], color=['blue', 'orange'])
    plt.title(f"Distribution of Feature '{feature}'")
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.savefig(feature + '_distribution.png') 
    
    print(f"Feature '{feature}': 1s = {count_1}, 0s = {count_0}")
