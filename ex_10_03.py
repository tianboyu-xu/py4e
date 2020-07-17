import string
try:
    fname = input('Enter a file name:')
    fhand = open(fname)
except:
    print('No file found, please check the file name.')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        t = tuple(word)
        for letter in t:
            counts[letter] = counts.get(letter, 0) + 1

lst = list()
for key, val in list(counts.items()):
    lst.append((val,key))
lst.sort(reverse=True)
for key, val in lst[:26]:
    print(key,val)
