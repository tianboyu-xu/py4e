fname = input("Enter a file name:")
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        print(words[1])
    else:
        continue
