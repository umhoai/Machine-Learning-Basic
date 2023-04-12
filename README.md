https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert
 traning model chưa tăng cường dữ liệu

import pandas as pd

# Define the desired number of samples in each label category
n_samples = 2

# Group the dataframe by the label column
grouped = df.groupby('label')

# Create an empty dataframe to store the balanced data
balanced_df = pd.DataFrame()

# Iterate over each label category
for label, group in grouped:
    # Shuffle the samples in the current label category
    shuffled = group.sample(frac=1)
    
    # Take the desired number of samples
    subset = shuffled[:n_samples]
    
    # Concatenate the subset with the balanced dataframe
    balanced_df = pd.concat([balanced_df, subset])
    
# Shuffle the entire balanced dataframe
balanced_df = balanced_df.sample(frac=1).reset_index(drop=True)

print(balanced_df)

