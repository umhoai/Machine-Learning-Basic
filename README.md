import pandas as pd

# Tạo DataFrame ví dụ
data = {'Câu': ['Đây là câu đầu tiên', 'Đây là câu thứ hai', 'Câu số 3', 'Câu số 4']}
df = pd.DataFrame(data)

# Thiết lập ngưỡng độ dài câu
min_length = 10

# Sử dụng hàm apply() kết hợp với hàm lambda để tách từ và đếm số lượng từ
df = df[df['Câu'].apply(lambda x: len(x.split()) >= min_length)]
