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


