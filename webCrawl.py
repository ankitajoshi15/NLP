#importing module to crawl
import codecs
import nltk
import urllib2
import re
from bs4 import BeautifulSoup

#soup = BeautifulSoup("https://mr.wikipedia.org/s/2cv")
#text = soup.getText()
#print(text)

f = urllib2.urlopen("https://mr.wikipedia.org/s/2cv")

soup = BeautifulSoup(f)
text = soup.getText()
#text = re.sub(r"\s+", "", text, flags=re.UNICODE)
#text = text.lstrip().rstrip()
#ntext = "".join(text.split(r'\s+')

e = re.sub(r"\s+", " ", text)
#print(e)

#ne=re.compile("[\W\d]+")
#nee = re.sub("_","abcd1234!@#$")
ne=re.sub(r'[^A-Za-z0-9]+', r'',e)
#ne = re.sub("[\W\d]+", "", e.strip())
print(ne)
#print nltk.clean_html(f.read())


