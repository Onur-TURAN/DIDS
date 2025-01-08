import pandas as pd
import matplotlib.pyplot as plt

file_path = '../../data/updated_sql_dataset.csv'
data = pd.read_csv(file_path)

first_five_rows = data.head()
print(first_five_rows)

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=first_five_rows.values, colLabels=first_five_rows.columns, cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)

#why am i doing this?
cell_dict = table.get_celld()
for i in range(len(first_five_rows.columns)):
    if first_five_rows.columns[i] == 'Query':
        cell_dict[(0, i)].set_width(0.6)
        for j in range(1, len(first_five_rows) + 1):
            cell_dict[(j, i)].set_width(0.6)
    else:
        cell_dict[(0, i)].set_width(0.1)
        for j in range(1, len(first_five_rows) + 1):
            cell_dict[(j, i)].set_width(0.1)

plt.savefig('../../data/graph/update_column.png')
plt.show()