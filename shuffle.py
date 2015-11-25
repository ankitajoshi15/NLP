import random

with open('labels.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('slabel.txt','w') as target:
    for _, line in data:
        target.write( line )
