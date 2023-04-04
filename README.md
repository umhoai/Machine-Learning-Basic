def add_spaces(text, lst):
    for word in lst:
        text = text.replace(word, ' ' + word)
    return text

df['text'] = df['text'].apply(add_spaces, args=([ 'one', 'without', 'another'],))
print(df)
