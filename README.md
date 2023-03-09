from sklearn.model_selection import train_test_split

# X and y represent your dataset
# y is the target variable

# Split the data into train and test sets, ensuring balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Count the number of data points in each class in the train set
train_class_counts = dict(zip(*np.unique(y_train, return_counts=True)))

# Determine the minimum number of data points in any class
min_class_count = min(train_class_counts.values())

# Randomly select data points from each class in the train set, up to the minimum count
train_indices = []
for k, v in train_class_counts.items():
    indices = np.where(y_train == k)[0]
    np.random.shuffle(indices)
    train_indices.extend(indices[:min_class_count])

# Use the selected indices to create the final train split
X_train_final = X_train[train_indices]
y_train_final = y_train[train_indices]
