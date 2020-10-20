import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def train(file):
    model = Word2Vec(LineSentence(file), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.wv.save_word2vec_format("model", binary=True)