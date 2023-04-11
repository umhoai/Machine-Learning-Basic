https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert


def generate_data_augmentation(df, num_sentences=1, aug_p=0.3, aug_min = 1, aug_max = 2):
    df1 = generate_synonym(df, num_sentences)
    df1.to_csv("./data-collected/generate_synonym.csv", index=False)
    df2 = generate_swap(df1, num_sentences)
    df2.to_csv("./data-collected/generate_swap.csv", index=False)
    df3 = generate_deletion(df2, num_sentences)
    df3.to_csv("./data-collected/generate_deletion.csv", index=False)
    df4 = generate_insert(df2, num_sentences)
    df4.to_csv("./data-collected/generate_deletion.csv", index=False)
    df_result = pd.concat([df3, df4])

