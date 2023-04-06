import json
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords
from gensim.models import Word2Vec

# Đoạn văn bản JSON
json_text = '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_year": 1951, "description": "The Catcher in the Rye is a novel by J.D. Salinger. It was first published in 1951.", "reviews": [{"username": "johnsmith", "rating": 4, "text": "I really enjoyed this book. The protagonist is a relatable character and the story is well-written."}, {"username": "janedoe", "rating": 2, "text": "I found this book to be boring and overrated."}]}'

# Phân tích cú pháp JSON và trích xuất nội dung văn bản từ thuộc tính "description"
json_dict = json.loads(json_text)
text = json_dict['description']

# Tiền xử lý dữ liệu bằng cách tách câu thành các từ và loại bỏ các từ không cần thiết
CUSTOM_FILTERS = [lambda x: x.lower(), remove_stopwords, lambda x: x.isalpha(), lambda x: len(x) > 1]
processed_text = preprocess_string(text, CUSTOM_FILTERS)

# Huấn luyện mô hình word2vec trên dữ liệu văn bản đã được tiền xử lý
model = Word2Vec([processed_text], min_count=1, size=100)

# Trích xuất các từ quan trọng từ mô hình word2vec
important_words = model.wv.index2entity[:3]
print(important_words)
