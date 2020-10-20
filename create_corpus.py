import os,pickle
import pandas as pd
import preprocessing

def create():
  corpus = []
  for root,dirs,files in os.walk('data'):
      for file in files:
        if file.endswith(".csv"):
          data = pd.read_csv('data/'+file)
          for i in range(0,len(data)):
            corpus.append(data['text'][i])

  with open('corpus.pickle', 'wb') as f:
    pickle.dump(corpus, f)

  return corpus
