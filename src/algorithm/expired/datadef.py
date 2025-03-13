import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('d:\\code\\DIDS\\src\\2_datadef\\updated_sql_dataset.csv')

# Yeni sütunları ekle
columns_to_add = {
    'contains_parentheses': lambda x: 1 if '(' in x else 0,
    'contains_three_nulls': lambda x: 1 if x.lower().count('null') >= 3 else 0,
    'contains_select_count': lambda x: 1 if 'select count' in x.lower() else 0,
    'contains_double_pipe': lambda x: 1 if '||' in x else 0,
    'contains_double_closing_parentheses': lambda x: 1 if '))' in x else 0,
    'contains_double_quote_1': lambda x: 1 if '"1"' in x else 0,
    'contains_sleep': lambda x: 1 if 'sleep' in x.lower() else 0,
    'contains_0x': lambda x: 1 if '0x' in x.lower() else 0,
    'contains_parentheses_double_pipe': lambda x: 1 if ') || (' in x else 0,
    'contains_union_all': lambda x: 1 if 'union all' in x.lower() else 0,
    'contains_benchmark': lambda x: 1 if 'benchmark' in x.lower() else 0,
    'contains_updatexml': lambda x: 1 if 'updatexml' in x.lower() else 0,
    'contains_extractvalue': lambda x: 1 if 'extractvalue' in x.lower() else 0,
    'contains_concat': lambda x: 1 if 'concat' in x.lower() else 0,
    'contains_char': lambda x: 1 if 'char' in x.lower() else 0,
    'contains_rand': lambda x: 1 if 'rand' in x.lower() else 0,
    'contains_floor': lambda x: 1 if 'floor' in x.lower() else 0,
    'contains_hex': lambda x: 1 if 'hex' in x.lower() else 0,
    'contains_md5': lambda x: 1 if 'md5' in x.lower() else 0,
    'contains_sha1': lambda x: 1 if 'sha1' in x.lower() else 0,
    'contains_group_by': lambda x: 1 if 'group by' in x.lower() else 0,
    'contains_order_by': lambda x: 1 if 'order by' in x.lower() else 0,
    'contains_having': lambda x: 1 if 'having' in x.lower() else 0,
    'contains_limit': lambda x: 1 if 'limit' in x.lower() else 0,
    'contains_case_when': lambda x: 1 if 'case when' in x.lower() else 0,
    'contains_if': lambda x: 1 if 'if' in x.lower() else 0,
    'contains_from': lambda x: 1 if 'from' in x.lower() else 0,
    'contains_where': lambda x: 1 if 'where' in x.lower() else 0,
    'contains_join': lambda x: 1 if 'join' in x.lower() else 0,
    'contains_like': lambda x: 1 if 'like' in x.lower() else 0,
}

for column, func in columns_to_add.items():
    df[column] = df['Query'].apply(func)

df.to_csv('d:\\code\\DIDS\\src\\2_datadef\\updated_sql_dataset_with_new_columns.csv', index=False)