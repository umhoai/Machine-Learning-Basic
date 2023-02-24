import pandas as pd

# Load the 'Sheet1' and 'Sheet2' sheets in the 'data.xlsx' Excel file into a single Pandas DataFrame
dfs = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'Sheet2'])

# Concatenate the DataFrames into a single DataFrame
df = pd.concat(dfs, ignore_index=True)

# Display the DataFrame
print(df)
