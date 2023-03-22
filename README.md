[-\w’\d]+(?:\s+[-\w’\d]+)*\s+[-\w’\d]+
Spacy sử dụng một số biểu thức chính quy (regex) để phát hiện các đối tượng trong văn bản. Dưới đây là danh sách các regex được sử dụng cho một số nhãn thực thể (entity labels) trong Spacy:
PERSON: regex cho tên người (person name):
[-\w’\d]+(?:\s+[-\w’\d]+)*
NORP (Nationalities or religious or political groups): regex cho tên quốc gia (country names):
[A-Z][a-z]+\s?(?:[A-Z][a-z]+)?
FAC (Buildings, airports, highways, bridges, etc.): regex cho tên địa điểm (location name):
[-\w’\d]+(?:\s+[-\w’\d]+)*
ORG (Companies, agencies, institutions, etc.): regex cho tên công ty (company name):
[-\w\d]+(?:\s+[-\w\d]+)*
GPE (Countries, cities, states): regex cho tên quốc gia (country name):
[A-Z][a-z]+\s?(?:[A-Z][a-z]+)*
LOC (Non-GPE locations, mountain ranges, bodies of water): regex cho tên địa danh (place name):
[-\w\d]+(?:\s+[-\w\d]+)*
PRODUCT (Objects, vehicles, foods, etc.): regex cho tên sản phẩm (product name):
[-\w\d]+(?:\s+[-\w\d]+)*
EVENT (Named hurricanes, battles, wars, sports events, etc.): regex cho tên sự kiện (event name):
[-\w\d]+(?:\s+[-\w\d]+)*
WORK_OF_ART (Titles of books, songs, etc.): regex cho tên tác phẩm nghệ thuật (artwork name):
[-\w\d]+(?:\s+[-\w\d]+)*
DATE (Absolute or relative dates or periods): regex cho các chuỗi ngày tháng (date string):
\d{4}-\d{2}-\d{2} hoặc \d{4}/\d{1,2}/\d{1,2}
TIME (Times, including dates with times): regex cho các chuỗi thời gian (time string):
(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d(?:\.\d+)?)?



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


