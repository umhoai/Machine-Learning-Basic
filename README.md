[-\w’\d]+(?:\s+[-\w’\d]+)*\s+[-\w’\d]+
Spacy sử dụng một số biểu thức chính quy (regex) để phát hiện các đối tượng trong văn bản. Dưới đây là danh sách các regex được sử dụng cho một số nhãn thực thể (entity labels) trong Spacy:
PERSON: regex cho tên người (person name):
[-\w’\d]+(?:\s+[-\w’\d]+)*
NORP (Nationalities or religious or political groups): regex cho tên quốc gia (country names):
[A-Z][a-z]+\s?(?:[A-Z][a-z]+)?
FAC (Buildings, airports, highways, bridges, etc.): regex cho tên địa điểm (location name):
[-\w’\d]+(?:\s+[-\w’\d]+)*
ORG (Companies, agencies, institutions, etc.): regex cho tên công ty (company name):
[-\w\d]+(?:\s+[-\w\d]+)*
GPE (Countries, cities, states): regex cho tên quốc gia (country name):
[A-Z][a-z]+\s?(?:[A-Z][a-z]+)*
LOC (Non-GPE locations, mountain ranges, bodies of water): regex cho tên địa danh (place name):
[-\w\d]+(?:\s+[-\w\d]+)*
PRODUCT (Objects, vehicles, foods, etc.): regex cho tên sản phẩm (product name):
[-\w\d]+(?:\s+[-\w\d]+)*
EVENT (Named hurricanes, battles, wars, sports events, etc.): regex cho tên sự kiện (event name):
[-\w\d]+(?:\s+[-\w\d]+)*
WORK_OF_ART (Titles of books, songs, etc.): regex cho tên tác phẩm nghệ thuật (artwork name):
[-\w\d]+(?:\s+[-\w\d]+)*
DATE (Absolute or relative dates or periods): regex cho các chuỗi ngày tháng (date string):
\d{4}-\d{2}-\d{2} hoặc \d{4}/\d{1,2}/\d{1,2}
TIME (Times, including dates with times): regex cho các chuỗi thời gian (time string):
(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d(?:\.\d+)?)?
