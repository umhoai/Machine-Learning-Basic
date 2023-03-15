from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM
import spacy

# Load the pre-trained model and tokenizer
model_name = 'bert-base-cased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

# Load the Spacy NER model
nlp = spacy.load('en_core_web_sm')

# Define input text with named entities
input_text = "I live in New York and work at Google."

# Extract named entities using Spacy NER
doc = nlp(input_text)
entities = []
for ent in doc.ents:
    entities.append(ent.text)

# Mask named entities in input text
for entity in entities:
    masked_text = input_text.replace(entity, tokenizer.mask_token)

    # Get the top 5 predictions for the masked entity
    fill_mask = pipeline('fill-mask', model=model, tokenizer=tokenizer)
    results = fill_mask(masked_text, top_k=5)

    # Replace the masked entity with the first prediction
    new_text = masked_text.replace(tokenizer.mask_token, results[0]['token_str'])

    # Update input text with replaced entity
    input_text = new_text

print(input_text)
