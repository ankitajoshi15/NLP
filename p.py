import codecs



with codecs.open('predict.txt','r') as out:
        for line in out:
		print line
