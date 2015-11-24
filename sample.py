import codecs
from bs4 import BeautifulSoup
import urllib2

htmlFile = urllib2.urlopen("http://blogs.navbharattimes.indiatimes.com/apninazarse/entry/why-silent-on-return-to-nation")
soup = BeautifulSoup(htmlFile)
text = soup.getText()

print(text)
