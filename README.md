import torch
import torch.nn as nn
import torch.optim as optim
from transformers import BertTokenizer, BertModel
from torchtext.data.utils import get_tokenizer
from torchtext.legacy.data import Field, TabularDataset, BucketIterator

# Define device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define fields for the dataset
label_field = Field(sequential=False, use_vocab=True)
text_field = Field(tokenize=tokenizer.tokenize, use_vocab=False, batch_first=True, 
                   sequential=True, pad_token=tokenizer.pad_token_id, unk_token=tokenizer.unk_token_id)

# Load the dataset and split into train and test
train_data, test_data = TabularDataset.splits(
    path='data',
    train='train.csv',
    test='test.csv',
    format='csv',
    fields=[('text', text_field), ('label', label_field)]
)
train_data, valid_data = train_data.split(split_ratio=0.8, stratified=True)

# Build the vocabulary using the training data
label_field.build_vocab(train_data)

# Define batch size and iterator
batch_size = 16
train_iter, valid_iter, test_iter = BucketIterator.splits(
    (train_data, valid_data, test_data), batch_size=batch_size, device=device)

# Define the model
class TransformerModel(nn.Module):
    def __init__(self, num_labels):
        super(TransformerModel, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(0.1)
        self.fc = nn.Linear(self.bert.config.hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs[1]
        pooled_output = self.dropout(pooled_output)
        logits = self.fc(pooled_output)
        return logits

# Define the model parameters
num_labels = len(label_field.vocab)

# Instantiate the model
model = TransformerModel(num_labels).to(device)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=2e-5)

# Train the model
def train(model, iterator, optimizer, criterion):
    model.train()
    epoch_loss = 0
    for batch in iterator:
        input_ids = batch.text
        attention_mask = (input_ids != tokenizer.pad_token_id).type(torch.LongTensor)
        input_ids, attention_mask = input_ids.to(device), attention_mask.to(device)
        optimizer.zero_grad()
        logits = model(input_ids, attention_mask)
        loss = criterion(logits, batch.label)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    return epoch_loss / len(iterator)

# Evaluate the model
def evaluate(model, iterator, criterion):
    model.eval()
    epoch_loss = 0
    with torch.no_grad():
        for batch in iterator:
            input_ids = batch.text
            attention_mask = (input_ids != tokenizer.pad_token_id).type(torch.LongTensor)
            input_ids, attention_mask = input_ids.to(device), attention_mask.to(device)
            logits = model(input_ids, attention_mask)
            loss = criterion(logits, batch.label)
            epoch_loss += loss.item()
    return epoch_loss / len(iterator)

# Train and evaluate the model
num_epochs = 5
best_valid_loss = float
