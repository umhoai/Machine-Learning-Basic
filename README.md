# Combine the patterns using the "or" operator and compile the regex
combined_regex = '|'.join(regex_patterns)
regex = re.compile(combined_regex)

# Apply the regex to the "text" column using str.replace()
df['text'] = df['text'].str.replace(regex, '', regex=True)
