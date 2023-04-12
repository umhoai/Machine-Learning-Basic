https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert
 traning model chưa tăng cường dữ liệu

import pandas as pd
import nlpaug.augmenter.word as naw
from nlpaug.util import Action


def generate_augmented_data(df, num_sentences=1):
    num_sentences_swap_del = 1

    # Define the augmentation techniques
    augmenter_synonym = naw.SynonymAug(aug_src='wordnet', aug_min=1, aug_max=3)
    augmenter_swap = naw.RandomWordAug(action=Action.SWAP, aug_min=1, aug_max=1)
    augmenter_delete = naw.RandomWordAug(action=Action.DELETE, aug_p=0.3, aug_min=1, aug_max=2)

    # Create a new dataframe with columns 'sentence', 'class', and 'method'
    df_augmented = pd.DataFrame(columns=['sentence', 'class', 'method'])

    # Iterate through each row in the input dataframe
    for _, row in df.iterrows():
        # Apply the synonym replacement technique to the original sentence, and create a list of the original sentence plus num_sentences augmented sentences
        augmented_sentences = [row['sentence']] + [augmenter_synonym.augment(row['sentence']) for _ in range(num_sentences)]

        # Apply the random position change technique to the augmented sentences and create a list of the augmented sentences plus num_sentences_swap_del augmented sentences
        augmented_sentences = augmented_sentences + [augmenter_swap.augment(sentence) for sentence in augmented_sentences for _ in range(num_sentences_swap_del)]

        # Apply the random deletion technique to the augmented sentences and create a list of the augmented sentences plus num_sentences_swap_del augmented sentences
        augmented_sentences = augmented_sentences + [augmenter_delete.augment(sentence) for sentence in augmented_sentences for _ in range(num_sentences_swap_del)]

        # Create a new dataframe with the augmented sentences and corresponding class and method values
        augmented_rows = pd.DataFrame({
            'sentence': augmented_sentences,
            'class': [row['class']] * len(augmented_sentences),
            'method': ['synonym'] * (num_sentences + 1) + ['swap'] * ((num_sentences + 1) * num_sentences_swap_del) + ['delete'] * ((num_sentences + 1) * num_sentences_swap_del)
        })

        # Append the new dataframe to df_augmented
        df_augmented = df_augmented.append(augmented_rows)

    # Reset the index of the final output dataframe
    df_augmented.reset_index(drop=True, inplace=True)

    # Remove "[" and "]" characters from each output line
    df_augmented['sentence'] = df_augmented['sentence'].apply(lambda x: str(x).replace('[', '').replace("'", '').replace('"', '').replace(']', ''))

    return df_augmented

