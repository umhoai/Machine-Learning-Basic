https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert



import nlpaug.augmenter.word as naw

text = 'The quick brown fox jumped over the lazy dog'
back_translation_aug = naw.BackTranslationAug(
    from_model_name='Helsinki-NLP/opus-mt-en-de',
    to_model_name='Helsinki-NLP/opus-mt-de-en'
    )
back_translation_aug.augment(text)
