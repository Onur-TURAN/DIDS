import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('../../data/backup_data/Modified_SQL_Dataset.csv')

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
    'contains_insert': lambda x: 1 if 'insert' in x.lower() else 0,
    'contains_delete': lambda x: 1 if 'delete' in x.lower() else 0,
    'contains_update': lambda x: 1 if 'update' in x.lower() else 0,
    'contains_union_select': lambda x: 1 if 'union select' in x.lower() else 0,
    'contains_sleep_time': lambda x: 1 if 'pg_sleep' in x.lower() or 'waitfor delay' in x.lower() else 0,
    'contains_exec': lambda x: 1 if 'exec' in x.lower() else 0,
    'contains_xp_cmdshell': lambda x: 1 if 'xp_cmdshell' in x.lower() else 0,
    'contains_load_file': lambda x: 1 if 'load_file' in x.lower() else 0,
    'contains_information_schema': lambda x: 1 if 'information_schema' in x.lower() else 0,
    'contains_select_version': lambda x: 1 if 'select version' in x.lower() or 'select @@version' in x.lower() else 0,
    'contains_v$version': lambda x: 1 if 'v$version' in x.lower() else 0,
    'contains_sysobjects': lambda x: 1 if 'sysobjects' in x.lower() else 0,
    'contains_syscolumns': lambda x: 1 if 'syscolumns' in x.lower() else 0,
    'contains_all_tables': lambda x: 1 if 'all_tables' in x.lower() else 0,
    'contains_all_tab_columns': lambda x: 1 if 'all_tab_columns' in x.lower() else 0,
    'contains_dba_role_privs': lambda x: 1 if 'dba_role_privs' in x.lower() else 0,
    'contains_sys_users': lambda x: 1 if 'sys.user$' in x.lower() else 0,
    'contains_v$instance': lambda x: 1 if 'v$instance' in x.lower() else 0,
    'contains_global_name': lambda x: 1 if 'global_name' in x.lower() else 0,
    'contains_utl_inaddr': lambda x: 1 if 'utl_inaddr' in x.lower() else 0,
    'contains_utl_http': lambda x: 1 if 'utl_http' in x.lower() else 0,
}

for column, func in columns_to_add.items():
    df[column] = df['Query'].apply(func)

df.to_csv('../../data/definedata.csv', index=False)