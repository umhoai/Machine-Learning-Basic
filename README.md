import pandas as pd

def find_rare_and_important_words(df, rare_threshold=0.001, important_threshold=0.1):
    # Combine all text data into a single Series
    all_text = pd.Series(df.values.ravel()).str.lower()
    
    # Calculate word frequencies
    word_counts = all_text.str.split(expand=True).stack().value_counts(normalize=True)
    
    # Find rare words
    rare_words = word_counts[word_counts < rare_threshold].index.tolist()
    
    # Find important words
    important_words = word_counts[word_counts > important_threshold].index.tolist()
    
    return rare_words, important_words
