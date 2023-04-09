import csv
import random
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def synonym_replacement(word, p=0.5):
    """
    Randomly replace words with their synonyms.
    """
    if wordnet.synsets(word):
        if random.uniform(0, 1) < p:
            synonym = random.choice(wordnet.synsets(word)).lemmas()[0].name()
            return synonym.replace('_', ' ')
    return word

def random_swap(words, n=5):
    """
    Randomly swap two words in a sentence n times.
    """
    new_words = words.copy()
    for _ in range(n):
        idx1, idx2 = random.sample(range(len(new_words)), 2)
        new_words[idx1], new_words[idx2] = new_words[idx2], new_words[idx1]
    return new_words

def random_erase(words, p=0.1):
    """
    Randomly erase words in a sentence with probability p.
    """
    new_words = []
    for word in words:
        if random.uniform(0, 1) > p:
            new_words.append(word)
    return new_words

# Read the input CSV file
input_file = 'input.csv'
with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# Generate new data
new_data = []
for sentence, label in data:
    words = word_tokenize(sentence)
    new_words = [synonym_replacement(word) for word in words]
    new_words = random_swap(new_words)
    new_words = random_erase(new_words)
    new_sentence = ' '.join(new_words)
    new_data.append([new_sentence, label])

# Write the new data to a CSV file
output_file = 'output.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_data)
