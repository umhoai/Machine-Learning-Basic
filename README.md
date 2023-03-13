def process_date(text):
    get_date_string = [r'\d{4}-\d{2}-\d{2}' ]

    for date in get_date_string:
        text=re.sub(date, ' @date ', text)

    return text
def process_dot_IELTS(text):
    text=re.sub(r'\b(\d[.]\d{1,1})', '@number', text) # lưu ý sau cái footer trước cái number
    return text
def process_hyphen(text):
    text=text.replace('-', ' @hyphen ')
    return text
