import gensim
from gensim import corpora, models

# Load corpus
documents = ["I love programming in Python",
             "Java is a popular programming language",
             "Data science is a rapidly growing field",
             "Machine learning is the future",
             "Python is the best language for machine learning"]

# Tokenize corpus
tokenized_documents = [doc.lower().split() for doc in documents]

# Create dictionary
dictionary = corpora.Dictionary(tokenized_documents)

# Create corpus
corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

# Create LSA model
lsa_model = models.LsiModel(corpus, num_topics=2, id2word=dictionary)

# Print top 5 important words for each topic
for i, topic in enumerate(lsa_model.show_topics()):
    print(f"Topic {i+1}:")
    print(", ".join([word[0] for word in lsa_model.show_topic(i, topn=5)]))
    print()
