from base64 import encode

from gensim.models import KeyedVectors, Word2Vec
from gensim.models import KeyedVectors
word_vectors = KeyedVectors.load_word2vec_format('model', binary=True)
print(word_vectors.most_similar('sahip'))