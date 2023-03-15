from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Chuỗi văn bản cần tạo các masked tokens
text = "I have a cat named Fluffy. She is very cute."

# Chuyển đổi chuỗi văn bản thành mã thông báo (tokenized text)
tokens = tokenizer.encode(text, add_special_tokens=True)

# Tạo masked tokens từ mã thông báo
masked_tokens = tokenizer.mask_tokens(tokens, 0.15, tokenizer.mask_token_id)

# Chuyển đổi masked tokens thành chuỗi văn bản
masked_text = tokenizer.decode(masked_tokens[0], skip_special_tokens=True)

print("Original text: ", text)
print("Masked text: ", masked_text)
