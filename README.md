def process_parser_error(text):
    if len(re.findall("\s", text)) > len(text)/3:
        text1 = re.sub("\s\s+", "_space_", text)
        text1 = re.sub(" ", "", text1)
        text1 = re.sub("_space_", " ", text1)
        text = text1
    return text
