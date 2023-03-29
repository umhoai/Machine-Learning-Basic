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
from transformers import AutoTokenizer
import json

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def extract_natural_language_words(json_string):
    # Parse the JSON string to a dictionary
    data = json.loads(json_string)

    # Extract the sentence from the data dictionary
    sentence = data['text']

    # Tokenize the sentence
    tokenized_text = tokenizer(sentence, return_tensors='pt').input_ids[0]

    # Convert the tokenized text to a list of words
    word_list = tokenizer.convert_ids_to_tokens(tokenized_text)

    # Filter out non-natural language words
    natural_language_words = [word for word in word_list if tokenizer.convert_tokens_to_string(word).isalpha()]

    # Convert the natural language words back to text
    natural_language_text = ' '.join(natural_language_words)

    return natural_language_text

# Apply the function to the "sentence" column of the DataFrame
df['natural_language_sentence'] = df['sentence'].apply(extract_natural_language_words)

print(df)

