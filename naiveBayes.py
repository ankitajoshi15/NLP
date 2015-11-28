import codecs
import re
import math
'''
Training part of Naive Bayes Module:
We need to count the number of times a word is seen for a given label, 
the number of documents seen for a given label (in our case one sentence is a document; so total number of marathi/hindi sentences), 
and labels we have seen throughout our data i.e two -> marathi and hindi.
'''
#making the dictionary
labels = ["marathi","hindi"]
scores = {}
mword_count = {}
hword_count = {}
marathiDocuments = 67204 #number of marathi documents
hindiDocuments = 42341	#number of hindi documents
marathiInverseCount = 42341 #numbner of documents without the marathi label
hindiInverseCount = 67204 #number of documents without the hindi label
totalDocuments = 109545	#number of documents without the marathi label



#counting number of words for "marathi" label
'''
with codecs.open('marathi.txt','r') as out:
	for line in out:
		words = re.split("\s+",line)
		for each_word in words:
			if each_word in mword_count:
			    mword_count[each_word] += 1
			else:
    				mword_count[each_word] = 1	
		out.close

for k,v in mword_count.items():
	with codecs.open('mwordcount.txt','a',encoding = 'utf-8') as q:
		if not k == "":
			value = k.decode('utf-8') + ":" + str(v)
			q.write(value + '\n')
			q.close

#counting number of words for "hindi" label
with codecs.open('hindi.txt','r') as out:
        for line in out:
                words = re.split("\s+",line)
                for each_word in words:
                        if each_word in hword_count:
                            hword_count[each_word] += 1
                        else:
                                hword_count[each_word] = 1
                out.close

for k,v in hword_count.items():
        with codecs.open('hwordcount.txt','a',encoding = 'utf-8') as q:
                if not k == "":
                        value = k.decode('utf-8') + ":" + str(v)
                        q.write(value + '\n')
                        q.close

'''

#calculating the probabilites for words

with codecs.open('predict.txt','r') as out:
	for line in out:
		checkwords = line.split(" ")
scores["marathi"] = 0
scores["hindi"] = 0
for l in labels:
	logSum = 0
	for w in checkwords:
	
		if w in hword_count.keys():
			stemTotalCount = hword_count[w]
			label = "hindi"
		else:
			if w in mword_count.keys():
				stemTotalCount = mword_count[w]
				label = "marathi"
			else:
				stemTotalCount = 0
		if stemTotalCount is 0:
			continue
		else:
	
			if label == "hindi":
				wordProbability = stuff[1] / hindiDocuments
				wordInverseProbability = 0 / marathiDocuments
	
			else:
				if label == "marathi":
					wordProbability = stuff[1] / marathiDocuments
        				wordInverseProbability = 0 / hindiDocuments

			wordicity = wordProbability / (wordProbability + wordInverseProbability)
			wordicity = ( (1 * 0.5) + (stemTotalCount * wordicity) ) / ( 1 + stemTotalCount )
			if wordicity is 0:
				wordicity = 0.01
			else:
				if wordicity is 1:
					wordicity = 0.99
			logsum += (math.log(1-wordicity) - math.log(wordicity))

	scores[l] = 1 / ( 1 + math.exp(logSum) )

for l in scores:
	print l,scores[l]
