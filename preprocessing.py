import re
import unicodedata
from os.path import join
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM
from unidecode import unidecode

with open('data/stopwords-tr.txt') as f:
    stop_words = f.read().splitlines()

def clean(corpus):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    for i, line in enumerate(corpus):  # removes whitespaces, emojis, punctuations and stopwords
        if isinstance(line, str):
            line = emoji_pattern.sub(r'', line)

            word_tokens = line.split()

            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            line = ' '.join(filtered_sentence)
            line = unidecode(line)
            word_tokens = line.split()
            word_tokens = [word.lower() for word in word_tokens if (word.isalpha() and word.isalnum())]

            line = ' '.join(word_tokens)

            line = ' '.join(line.split())
            corpus[i] = line.replace('\u0307','').replace('\u016b','').replace('\u0137','').replace('\u013a','')

    with open('corpus.txt', 'w') as f:
        for item in corpus:
            if isinstance(item,str) and len(item)>5:
                f.write("%s\n" % item)
    return corpus
