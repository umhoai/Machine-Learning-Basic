from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import TensorDataset

# Assume your data is stored in a pandas DataFrame called `data` with columns "text" and "label"

# Split the data into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Convert the training data into PyTorch tensors
train_encodings = tokenizer(list(train_data["text"].values), truncation=True, padding=True)
train_labels = train_data["label"].values
train_labels_int = [label2id[label] for label in train_labels]  # map labels to integers
train_dataset = TensorDataset(
    torch.tensor(train_encodings['input_ids']),
    torch.tensor(train_encodings['attention_mask']),
    torch.tensor(train_labels_int, dtype=torch.long)  # convert to tensor with supported dtype
)

# Convert the test data into PyTorch tensors
test_encodings = tokenizer(list(test_data["text"].values), truncation=True, padding=True)
test_labels = test_data["label"].values
test_labels_int = [label2id[label] for label in test_labels]  # map labels to integers
test_dataset = TensorDataset(
    torch.tensor(test_encodings['input_ids']),
    torch.tensor(test_encodings['attention_mask']),
    torch.tensor(test_labels_int, dtype=torch.long)  # convert to tensor with supported dtype
)
