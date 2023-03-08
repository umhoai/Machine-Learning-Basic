import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

# Áp dụng stemming cho từng từ trong cột văn bản
for i in range(len(data)):
    text = data.loc[i, 'text_column']
    words = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    data.loc[i, 'stemmed_text'] = ' '.join(stemmed_words)
