f = open('marathi.txt','r')
for line in f:

        #decode the input
        l = unicode(line, encoding='utf-8')# decode the input                                                                                  
        some = line.split(" ")
        for s in some:
                if not s=="":
                        #spaceshit = s.split(" ")
			#for k in spaceshit:
			print(s.decode('utf-8') + "FUCK")
			#	print("\tFUCK\t")
			#	print('\n')
f.close()

