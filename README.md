def process_one_char(string):
    return " ".join([token.text for token in nlp(string) if len(str(token))>1])

nlp = spacy.load('en_core_web_sm')

stop_words = set(stopwords.words('english'))

df['text'] = df['text'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))
print(df)
-----------------------
import random

def add_linking_words(sentence, conjunctions=["and"]):
    # Split the sentence into a list of phrases using the comma as the delimiter
    phrases = sentence.split(", ")

    # If there are fewer than two phrases, return the original sentence
    if len(phrases) < 2:
        return sentence

    # Add the conjunction between each pair of phrases
    linked_phrases = [phrases[0]]
    for phrase in phrases[1:]:
        conjunction = random.choice(conjunctions)
        linked_phrases.append(conjunction)
        linked_phrases.append(phrase)

    # Combine the linked phrases into a single string and return it
    linked_sentence = " ".join(linked_phrases)
    return linked_sentence
----------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataframe with preprocessed text data
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "text": [
        "Global warming is a major issue that needs to be addressed",
        "The melting of the polar ice caps is a clear sign of climate change",
        "Greenhouse gas emissions from human activity are causing climate change",
        "Rising sea levels are a threat to coastal communities",
        "Renewable energy sources such as solar and wind power can help mitigate climate change"
    ]
})

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text"])

# Extract the most important words
feature_names = tfidf_vectorizer.get_feature_names()
top_words = []
for i in range(len(df)):
    tfidf_scores = zip(feature_names, tfidf_matrix[i].toarray()[0])
    sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
    top_words.append([word for word, score in sorted_scores][:5])

# Add top words to the dataframe
df["top_words"] = top_words

# Print the dataframe
print(df)


---------------------------------------------------------------------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataframe with preprocessed text data
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "text": [
        "Global warming is a major issue that needs to be addressed",
        "The melting of the polar ice caps is a clear sign of climate change",
        "Greenhouse gas emissions from human activity are causing climate change",
        "Rising sea levels are a threat to coastal communities",
        "Renewable energy sources such as solar and wind power can help mitigate climate change"
    ]
})

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text"])

# Extract the most important words
feature_names = tfidf_vectorizer.get_feature_names()
top_words = []
for i in range(len(df)):
    tfidf_scores = zip(feature_names, tfidf_matrix[i].toarray()[0])
    sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
    top_words.append([word for word, score in sorted_scores][:5])

# Add top words to the dataframe
df["top_words"] = top_words

# Print the dataframe
print(df)



-------------------
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Read preprocessed text data from CSV file
df = pd.read_csv("preprocessed_data.csv")

# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text data
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text"])

# Get feature names
feature_names = tfidf_vectorizer.get_feature_names()

# Define query
query = "important topic"

# Transform query using the vectorizer
query_tfidf = tfidf_vectorizer.transform([query])

# Extract the most important words for the query
tfidf_scores = zip(feature_names, query_tfidf.toarray()[0])
sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)
top_words = [word for word, score in sorted_scores][:5]

# Print the most important words for the query
print("Top words for query '{}'".format(query))
print(", ".join(top_words))

--------------------------------------
def parse_events(events):
    # Initialize an empty list to store the individual event strings
    event_strings = []

    # Iterate over each event in the input list and parse it into a string
    for event in events:
        if event.startswith("user click button"):
            # Extract the button name from the event string
            button_name = event.split(": ")[1]
            event_string = f"The user clicked the \"{button_name}\" button"
        elif event.startswith("user view page"):
            # Extract the page name from the event string
            page_name = event.split(": ")[1]
            event_string = f"The user viewed the \"{page_name}\" page"
        elif event.startswith("user click link"):
            # Extract the link name from the event string
            link_name = event.split(": ")[1]
            # Extract the link location (e.g. order or account) from the event string
            link_location = event.split(": ")[0].split(" ")[-1]
            event_string = f"The user clicked the \"{link_name}\" link in the \"{link_location}\" section"
        elif event.startswith("guest view page"):
            # Extract the page name from the event string
            page_name = event.split(": ")[1]
            event_string = f"A guest viewed the \"{page_name}\" page"
        else:
            # If the event string does not match any of the expected formats, skip it
            continue

        # Add the parsed event string to the list
        event_strings.append(event_string)

    # Combine the individual event strings into a single sentence
    sentence = ", and ".join(event_strings[:-1]) + ", while " + event_strings[-1] if len(event_strings) > 1 else event_strings[0]

    # Add a period to the end of the sentence
    sentence += "."

    return sentence

