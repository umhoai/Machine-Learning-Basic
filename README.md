https://jaketae.github.io/study/keyword-extraction/

https://www.kaggle.com/code/ianalyticsgeek/keywords-extraction-using-bert



import nlpaug.augmenter.word as naw

text = 'The quick brown fox jumped over the lazy dog'
back_translation_aug = naw.BackTranslationAug(
    from_model_name='Helsinki-NLP/opus-mt-en-de',
    to_model_name='Helsinki-NLP/opus-mt-de-en'
    )
back_translation_aug.augment(text)



import nlpaug.augmenter.word as naw

text = 'The quick brown fox jumped over the lazy dog'
back_translation_aug = naw.BackTranslationAug(
    from_model_name='facebook/wmt19-en-de', 
    to_model_name='facebook/wmt19-de-en'
)
back_translation_aug.augment(text)


import os
os.environ["MODEL_DIR"] = '../model'

# Load models from local path
import nlpaug.augmenter.word as naw

from_model_dir = os.path.join(os.environ["MODEL_DIR"], 'word', 'fairseq', 'wmt19.en-de')
to_model_dir = os.path.join(os.environ["MODEL_DIR"], 'word', 'fairseq', 'wmt19.de-en')

text = 'The quick brown fox jumped over the lazy dog'
back_translation_aug = naw.BackTranslationAug(
    from_model_name=from_model_dir, from_model_checkpt='model1.pt',
    to_model_name=to_model_dir, to_model_checkpt='model1.pt', 
    is_load_from_github=False)
back_translation_aug.augment(text)
