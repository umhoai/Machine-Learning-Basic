
Help me find pharmacies around here
Do I have Dental coverage? 
How much is paid by the plan after my deductible?
What is my Annual deductible?
What is my Maximum Out of Pocket Limit?
Does my plan covers Pap smear/mammogram?
What are the mental health services covered by the plan?
Is home health care supported?
What is the coverage for hearing aids?
Is Hospice service covered?
Will my plan covers Tobacco-cessation medicines? 

Find pharmacy
Coverage inquiry
Payment amount
Deductible inquiry
Maximum expense limit inquiry
Coverage query
Mental health coverage inquiry
Home health care query
Hearing aid coverage inquiry
Hospice coverage inquiry
Tobacco treatment coverage inquiry

import pandas as pd
import nlpaug.augmenter.word as naw
from nlpaug.util import Action

# Load the input data into a Pandas DataFrame
df = pd.read_excel('./data-collected/ic-question-assessment.xlsx')

df.info()
print(f'Rows: {df.shape[0]}, Cols: {df.shape[1]}')
df.head(11)

# Define a function to generate augmented data from input dataframe df, with default of 1 sentence generated per original sentence
def generate_augmented_data(df, num_sentences=1):
    num_sentences_swap_del = 1

    # Define the synonym replacement augmentation technique
    augmenter_synonym = naw.SynonymAug(aug_src='wordnet', aug_min=1, aug_max=1) # aug_min=1, aug_max=1

    # Apply the synonym replacement technique to the input data and save to dataset A, Create a new dataframe with columns 'sentence', 'class', and 'method'
    df_A = pd.DataFrame(columns=['sentence', 'class', 'method'])
    # Iterate through each row in the input dataframe
    for _, row in df.iterrows(): # _ : index of row
        # Apply the synonym replacement technique to the original sentence, and create a list of the original sentence plus num_sentences augmented sentences
        augmented_sentences = [row['sentence']] + [augmenter_synonym.augment(row['sentence']) for _ in range(num_sentences)]
        # Create a new dataframe with the augmented sentences and corresponding class and method values
        augmented_rows = pd.DataFrame({
            'sentence': augmented_sentences,
            'class': [row['class']] * len(augmented_sentences),
            'method': ['synonym'] + ['synonym'] * num_sentences
        })
        # Append the new dataframe to df_A
        df_A = df_A.append(augmented_rows)

    # Define the random position change augmentation technique
    augmenter_swap = naw.RandomWordAug(action=Action.SWAP, aug_min=1, aug_max=1)

    # Apply the random position change technique to the A dataset and save to dataset B, Create a new dataframe with columns 'sentence', 'class', and 'method'
    df_B = pd.DataFrame(columns=['sentence', 'class', 'method'])
    # Iterate through each row in df_A
    for _, row in df_A.iterrows():
        # Apply the random swap technique to the sentence, and create a list of the original sentence plus num_sentences augmented sentences
        augmented_sentences = [row['sentence']] + [augmenter_swap.augment(row['sentence']) for _ in range(num_sentences_swap_del)]
        # Create a new dataframe with the augmented sentences and corresponding class and method values
        augmented_rows = pd.DataFrame({
            'sentence': augmented_sentences,
            'class': [row['class']] * len(augmented_sentences),
            'method': [row['method']] + ['swap'] * num_sentences_swap_del
        })
        # Append the new dataframe to df_B
        df_B = df_B.append(augmented_rows)

    # Define the random deletion augmentation technique, Create a new dataframe with columns 'sentence', 'class', and 'method'
    augmenter_delete = naw.RandomWordAug(action=Action.DELETE, aug_p=0.3, aug_min=1, aug_max=2)

    # Apply the random deletion technique to the B dataset and save to the final output file
    df_augmented = pd.DataFrame(columns=['sentence', 'class', 'method'])
    # Iterate through each row in df_B
    for _, row in df_B.iterrows():
        # Apply the random deletion technique to the sentence, and create a list of the original sentence plus num_sentences augmented sentences
        augmented_sentences = [row['sentence']] + [augmenter_delete.augment(row['sentence']) for _ in range(num_sentences_swap_del)]
        # Create a new dataframe with the augmented sentences and corresponding class and method values
        augmented_rows = pd.DataFrame({
            'sentence': augmented_sentences,
            'class': [row['class']] * len(augmented_sentences),
            'method': [row['method']] + ['delete'] * num_sentences_swap_del
        })
        # Append the new dataframe to df_augmented
        df_augmented = df_augmented.append(augmented_rows)

    # Reset the index of the final output dataframe
    df_augmented.reset_index(drop=True, inplace=True)

    # Remove "[" and "]" characters from each output line
    df_augmented['sentence'] = df_augmented['sentence'].apply(lambda x: str(x).replace('[', '').replace("'", '').replace(']', ''))

    return df_augmented

data = generate_augmented_data(df, 2)

data.info()
print(f'Rows: {data.shape[0]}, Cols: {data.shape[1]}')
data.head(8)

data.duplicated().sum()

data.to_csv("./data-collected/augmented_data_v12_m3.csv", index=False)
