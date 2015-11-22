#importing module to crawl
import codecs
import nltk
import urllib2

f = urllib2.urlopen("https://mr.wikipedia.org/s/2cv")
print nltk.clean_html(f.read())


