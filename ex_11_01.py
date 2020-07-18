import re
fhand = open("mbox.txt")
term = input('Enter a regular expression:')
num = 0
for line in fhand:
    line = line.rstrip()
    if re.search(term, line):
        num = num + 1
    else:
        continue
print('mbox.txt had', num, 'lines that matched', term)
