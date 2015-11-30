# -*- coding: utf-8 -*-
import codecs
from chardet import detect

with codecs.open('marathi.txt', 'r', encoding='utf-8') as rr:

	for line in rr:                                                                               
	#	print line.encode('utf-8')
		l = line.split("\n")
		w =l[0].rstrip()
		str1 = ''.join(w)
		value = str1 + ',marathi' + '\n'
#		print(value)
		str1 = ""
		with codecs.open('marathilabel.txt', 'a', encoding='utf-8') as out:
				#s1 = value.decode('utf-8')
                		out.write(value)
                		out.close
			
			#answer = str1.join('marathi')
			#print str1.decode('utf-8')
			#print answer.decode('utf-8')
			#print('\n')
			
		#str1 = 'marathi,'.join(s)
	#encode the output
		#print str1.decode('utf-8')
		#print('\n')                                                                                           

