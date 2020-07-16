
try:
    #fname = input('Enter a file name:')
    fhand = open(fname)
except:
    print('No file found, please check the file name.')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 2:
            sender = words[1]                                                                                           # Find full email address
            sender_dm = sender[sender.find('@')+1:]                                                                     # Strip address after @
            counts[sender_dm] = counts.get(sender_dm, 0)+1                                                              # Count domain number
        else:
            continue
    else:
        continue
print(counts)

