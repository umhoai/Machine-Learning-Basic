import torch
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
import pandas as pd

# Define the dataset
df = pd.read_csv('dataset.csv')
labels = df['label'].values
texts = df['text'].values

# Split the dataset into train and test sets
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2)

# Load the pre-trained GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-j-6B')

# Tokenize the text data
train_encodings = tokenizer(train_texts, truncation=True, padding=True)
test_encodings = tokenizer(test_texts, truncation=True, padding=True)

# Convert the data into PyTorch tensors
train_dataset = torch.utils.data.TensorDataset(
    torch.tensor(train_encodings['input_ids']),
    torch.tensor(train_encodings['attention_mask']),
    torch.tensor(train_labels)
)
test_dataset = torch.utils.data.TensorDataset(
    torch.tensor(test_encodings['input_ids']),
    torch.tensor(test_encodings['attention_mask']),
    torch.tensor(test_labels)
)

# Load the pre-trained GPT-2 model
model = GPT2ForSequenceClassification.from_pretrained('EleutherAI/gpt-j-6B')

# Fine-tune the model on the training dataset
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
optimizer = AdamW(model.parameters(), lr=1e-5)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=8, shuffle=True)
for epoch in range(5):
    for batch in train_loader:
        input_ids = batch[0].to(device)
        attention_mask = batch[1].to(device)
        labels = batch[2].to(device)
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

# Evaluate the performance of the model on the test dataset
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=8, shuffle=False)
model.eval()
with torch.no_grad():
    num_correct = 0
    num_total = 0
    for batch in test_loader:
        input_ids = batch[0].to(device)
        attention_mask = batch[1].to(device)
        labels = batch[2].to(device)
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_labels = torch.argmax(logits, dim=1)
        num_correct += (predicted_labels == labels).sum().item()
        num_total += len(labels)
accuracy = num_correct / num_total
print('Accuracy:', accuracy)
