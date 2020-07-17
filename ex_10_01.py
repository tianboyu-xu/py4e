try:
    fname = input('Enter a file name:')
    fhand = open(fname)
except:
    print('No file found, please check the file name.')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 2:
            sender = words[1]
            counts[sender] = counts.get(sender, 0)+1
        else:
            continue
    else:
        continue
#print(max(counts))

#current_max = 0
#for key in counts:
#    if counts[key] > current_max:
#        current_max = counts[key]
#        k_max = key
#    else:
#        continue
#print('The max sender is :', k_max, current_max)

#print('The max sender is :',  max(counts, key=counts.get), counts[max(counts, key=counts.get)] )

lst = list()
for key, val in list(counts.items()):
    lst.append((val,key))
lst.sort(reverse=True)
for key, val in lst[:1]:
    print(key,val)
