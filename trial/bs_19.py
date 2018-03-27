import requests
import codecs
import translitcodec
import codecs
from bs4 import BeautifulSoup 


def get_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    # delete unwanted tags:
    for s in soup(['figure', 'script', 'style', 'table']):
        s.decompose()

    article_soup = [s.get_text(separator="\n", strip=True) for s in soup.find_all( ['p', {'class':'mol-para-with-font'}])]    
    article = '\n'.join(article_soup)

    text = codecs.encode(article, 'translit/one').encode('utf-8', 'replace') #replace traslit with ascii
    text = u"{}".format(text) #encode to unicode
    return text
    #print text

#url = 'http://www.dailymail.co.uk/femail/article-4703718/How-Alexander-McQueen-Kate-s-royal-tours.html'
#url = "https://www.yahoo.com"
url = "http://vget.org/"
nf = get_text(url)
print nf
#content = nf.read()
#with open("Output.txt", "wb") as text_file:
#file=open('output.txt', 'w')
	#text_file.write(str(get_text(url))+"\n")
       #	text_file.close()
#ghtmlo.write(nf.encode("utf-8") +"\n")
