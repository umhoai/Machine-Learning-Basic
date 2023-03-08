import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')

# Định nghĩa hàm loại bỏ stopword từ một chuỗi
def remove_stopwords(text):
    words = text.split()
    return " ".join([word for word in words if word.lower() not in stop_words])

# Áp dụng hàm remove_stopwords vào một cột của DataFrame
df['text_column'] = df['text_column'].apply(remove_stopwords)
