# Hàm xử lý chuỗi JSON
def remove_key(json_str, key_to_remove):
    # Chuyển đổi chuỗi JSON thành dictionary
    json_dict = json.loads(json_str)
    
    # Xóa cặp key-value
    del json_dict[key_to_remove]
    
    # Chuyển đổi dictionary thành chuỗi JSON
    return json.dumps(json_dict)

# Xóa cặp key-value "address" trong từng dòng của DataFrame
df['json_column'] = df['json_column'].apply(lambda x: remove_key(x, 'address'))

-----------------------
def split_words(text, words_to_split):
    """
    A helper function that splits words in a text that are in the given list of words_to_split
    """
    for word in words_to_split:
        if word in text:
            split_words = wordninja.split(word)
            for split_word in split_words:
                text = text.replace(word, split_word)
    return text

# Example dataframe with a text column
df = pd.DataFrame({'text': ['Hello worldd', 'Iloveyou', 'Whatareyoudoing', 'helloworld']})

# List of words to split
words_to_split = ['world', 'love', 'doing', 'helloworld']

# Apply the split_words function to the text column
df['text'] = df['text'].apply(split_words, words_to_split=words_to_split)
