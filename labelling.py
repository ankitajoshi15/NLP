import codecs
from chardet import detect

f = open('hindi.txt','r')    
for line in f:

	#decode the input
	l = unicode(line, encoding='utf-8')# decode the input                                                                                  
    	some = line.split(".")
	for s in some:
		if not s=="":		
			print s.decode('utf-8')
			str1 = ''.join(s)
			value = 'hindi,' + str1 + '\n'
			print(value)
			with codecs.open('hlabel.txt', 'a', encoding='utf-8') as out:
				s1 = value.decode('utf-8')
                		out.write(s1)
                		out.close
			
			#answer = str1.join('marathi')
			#print str1.decode('utf-8')
			#print answer.decode('utf-8')
			#print('\n')
			str1 = ""
		#str1 = 'marathi,'.join(s)
	#encode the output
		#print str1.decode('utf-8')
		#print('\n')                                                                                           
f.close()

