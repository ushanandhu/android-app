import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.insert(0,'src')
from common import *
import google
from variables import *
import requests
import twitter
import codecs
#import translitcodec
import codecs
import tweepy
#import re
#from tweepy import OAuthHandler
from bs4 import BeautifulSoup 
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from textblob.classifiers import NaiveBayesClassifier

global txt_1


keyword = input_keyword()
def create_queries(keyword,stype="normal"):
	while True:
		if not keyword:
			print "keyword cannot be blank"
			keyword = input_keyword()
		elif "." in keyword:
			sys.stdout.write( "Please enter the keyword without specifying .com,.or,etc..")
			raw_input () 
			keyword = input_keyword()

		else:
			
			break
create_queries(keyword)

twitter.main(keyword)
google.gscrapper(keyword)





def get_text(url):
    r = requests.get(url,verify=False)
    soup = BeautifulSoup(r.content, "html.parser")

    # delete unwanted tags:
    for s in soup(['figure', 'script', 'style', 'table']):
        s.decompose()

    article_soup = [s.get_text(separator="\n", strip=True) for s in soup.find_all( ['p', {'class':'mol-para-with-font'}])]    
    article = '\n'.join(article_soup)

    text = codecs.encode(article, 'translit/one').encode('ascii', 'replace') #replace traslit with ascii
    text = u"{}".format(text) #encode to unicode
    return text
    #print text





#print "print uri value",uri[68]
#print uri
for index in range(10):
	data = uri[index].replace('/', '_')
	data = data.replace('?', '_')
	data = data.replace('=', '_')
	#data = data.translate(None," ?.!/;:=")
	data2=data+".txt"
	nfw=open(data2, 'w')
 	#print data2;
	url = uri[index]
	nf = get_text(url)
	
	txt_1.append(nf)
	#nfw.write(nf.encode("utf-8") +"\n")
	nfw.write(nf)

print "first file",txt_1[0]

for index in range(10):
	
	blob = TextBlob(txt_1[index])
	r=blob.sentiment.polarity
	print r
	for item in blob.sentences:
		
		if item.sentiment.polarity > 0:
                	
			r2=blob.sentiment.polarity
			print item.replace('\n', ' ')
			print 'positive'
			print r2
			#print("Accuracy: {0}".format(cl.accuracy(item)))
	
		elif item.sentiment.polarity < 0:
                	r2=blob.sentiment.polarity
			print item.replace('\n', ' ')
			print 'Negative'
			print r2


