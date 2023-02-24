# Load the 'Sheet1' and 'Sheet2' sheets in the 'data.xlsx' Excel file into separate Pandas DataFrames
df_sheet1 = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df_sheet2 = pd.read_excel('data.xlsx', sheet_name='Sheet2')

# Divide each sheet into 3 columns
df_sheet1 = pd.DataFrame(df_sheet1.values.reshape(-1, 3), columns=['col1', 'col2', 'col3'])
df_sheet2 = pd.DataFrame(df_sheet2.values.reshape(-1, 3), columns=['col1', 'col2', 'col3'])

# Display the resulting DataFrames
print('Sheet1:')
print(df_sheet1)
print('\nSheet2:')
print(df_sheet2)
