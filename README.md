import re
import wordninja

def split_words(text, word_list):
    # Thay thế các từ liên kết trong list bằng dấu gạch dưới
    for word in word_list:
        text = re.sub(word, word.replace(" ", "_"), text)
    
    # Tách các từ bằng wordninja
    words = wordninja.split(text)
    
    # Thay thế các dấu gạch dưới bằng khoảng trắng và kết hợp thành chuỗi
    result = " ".join([word.replace("_", " ") for word in words])
    
    return result
