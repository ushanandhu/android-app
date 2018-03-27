from textblob import TextBlob
from nltk.tokenize import word_tokenize
from textblob.classifiers import NaiveBayesClassifier
#with open('/home/user/Desktop/ghtml.txt', 'r','utf-8') as fp:
blob = TextBlob(open("/home/encompass/Desktop/trial/https__enwikipediaorg_wiki_Sathish.txt").read())
for item in blob.sentences:
	if item.sentiment.polarity > 0:
                print 'positive'
		print item.replace('\n', ' ')
		#print("Accuracy: {0}".format(cl.accuracy(item)))
for item in blob.sentences:
	if item.sentiment.polarity < 0:
                print 'negative'
		print item.replace('\n', ' ')


    
