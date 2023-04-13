https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert



# Define a function to apply the augmenter to a DataFrame column
def back_trans_augment(text):
    return back_trans_aug.augment(text)

# Apply the augmenter to a DataFrame column
df['augmented_text'] = df['text_column'].apply(back_trans_augment)
