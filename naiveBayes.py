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
flag = 0
Documents = {}
InverseDocuments = {}
scores = {}
mword_count = {}
hword_count = {}
Documents["marathi"] = 67204.0 #number of marathi documents
Documents["hindi"] = 42341.0	#number of hindi documents
InverseDocuments["marathi"] = 42341.0 #numbner of documents without the marathi label
InverseDocuments["hindi"] = 67204.0 #number of documents without the hindi label
totalDocuments = 109545.0	#number of documents without the marathi label


'''
#counting number of words for "marathi" label
print("Counting marathi")
with codecs.open('marathi.txt','r') as out:
	for line in out:
		words = re.split("\s+",line)
		for each_word in words:
			if each_word in mword_count.keys():
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

print("counting hindi")
#counting number of words for "hindi" label
with codecs.open('hindi.txt','r') as out:
        for line in out:
                words = re.split("\s+",line)
                for each_word in words:
                        if each_word in hword_count.keys():
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
#taking back wordcounts
#mword_count = {}

with codecs.open('hwordcount.txt' , 'r') as out:
	for line in out:
		stuff = line.split(":")
		hword_count.update({stuff[0]:stuff[1]})
	out.close



with codecs.open('mwordcount.txt' , 'r') as out:
        for line in out:
                stuff = line.split(":")
                mword_count.update({stuff[0]:stuff[1]})
        out.close

#for k,v in hword_count.items():
#	print k.decode('utf-8') , ":" , str(v)




#calculating the probabilites for words
'''
with codecs.open('predict.txt','r') as out:
	for line in out:
		checkwords = line.split(" ")
'''
'''
for w in checkwords:
	print w
	if w in hword_count.keys():
		print hword_count[w]
	else:
		print "not present"

	
for w in checkwords:
        print w
        if w in mword_count.keys():
                print mword_count[w]
        else:
                print "not present"

'''


'''

with codecs.open('predict.txt','r') as out:
        for line in out:
                checkwords = line.split(" ")
		scores["marathi"] = 0.0
		scores["hindi"] = 0.0

for l in labels:
	flag = 0
	logSum = 0.0
	for w in checkwords:
		stemTotalCount = 0.0
		stemTotalCount1 = 0.0
		stemTotalCount2 = 0.0
		if w in hword_count.keys():
			stemTotalCount1 = float(hword_count[w])
		if w in mword_count.keys():
			stemTotalCount2 = stemTotalCount + float(mword_count[w])
		if w not in hword_count.keys() and w not in mword_count.keys():
			flag = 1
			stemTotalCount = 0.0
		stemTotalCount = stemTotalCount1 + stemTotalCount2
		if flag is 1:
			continue
		else:
			if l == "marathi":
				wordProbability = stemTotalCount2 / Documents[l]
			else:
				wordProbability = stemTotalCount1 / Documents[l]
			if l == "marathi":
				wordInverseProbability = stemTotalCount1 / InverseDocuments[l]
			else:
				wordInverseProbability = stemTotalCount2 / InverseDocuments[l]
			
			wordicity = wordProbability / (wordProbability + wordInverseProbability)
			wordicity = ( (1.0 * 0.5) + (stemTotalCount * wordicity) ) / ( 1.0 + stemTotalCount )
			
			if wordicity is 0.0:
				wordicity = 0.01
			else:
				if wordicity is 1.0:
					wordicity = 0.99
			logSum += (math.log(1.0-wordicity) - math.log(wordicity))

	scores[l] = 1.0 / ( 1.0 + math.exp(logSum) )

for l in scores:
	print l,scores[l]
'''



def predict():

	number_of_lines = 0
	accuracy = 0
	with codecs.open('predict1.txt','r') as out:
		for line in out:
			print line
			scores = check(line)
			number_of_lines += 1
			#print scores["marathi"]
				#accuracy +=1
	#print accuracy
                






def check(line):

	checkwords = line.split(" ")
	scores["marathi"] = 0.0
	scores["hindi"] = 0.0

	for l in labels: 
		flag = 0
		logSum = 0.0
		for w in checkwords:
			stemTotalCount = 0.0
			stemTotalCount1 = 0.0
			stemTotalCount2 = 0.0
			if w in hword_count.keys():
				stemTotalCount1 = float(hword_count[w])
			if w in mword_count.keys():
				stemTotalCount2 = stemTotalCount + float(mword_count[w])
			if w not in hword_count.keys() and w not in mword_count.keys():
				flag = 1
				stemTotalCount = 0.0
			stemTotalCount = stemTotalCount1 + stemTotalCount2
			if flag is 1:
				continue
			else:
				if l == "marathi":
					wordProbability = stemTotalCount2 / Documents[l]
				else:
					wordProbability = stemTotalCount1 / Documents[l]
				if l == "marathi":
					wordInverseProbability = stemTotalCount1 / InverseDocuments[l]
				else:
					wordInverseProbability = stemTotalCount2 / InverseDocuments[l]

				wordicity = wordProbability / (wordProbability + wordInverseProbability)
				wordicity = ( (1.0 * 0.5) + (stemTotalCount * wordicity) ) / ( 1.0 + stemTotalCount )

				if wordicity is 0.0:
					wordicity = 0.01
				else:
					if wordicity is 1.0:
					        wordicity = 0.99
				logSum += (math.log(1.0-wordicity) - math.log(wordicity))

		scores[l] = 1.0 / ( 1.0 + math.exp(logSum) )
		print l , " ",  scores[l]
	return scores


predict()
