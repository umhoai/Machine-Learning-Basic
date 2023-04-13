https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert



import pandas as pd
import nlpaug.augmenter.word as naw
from nlpaug.util import Action
import os
from tqdm import tqdm

def save_to_csv(df, filename):
    mode = 'a' if os.path.exists(filename) else 'w'
    header = not os.path.exists(filename)
    df.to_csv(filename, mode=mode, header=header, index=False)

def generate_augmented_data(df, num_sentences=1, save_original=True):

    # Define the augmentation techniques
    augmenter_synonym = naw.SynonymAug(aug_src='wordnet', aug_min=1, aug_max=3)
    augmenter_swap = naw.RandomWordAug(action=Action.SWAP, aug_min=1, aug_max=1)
    augmenter_delete = naw.RandomWordAug(action=Action.DELETE, aug_p=0.3, aug_min=1, aug_max=2)
    augmenter_insert = naw.ContextualWordEmbsAug(model_path='bert-base-uncased', action="insert")    
    # Create a new dataframe with columns 'sentence', 'class'
    df_augmented = pd.DataFrame(columns=['sentence', 'class'])

    # Iterate through each row in the input dataframe
    for _, row in tqdm(df.iterrows()):
        augmented_sentences = []
        augmented_sentences_branch1 = []
        augmented_sentences_branch2 = []
        # Apply the synonym replacement technique to the original sentence, and create a list of the original sentence plus num_sentences augmented sentences
        augmented_sentences += [augmenter_synonym.augment(row['sentence']) for _ in range(num_sentences)]
        if save_original:
            augmented_sentences = [row['sentence']] + augmented_sentences
        save_to_csv(pd.DataFrame({'sentence': augmented_sentences, 'class': [row['class']] * len(augmented_sentences)}), 'synonym_aug.csv')

        # Apply the random position change technique to the augmented sentences and create a list of the augmented sentences plus num_sentences_swap_del augmented sentences
        augmented_sentences = augmented_sentences + [augmenter_swap.augment(sentence) for sentence in augmented_sentences for _ in range(num_sentences)]
        save_to_csv(pd.DataFrame({'sentence': augmented_sentences, 'class': [row['class']] * len(augmented_sentences)}), 'swap_aug.csv')

        # Apply the random deletion technique to the augmented sentences and create a list of the augmented sentences plus num_sentences_swap_del augmented sentences
        augmented_sentences_branch1 = augmented_sentences + [augmenter_delete.augment(sentence) for sentence in augmented_sentences for _ in range(num_sentences)]
        save_to_csv(pd.DataFrame({'sentence': augmented_sentences_branch1, 'class': [row['class']] * len(augmented_sentences_branch1)}), 'delete_aug.csv')

        # Apply the random deletion technique to the augmented sentences and create a list of the augmented sentences plus num_sentences_swap_del augmented sentences
        augmented_sentences_branch2 = [augmenter_insert.augment(sentence) for sentence in augmented_sentences for _ in range(num_sentences)]
        save_to_csv(pd.DataFrame({'sentence': augmented_sentences_branch2, 'class': [row['class']] * len(augmented_sentences_branch2)}), 'insert_aug.csv')

        # Append the new dataframe to df_augmented
        augmented_rows_branch1 = pd.DataFrame({
            'sentence': augmented_sentences_branch1,
            'class': [row['class']] * len(augmented_sentences_branch1)
        })

        # Append the new dataframe to df_augmented
        augmented_rows_branch2 = pd.DataFrame({
            'sentence': augmented_sentences_branch2,
            'class': [row['class']] * len(augmented_sentences_branch2)
        })

        # Append the new dataframe to df_augmented
        df_augmented = df_augmented.append([augmented_rows_branch1, augmented_rows_branch2])

    # Reset the index of the final output dataframe
    df_augmented.reset_index(drop=True, inplace=True)

    # Remove "[" and "]" characters from each output line
    df_augmented['sentence'] = df_augmented['sentence'].apply(lambda x: str(x).replace('[', '').replace("'", '').replace('"', '').replace(']', ''))

    return df_augmented
