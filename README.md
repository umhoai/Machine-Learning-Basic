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


import re
import pandas as pd

# Define the mask patterns
mask_patterns = [
    {"regex_pattern": "((?<=[^A-Za-z0-9])|^)(([0-9a-f]{2,}:){3,}([0-9a-f]{2,}))((?=[^A-Za-z0-9])|$)", "mask_with": "ID"},
    {"regex_pattern": "((?<=[^A-Za-z0-9])|^)(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})((?=[^A-Za-z0-9])|$)", "mask_with": "IP"},
    {"regex_pattern": "((?<=[^A-Za-z0-9])|^)([0-9a-f]{6,} ?){3,}((?=[^A-Za-z0-9])|$)", "mask_with": "SEQ"},
    {"regex_pattern": "((?<=[^A-Za-z0-9])|^)([0-9A-F]{4} ?){4,}((?=[^A-Za-z0-9])|$)", "mask_with": "SEQ"},
    {"regex_pattern": "((?<=[^A-Za-z0-9])|^)(0x[a-f0-9A-F]+)((?=[^A-Za-z0-9])|$)", "mask_with": "HEX"},
    {"regex_pattern": "((?<=[^A-Za-z0-9])|^)([\\-\\+]?\\d+)((?=[^A-Za-z0-9])|$)", "mask_with": "NUM"},
    {"regex_pattern": "(?<=executed cmd )(\".+?\")", "mask_with": "CMD"}
]

# Define the mask function
def mask_value(value, patterns):
    # Check if the value is a string
    if isinstance(value, str):
        # Apply each mask pattern to the value
        for pattern in patterns:
            regex_pattern = pattern["regex_pattern"]
            mask_with = pattern["mask_with"]
            value = re.sub(regex_pattern, mask_with, value)
    return value

# Load the data into a DataFrame
df = pd.read_csv('data.csv')

# Mask values in the entire DataFrame
df = df.applymap(lambda x: mask_value(x, mask_patterns))
