import spacy

nlp = spacy.load("en_core_web_sm")

# Define the text to process
text = "Steve Jobs was the CEO of Apple."

# Process the text with Spacy
doc = nlp(text)

# Loop through each named entity in the document
for entity in doc.ents:
    # Replace the entity with a generic label
    text = text.replace(entity.text, entity.label_)

# Print the updated text
print(text)
