# Import the required libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Load the data and preprocess it
# ...

# Convert the text data into a numerical format
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(data)

# Train the Random Forest model
rf = RandomForestClassifier()
rf.fit(X, y)

# Extract feature importances
importances = rf.feature_importances_

# Rank the most useful words
feature_names = vectorizer.get_feature_names()
most_useful_words = sorted(zip(importances, feature_names), reverse=True)[:10]

print("Most useful words:")
for importance, word in most_useful_words:
    print(f"{word}: {importance}")
