import sys
sys.path.insert(0,'src')
from common import *
import google
from variables import *
import requests
import codecs
import translitcodec
import codecs
from bs4 import BeautifulSoup 
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from textblob.classifiers import NaiveBayesClassifier
import tempfile


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
google.gscrapper(keyword)


def get_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

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
for index in range(5):
	data = uri[index].replace('/', '_')
	data = data.replace('?', '_')
	data = data.replace('=', '_')
	data = data.translate(None, " ?.!/;:=")
	data2=data+".txt"
	nfw=open(data2, 'w')
	#print data2
	url = uri[index]
	nf = get_text(url)
	#nfw.write(nf.encode("utf-8") +"\n")
	nfw.write(nf)
	print data2
	op = open("data2.txt", 'a')
	op.write(str(data2) +"\n")



