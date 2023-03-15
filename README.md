def process_number_phone(text):
    regex_number_phone = [
        r'\+\d{2} \d{3} \d{3} \d{4}',
        r'\(\d{3}\)\d{3}-\d{4}',
        r'\(\d{3}\)-\d{3}-\d{4}',
        r'\d{3}-\d{3}-\d{4}',
        r'[\d\+\s\(\)]{10,}'
    ]
    for num_phone in regex_number_phone:
        text=re.sub(num_phone, ' @numberphone ', text)
    return text
