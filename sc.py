filenames = ['marathilabel.txt', 'hindilabel.txt']
with open('labelled.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
