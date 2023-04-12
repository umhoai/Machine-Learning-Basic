https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert



import pandas as pd
import numpy as np

df = pd.DataFrame({
    'label': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
              'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
              'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
    'feature': range(30)
})

# Calculate the size of each label category
label_sizes = df.groupby('label').size()

# Calculate the maximum label size
max_label_size = label_sizes.max()

# Calculate the target sample size for each label category
target_sizes = label_sizes.apply(lambda x: min(x, max_label_size))

# Calculate the number of samples to take from each label category
n_samples = target_sizes.values

# Group the dataframe by the label column
grouped = df.groupby('label')

# Create an empty dataframe to store the balanced data
balanced_df = pd.DataFrame()

# Iterate over each label category
for label, group in grouped:
    # Shuffle the samples in the current label category
    shuffled = group.sample(frac=1)
    
    # Take the desired number of samples
    subset = shuffled[:n_samples[label]]
    
    # Concatenate the subset with the balanced dataframe
    balanced_df = pd.concat([balanced_df, subset])
    
# Shuffle the entire balanced dataframe
balanced_df = balanced_df.sample(frac=1).reset_index(drop=True)

print(balanced_df)
