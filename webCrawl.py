# -*- coding: utf-8 -*-
import codecs
import nltk
import urllib2
import re
from bs4 import BeautifulSoup
import string
from bs4 import SoupStrainer

regex = re.compile(ur"[^\u0900-\u097F\s]+")
with open("hindiulrs.txt") as f:
    for line in f:
        htmlFile = urllib2.urlopen(line)

	soup = BeautifulSoup(htmlFile)

	text = soup.getText()

	test = text.replace(ur"।",".")


	x = re.sub("\s+"," ", test)

	y = x.split(".")

	for i in y:
                clean1 = regex.sub("", i)
                if not clean1 == "" and not clean1.isspace():
                        with codecs.open('please_work.txt', 'a', encoding='utf-8') as out:
                                out.write(re.sub("\s+"," ",clean1) +'\n')
#                                print clean1.encode('utf-8')
                                out.close
	print(line)

f.close
