import codecs
import re
'''
Training part of Naive Bayes Module:
We need to count the number of times a word is seen for a given label, 
the number of documents seen for a given label (in our case one sentence is a document; so total number of marathi/hindi sentences), 
and labels we have seen throughout our data i.e two -> marathi and hindi.
'''
#making the dictionary

mword_count = {}
hword_count = {}
marathiDocuments = 67204 #number of marathi documents
hindiDocuments = 42341	#number of hindi documents
marathiInverseCount = 42341 #numbner of documents without the marathi label
hindiInverseCount = 67204 #number of documents without the hindi label
totalDocuments = 109545	#number of documents without the marathi label



#counting number of words for "marathi" label
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

#	print k.decode('utf-8') , ":" ,v
	#print v


