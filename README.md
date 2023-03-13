def process_number(text):
    regex_number = r'[0-9]{2,}'
    return re.sub(regex_number, '@number', text)
