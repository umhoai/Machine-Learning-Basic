# hàm tính số lần xuất hiện của mỗi từ trong toàn bộ tập dữ liệu
def word_count(data):
    words = data.str.lower().str.split()
    words = words.explode().str.strip('.,!?;')
    return Counter(words)

# tạo bộ đếm từ cho toàn bộ tập dữ liệu
word_counts = word_count(df['text'])

# tìm các từ hiếm và các từ xuất hiện nhiều nhất trong toàn bộ tập dữ liệu
rare_words = [word for word, count in word_counts.items() if count < 2]
top_words = [word for word, count in word_counts.most_common(3)]

# in ra các từ hiếm và các từ xuất hiện nhiều nhất trong toàn bộ tập dữ liệu
print('Rare words:', rare_words)
print('Top words:', top_words)
