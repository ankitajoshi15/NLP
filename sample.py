# -*- coding: utf-8 -*-

import codecs
from bs4 import BeautifulSoup
import urllib2
import re

regex = re.compile(ur"[^\u0900-\u097F\s]+")
htmlFile = urllib2.urlopen("http://blogs.navbharattimes.indiatimes.com/apninazarse/entry/why-silent-on-return-to-nation")
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
                        	print clean1.encode('utf-8')
                        	out.close
