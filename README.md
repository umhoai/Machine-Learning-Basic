# hàm tính số lần xuất hiện của mỗi từ trong từng dòng
def word_count(row):
    words = row['text'].lower().split()
    words = [word.strip('.,!?;') for word in words]
    return Counter(words)

# tạo một cột mới chứa bộ đếm từ cho mỗi dòng
df['word_count'] = df.apply(word_count, axis=1)

# tìm các từ hiếm và các từ xuất hiện nhiều nhất trong từng dòng
df['rare_words'] = df['word_count'].apply(lambda x: [word for word, count in x.items() if count < 5])
df['top_words'] = df['word_count'].apply(lambda x: [word for word, count in x.most_common(10)])

# in ra các từ hiếm và các từ xuất hiện nhiều nhất trong từng dòng
print(df[['text', 'rare_words', 'top_words']])
