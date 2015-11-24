filenames = ['marathi1.txt', 'marathi2.txt']
with open('marathi.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
