PUNCT_TO_REMOVE = '!"%&\'()*:;<=>?[\\]^_`{}~'

def process_punctuation(text):
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))
