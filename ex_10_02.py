try:
    fname = input('Enter a file name:')
    fhand = open(fname)
except:
    print('No file found, please check the file name.')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            time = words[5].split(':')
            hours = time[0]
            counts[hours] = counts.get(hours, 0)+1
        else:
            continue
    else:
        continue
#print(counts)

lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))
lst.sort()
print(lst)
