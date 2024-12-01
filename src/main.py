import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Load the data

data = pd.read_csv('../data/Modified_SQL_Dataset.csv')
data.head()
