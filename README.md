# Convert string labels to integers
label_map = {label: i for i, label in enumerate(set(labels))}
labels_int = [label_map[label] for label in labels]

# Make sure input tensors and labels have the same number of samples
if len(encoded_data['input_ids']) != len(labels_int):
    raise ValueError('Number of input samples and labels do not match')
