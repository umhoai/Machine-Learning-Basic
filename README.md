# tách các từ và tính tần suất xuất hiện của chúng
all_words = [word for text in df['text'] for word in str(text).split()]
word_counts = Counter(all_words)

# tìm các từ hiếm ít xuất hiện và các từ xuất hiện thường xuyên nhất
rare_words = [word for word, count in word_counts.items() if count < 5]
common_words = [word for word, count in word_counts.most_common(100)]

print('Rare words:', rare_words)
print('Common words:', common_words)
