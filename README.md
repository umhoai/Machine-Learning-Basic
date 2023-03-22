# Hàm xử lý
def remove_short_strings(s):
    if isinstance(s, str) and len(s) <= threshold:
        return np.nan
    else:
        return s

# Áp dụng hàm xử lý trên dataframe
df_cleaned = df.applymap(remove_short_strings)

# Xóa các hàng chứa giá trị NaN
df_cleaned = df_cleaned.dropna(how='all')
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
# Danh sách các chuỗi ký tự
strings = ['this is a string with more than three words', 'this is another string', 'short string', 'yet another string with more than three words']

# Ngưỡng số từ
threshold = 3

# Loại bỏ các chuỗi có số từ ít hơn ngưỡng
filtered_strings = [s for s in strings if len(s.split()) >= threshold]

print(filtered_strings) # Kết quả: ['this is a string with more than three words', 'this is another string', 'yet another string with more than three words']


