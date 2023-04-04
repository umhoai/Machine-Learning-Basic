import re
import wordninja

def split_words(text, word_list):
    # Tách các từ bằng wordninja
    words = wordninja.split(text)
    
    # Tạo một danh sách rỗng để lưu trữ kết quả
    result = []
    
    # Duyệt qua từng từ trong danh sách đã tách
    for word in words:
        # Kiểm tra xem từ có trong danh sách các từ cần tách không
        if word in word_list:
            # Nếu có, thay thế bằng từ được tách thành hai từ
            result.extend(wordninja.split(word.replace("_", " ")))
        else:
            # Nếu không, giữ nguyên từ
            result.append(word)
    
    # Kết hợp các từ lại thành chuỗi và trả về
    return " ".join(result)
 
