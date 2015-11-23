#importing module to crawl
import codecs
import nltk
import urllib2
import re
from bs4 import BeautifulSoup
import string
import unicodedata

f2 = urllib2.urlopen("https://mr.wikipedia.org/s/2cv").read().decode("utf-8-sig")
regex = re.compile(ur"[^\u0900-\u097F]+")
f = regex.sub("foo", f2)

soup = BeautifulSoup(f)
text = soup.getText()

#remove extra spaces
removedSpaces = re.sub(r"\s+", " ", text)

#remove ascii characters

_ascii_letters = re.compile(r'[a-zA-Z0-9]', flags=re.UNICODE)
removedEnglish = _ascii_letters.sub("", removedSpaces)


#remove the punctuation marks like "?,!,/,\,(,)

#punctutationMarks = re.compile(r'[?|$|.|!|(|)|%|#|}|{|.|;|,]')
#devnagri = re.compile([\u0900-\u097F],re.UNICODE)



clean = re.sub(r"['_,!\-\"\\\/}{?\.()%$*;\[\]:><|=@#]",'',removedEnglish).strip()

print(clean)

