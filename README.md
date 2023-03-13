from drain3 import Drain3Parser
parser = Drain3Parser()

df['response_body'] = df['response_body'].apply(lambda x: parser.parse(x).to_json() if x else '')

import json
import dateutil.parser

def clean_json(json_text):
    # Convert the JSON text to a dictionary
    json_dict = json.loads(json_text)

    # Remove leading/trailing spaces from string values
    for key in json_dict:
        if isinstance(json_dict[key], str):
            json_dict[key] = json_dict[key].strip()

    # Convert timestamp to ISO format
    if 'timestamp' in json_dict:
        json_dict['timestamp'] = dateutil.parser.parse(json_dict['timestamp']).isoformat()

    # Convert amount to float
    if 'amount' in json_dict:
        json_dict['amount'] = float(''.join(filter(str.isdigit, json_dict['amount'])))/100

    # Convert the dictionary back to JSON
    cleaned_json = json.dumps(json_dict)
    return cleaned_json

df['response_body'] = df['response_body'].apply(lambda x: clean_json(x) if x else '')


def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values('% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n" "There are " + str(mis_val_table_ren_columns.shape[0]) + " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns
