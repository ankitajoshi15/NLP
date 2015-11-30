import codecs
import re


mword_count ={}

with codecs.open('predict.txt','r') as out:
        for line in out:
                words = re.split("\s+",line)
                for each_word in words:
                        if each_word in mword_count.keys():
                            mword_count[each_word] += 1
                        else:
                                mword_count[each_word] = 1
                out.close

for k,v in mword_count.items():
	print k.decode('utf-8'), ":",v
