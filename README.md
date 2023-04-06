import json
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords
from gensim.models import Word2Vec

# Đọc dữ liệu log từ file JSON vào một danh sách các câu
with open('log.json', 'r') as f:
    logs = [json.loads(line)['message'] for line in f]

# Tách câu thành các từ và loại bỏ các từ không cần thiết
CUSTOM_FILTERS = [lambda x: x.lower(), remove_stopwords, lambda x: x.isalpha(), lambda x: len(x) > 1]
processed_logs = [preprocess_string(log, CUSTOM_FILTERS) for log in logs]

# Huấn luyện mô hình word2vec trên dữ liệu log đã được tiền xử lý
model = Word2Vec(processed_logs, min_count=5, size=100)

# Trích xuất các từ quan trọng từ mô hình word2vec
important_words = model.wv.index2entity[:3]
print(important_words)
