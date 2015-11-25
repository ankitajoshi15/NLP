filenames = ['nmlabel.txt', 'nhlabel.txt']
with open('newlabels.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
