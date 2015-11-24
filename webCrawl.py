#importing module to crawl
import codecs
import nltk
import urllib2
import re
from bs4 import BeautifulSoup
import string
from bs4 import SoupStrainer

#soup = BeautifulSoup("https://mr.wikipedia.org/s/2cv")
#text = soup.getText()
#print(text)

#f = urllib2.urlopen("https://mr.wikipedia.org/")

with open("h.txt") as f:
    for line in f:
        htmlFile = urllib2.urlopen(line)

	soup = BeautifulSoup(htmlFile)


	text = soup.getText()

#removedSpaces = re.sub(r"\s+", " ", text)
#remove ascii characters
#_ascii_letters = re.compile(r'[a-zA-Z0-9]', flags=re.UNICODE)
#removedEnglish = _ascii_letters.sub("", removedSpaces)
#remove the punctuation marks like "?,!,/,\,(,)
#punctutationMarks = re.compile(r'[?|$|.|!|(|)|%|#|}|{|.|;|,]')
#clean = re.sub(r"['_,!\-\"\\\/}{?\()%$*;\[\]:><|=@#+]",'',removedEnglish).strip()

	regex = re.compile(ur"[^\u0900-\u097F.]+")
	clean = regex.sub("", text)

	with codecs.open('hindi.txt', 'a', encoding='utf-8') as out:  
	    	out.write(clean)
		out.close
	print(line)

f.close


#print(clean)

