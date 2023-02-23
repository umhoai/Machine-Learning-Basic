import pandas as pd

# read the JSON file into a DataFrame
df = pd.read_json('path/to/file.json')

# display the DataFrame
print(df)

df = pd.read_json('path/to/file.json', orient='records')

import json

# example JSON string
json_str = '{"name": "Alice", "age": 25, "city": "New York"}'

# convert the JSON string to a DataFrame
df = pd.read_json(json.loads(json_str))
