import random

with open('labelled.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('train.txt','w') as target:
    for _, line in data:
        target.write( line )
