# Shuffle the training data and reset index
train_data = shuffle(train_data).reset_index(drop=True)

# Shuffle the testing data and reset index
test_data = shuffle(test_data).reset_index(drop=True)
