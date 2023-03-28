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
def remove_person_names(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            text = text.replace(ent.text, "")
    return text

df["text"] = df["text"].apply(remove_person_names)


