
# find and display IDs where col1 == col2 in both dataframes
equal_ids = set(df1[df1['col1'] == df1['col2']]['id']).intersection(set(df2[df2['col1'] == df2['col2']]['id']))
print(equal_ids)
