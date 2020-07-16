fname = input('Enter the file name:')
try:
    fhand = open(fname)
    for line in fhand:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            start = line.find(':')
            output = line[start+1:]
            print(output)
except:
    print('No file found, please check the name')
