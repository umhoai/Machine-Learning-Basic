import re
import wordninja

def split_words(text, split_words_list):
    # Tìm kiếm các từ dính liền trong danh sách từ cần tách
    pattern = r'(' + '|'.join([re.escape(x) for x in split_words_list]) + r')'
    
    # Tách câu thành các từ bằng wordninja và lưu vào danh sách
    words = wordninja.split(text)
    
    # Tạo danh sách kết quả rỗng
    result = []
    
    # Duyệt qua từng từ
    for word in words:
        # Kiểm tra xem từ có phải từ dính liền không
        if re.match(pattern, word):
            # Nếu đúng, tách từ và thêm vào danh sách kết quả
            subwords = wordninja.split(word.replace("_", " "))
            result.extend(subwords)
        else:
            # Nếu không, giữ nguyên từ và thêm vào danh sách kết quả
            result.append(word)
    
    # Trả về chuỗi kết quả
    return " ".join(result)
