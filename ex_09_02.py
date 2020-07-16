try:
    fname = input('Enter a file name:')
    fhand = open(fname)
except:
    print('No file found, please check the file name.')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 3:
            weekday = words[2]
            counts[weekday] = counts.get(weekday, 0)+1
        else:
            continue
    else:
        continue
print(counts)
