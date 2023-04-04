# Xóa các từ lặp lại liền kề nhau
        item = re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', item)
