def format_sentence(text):
    lines = text.strip().split('\n')
    sentence = ""
    for line in lines:
        key, value = line.split(': ')
        sentence += f"{key} {value}, "
    sentence = sentence[:-2] + "."
    return sentence

text = parse_json(json_str)
sentence = format_sentence(text)
print(sentence)
