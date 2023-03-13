def process_lower_text(text):
    return text.lower()
def process_one_char(string):
    return " ".join([token.text for token in nlp(string) if len(str(token))>1])
def pre_preprocess(current_text ):
    current_text = process_lower_text(current_text )
    current_text = process_punctuation(current_text)
    return current_text 

import re

# Regular expression pattern for an ISO 8601 timestamp with UTC timezone
iso_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z'

# Example timestamp string
timestamp_string = '2022-03-13T08:30:00.123456Z'

# Match the timestamp string against the regular expression pattern
match = re.match(iso_pattern, timestamp_string)

# Print whether the timestamp string matches the pattern
print(bool(match))
