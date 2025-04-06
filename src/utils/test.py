# Heatmap: Shows the correlation between columns with values of 1 and the Label column
label_1_df = df[df['Label'] == 1]
numeric_columns = label_1_df.select_dtypes(include=['number']).columns
correlation_matrix = label_1_df[numeric_columns].corr()
plt.figure(figsize=(15, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Label 1 Rows')
plt.savefig(os.path.join(output_dir, 'correlation_matrix_heatmap.png'))
plt.close()