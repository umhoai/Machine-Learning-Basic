from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
# Lemmatize
        words = item.split()
        words = [wnl.lemmatize(word) for word in words]
        item = ' '.join(words)
