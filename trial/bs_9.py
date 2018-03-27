import sys
import codecs
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from unidecode import unidecode

def end_word_extractor("/home/encompass/Desktop/trial/https__enwikipediaorg_wiki_Sathish.txt"):
...     tokens = document.split()
...     first_word, last_word = tokens[0], tokens[-1]
...     feats = {}
...     feats["first({0})".format(first_word)] = True
...     feats["last({0})".format(last_word)] = False
...     return feats
features = end_word_extractor("I feel happy")
assert features == {'last(happy)': False, 'first(I)': True}
cl2 = NaiveBayesClassifier(test, feature_extractor=end_word_extractor)
blob = TextBlob("I'm excited to try my new classifier.", classifier=cl2)
blob.classify()
