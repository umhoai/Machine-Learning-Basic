import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder

# example log data
log_data_1 = "[2022-01-01 12:34:56] GET /api/v1/user/123 HTTP/1.1 200 OK"
log_data_2 = "[2022-01-01 12:35:02] POST /api/v1/user/123/friends HTTP/1.1 201 Created"
log_data_3 = "ERROR: file not found"
log_data_4 = "INFO: request processing completed"

# define functions for cleaning and processing log data
def clean_log_data(log_data):
    # remove timestamp and HTTP version
    log_data = re.sub(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]|\sHTTP/\d\.\d', '', log_data)

    # remove special characters
    log_data = re.sub(r'[^\w\s]', ' ', log_data)

    # tokenize the text
    tokens = word_tokenize(log_data)

    # remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]

    return filtered_tokens

def process_log_data(log_data):
    # clean log data
    cleaned_log_data = [clean_log_data(log) for log in log_data]

    # perform stemming
    stemmer = PorterStemmer()
    stemmed_log_data = [[stemmer.stem(token) for token in log] for log in cleaned_log_data]

    # identify bigrams
    bigram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_documents(stemmed_log_data)
    finder.apply_freq_filter(2)
    bigrams = [" ".join(bigram) for bigram in finder.nbest(bigram_measures.pmi, 10)]

    return cleaned_log_data, stemmed_log_data, bigrams

# process log data
log_data = [log_data_1, log_data_2, log_data_3, log_data_4]
cleaned_log_data, stemmed_log_data, frequent_bigrams = process_log_data(log_data)

# print results
print("Cleaned log data:")
for log in cleaned_log_data:
    print(" ".join(log))
print("Stemmed log data:")
for log in stemmed_log_data:
    print(" ".join(log))
print("Frequent bigrams:", frequent_bigrams)
