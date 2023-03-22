def process_one_char(string):
    return " ".join([token.text for token in nlp(string) if len(str(token))>1])
----------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataframe with preprocessed text data
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "text": [
        "Global warming is a major issue that needs to be addressed",
        "The melting of the polar ice caps is a clear sign of climate change",
        "Greenhouse gas emissions from human activity are causing climate change",
        "Rising sea levels are a threat to coastal communities",
        "Renewable energy sources such as solar and wind power can help mitigate climate change"
    ]
})

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text"])

# Extract the most important words
feature_names = tfidf_vectorizer.get_feature_names()
top_words = []
for i in range(len(df)):
    tfidf_scores = zip(feature_names, tfidf_matrix[i].toarray()[0])
    sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
    top_words.append([word for word, score in sorted_scores][:5])

# Add top words to the dataframe
df["top_words"] = top_words

# Print the dataframe
print(df)


---------------------------------------------------------------------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataframe with preprocessed text data
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "text": [
        "Global warming is a major issue that needs to be addressed",
        "The melting of the polar ice caps is a clear sign of climate change",
        "Greenhouse gas emissions from human activity are causing climate change",
        "Rising sea levels are a threat to coastal communities",
        "Renewable energy sources such as solar and wind power can help mitigate climate change"
    ]
})

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text"])

# Extract the most important words
feature_names = tfidf_vectorizer.get_feature_names()
top_words = []
for i in range(len(df)):
    tfidf_scores = zip(feature_names, tfidf_matrix[i].toarray()[0])
    sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
    top_words.append([word for word, score in sorted_scores][:5])

# Add top words to the dataframe
df["top_words"] = top_words

# Print the dataframe
print(df)



-------------------
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Read preprocessed text data from CSV file
df = pd.read_csv("preprocessed_data.csv")

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text"])

# Get feature names
feature_names = tfidf_vectorizer.get_feature_names()

# Define query
query = "important topic"

# Transform query using the vectorizer
query_tfidf = tfidf_vectorizer.transform([query])

# Extract the most important words for the query
tfidf_scores = zip(feature_names, query_tfidf.toarray()[0])
sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
top_words = [word for word, score in sorted_scores][:5]

# Print the most important words for the query
print("Top words for query '{}'".format(query))
print(", ".join(top_words))



