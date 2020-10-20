import create_corpus,preprocessing,train_word2vec

corpus = create_corpus.create()
corpus = preprocessing.clean(corpus)
train_word2vec.train("corpus.txt")
