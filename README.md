def process_data(data):
    result = []
    for item in data:
        # Xóa các ký tự đặc biệt
        item = re.sub('[^A-Za-z0-9]+', '', item)
        # Xóa số
        item = re.sub('[0-9]+', '', item)
        # Xóa email
        item = re.sub('\S+@\S+', '', item)
        # Xóa khoảng trắng thừa
        item = item.strip()
        # Thay thế từ được chỉ định
        item = item.replace('some_word', 'replacement_word')
        result.append(item)
    return result
