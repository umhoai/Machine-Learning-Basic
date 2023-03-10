from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Read in the CSV file
data = pd.read_csv('data.csv')

# Get the unique labels in the dataset
labels = np.unique(data['label'])

# Separate data into subsets by label
label_data = {}
for label in labels:
    label_data[label] = data[data['label'] == label]

# Split each label subset into training and testing sets with equal sample sizes
train_data = []
test_data = []
for label in labels:
    label_train, label_test = train_test_split(label_data[label], train_size=0.8, test_size=0.2, random_state=42)
    train_data.append(label_train)
    test_data.append(label_test)

# Combine the training and testing sets for all labels
train_data = pd.concat(train_data, axis=0)
test_data = pd.concat(test_data, axis=0)
