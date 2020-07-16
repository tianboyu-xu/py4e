fname = input('Enter a file name:')

try:
    fhand = open(fname)
    for line in fhand:
        line = line.rstrip()
        line = line.upper()
        print(line)
except:
    print('No file found, please check the name')
