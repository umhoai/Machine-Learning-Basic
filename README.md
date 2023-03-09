# Tách từ và stemming từng từ trong cột text
df['stemmed_text'] = df['text'].apply(lambda x: ' '.join([stemmer.stem(word) for word in word_tokenize(x)]))
