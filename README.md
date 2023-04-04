def split_words(s, split_list):
    # Tách các từ bằng wordninja
    words = wordninja.split(s)
    # Tách các từ dính liền được chỉ định trong split_list
    for split_word in split_list:
        new_words = []
        for word in words:
            if split_word in word:
                split_parts = word.split(split_word)
                for i, part in enumerate(split_parts):
                    new_words.append(part)
                    if i < len(split_parts)-1:
                        new_words.append(split_word)
            else:
                new_words.append(word)
        words = new_words
    return words


def process_text(row, split_list):
    text = row['text']
    processed_text = ' '.join(split_words(text, split_list))
    return processed_text
    
    # Chỉ định danh sách từ dính liền cần tách
split_list = ['attached']

# Áp dụng hàm process_text cho từng dòng trong dataframe
df['processed_text'] = df.apply(process_text, args=(split_list,), axis=1)


text = "This is a wordsattached example with wordlist and some other wordsattached"
split_list = ["attached"]
processed_text = ' '.join(split_words(text, split_list))
print(processed_text)
