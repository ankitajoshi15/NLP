from nltk.util import ngrams
from nltk import NaiveBayesClassifier as nbc


hindi = "".join(open('hlabel.txt','r'))
marathi = "".join(open('mlabel.txt','r'))

#print hindi

print ngrams(hindi[:10], 2)

