import codecs
from chardet import detect

f = open('marathi.txt','r')    
for line in f:

	#decode the input
	l = unicode(line, encoding='utf-8')# decode the input                                                                                  
    	some = line.split(".")
	for s in some:
		if not s=="":		
			print s.decode('utf-8')
			str1 = ''.join(s)
			value = str1 + ',marathi'
			with codecs.open('hindi.txt', 'a', encoding='utf-8') as out:
                		out.write(value)
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

