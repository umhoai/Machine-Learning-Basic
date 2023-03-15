from transformers import pipeline 

nlp = pipeline("text2text-generation", model="distilbert-base-cased")
input_text = "Jame Doe's phone number is 555-1234"
masked_text = nlp(input_text, max_length=512, num_return_sequences=1, do_sample=True, top_p=0.9, mask_token="[MASK]")[0]['generated_text']
print(masked_text)
