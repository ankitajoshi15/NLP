import codecs
from textblob.classifiers import NaiveBayesClassifier


aList = []
with codecs.open("train.csv" , 'r' ,encoding = 'utf-8') as out:
	for line in out:
		aList.append(line.decode('utf-8'))
		
print(aList)

'''
cl = NaiveBayesClassifier("train.csv","csv")



with codecs.open("predict.txt",'r') as out:
	for line in out:
		cl.classify(line)
'''
