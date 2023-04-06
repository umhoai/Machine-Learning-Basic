import pandas as pd
from collections import Counter

def find_rare_and_important_words(df, rare_threshold=0.01, important_threshold=0.05):
    # Combine all text data into a single string
    text = " ".join(df[df.columns[0]].astype(str))
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the total number of words
    num_words = len(words)
    
    # Determine the threshold for rare words
    rare_count_threshold = int(num_words * rare_threshold)
    
    # Find the rare words
    rare_words = [word for word, count in word_counts.items() if count < rare_count_threshold]
    
    # Determine the threshold for important words
    important_count_threshold = int(num_words * important_threshold)
    
    # Find the important words
    important_words = [word for word, count in word_counts.items() if count > important_count_threshold]
    
    # Return the rare and important words
    return rare_words, important_words
