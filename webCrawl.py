#importing module to crawl
import codecs
import nltk
import urllib2

from bs4 import BeautifulSoup

#soup = BeautifulSoup("https://mr.wikipedia.org/s/2cv")
#text = soup.getText()
#print(text)

f = urllib2.urlopen("https://mr.wikipedia.org/s/2cv")

soup = BeautifulSoup(f)
text = soup.getText()
print(text)

#print nltk.clean_html(f.read())


