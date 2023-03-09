from sklearn.model_selection import StratifiedShuffleSplit

# X and y represent your dataset
# y is the target variable

# Define the number of folds for the cross-validation
num_folds = 1

# Define the percentage of data to be used for training
train_size = 0.6

# Initialize empty arrays for the train and validation data
X_train, y_train = None, None

# Define the cross-validation strategy to generate the train and validation splits
cv = StratifiedShuffleSplit(n_splits=num_folds, train_size=train_size, random_state=42)

# Loop over the folds and select the train and validation splits
for train_index, val_index in cv.split(X, y):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]

# Check the number of samples in each class in the train set
unique_labels, counts_train = np.unique(y_train, return_counts=True)
print(f"Train set class counts: {dict(zip(unique_labels, counts_train))}")

# Check the number of samples in each class in the validation set
unique_labels, counts_val = np.unique(y_val, return_counts=True)
print(f"Validation set class counts: {dict(zip(unique_labels, counts_val))}")
