from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
file=open("/home/encompass/Desktop/trial/https__enwikipediaorg_wiki_Sathish.txt");
t=file.read();

a=TextBlob(t)
r=a.sentiment.polarity
print r

