# Transformer

import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.datasets import AG_NEWS
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer
from torchtext.legacy.data import Field, TabularDataset, BucketIterator

import time

Define device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

Define tokenizer
tokenizer = get_tokenizer('basic_english')

Define fields for the dataset
label_field = Field(sequential=False, use_vocab=True)
text_field = Field(tokenize=tokenizer, lower=True, include_lengths=True)

Load the dataset and split into train and test
train_data, test_data = AG_NEWS(root='.data', split=('train', 'test'))
train_data, valid_data = train_data.split(split_ratio=0.8)

Build the vocabulary using the training data
text_field.build_vocab(train_data, max_size=25000)
label_field.build_vocab(train_data)

Define batch size and iterator
batch_size = 64
train_iter, valid_iter, test_iter = BucketIterator.splits(
    (train_data, valid_data, test_data), batch_size=batch_size, device=device)

Define the model
class TransformerModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_class, num_heads, num_layers, dropout):
        super(TransformerModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=embed_dim, nhead=num_heads, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(embed_dim, num_class)

    def forward(self, text, text_lengths):
        embedded = self.embedding(text)
        embedded = embedded.permute(1,0,2)
        packed_output = nn.utils.rnn.pack_padded_sequence(embedded, text_lengths)
        encoded_output = self.transformer_encoder(packed_output)
        encoded_output, _ = nn.utils.rnn.pad_packed_sequence(encoded_output)
        pooled_output = nn.functional.avg_pool2d(encoded_output, (encoded_output.shape[0], 1)).squeeze(1)
        output = self.fc(pooled_output)
        return output

Define the model parameters
vocab_size = len(text_field.vocab)
embed_dim = 32
num_class = len(label_field.vocab)
num_heads = 2
num_layers = 2
dropout = 0.2

Instantiate the model
model = TransformerModel(vocab_size, embed_dim, num_class, num_heads, num_layers, dropout).to(device)

Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

Train the model
def train(model, iterator, optimizer, criterion):
    model.train()
    epoch_loss = 0
    for batch in iterator:
        text, text_lengths = batch.text
        optimizer.zero_grad()
        predictions = model(text, text_lengths).squeeze(1)
        loss = criterion(predictions, batch.label)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    return epoch_loss / len(iterator)

Evaluate the model
def evaluate(model, iterator, criterion):
    model.eval()
    epoch_loss = 0
    with torch.no_grad():
        for batch in iterator:
            text, text_lengths = batch.text
           
