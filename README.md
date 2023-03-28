# Hàm xử lý chuỗi JSON
def remove_key(json_str, key_to_remove):
    # Chuyển đổi chuỗi JSON thành dictionary
    json_dict = json.loads(json_str)
    
    # Xóa cặp key-value
    del json_dict[key_to_remove]
    
    # Chuyển đổi dictionary thành chuỗi JSON
    return json.dumps(json_dict)

# Xóa cặp key-value "address" trong từng dòng của DataFrame
df['json_column'] = df['json_column'].apply(lambda x: remove_key(x, 'address'))

-----------------------

import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

df = pd.DataFrame({"text": ["John Smith is a software engineer at Google.", "Mary Johnson works at Microsoft."]})

def detect_person_names(text):
    doc = nlp(text)
    person_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return ", ".join(person_names)

df["person_names"] = df["text"].apply(detect_person_names)

print(df)



