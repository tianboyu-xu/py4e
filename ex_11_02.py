import re
fname = input('Enter file:')
fhand = open(fname)
total = 0
num = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        num = num + 1
        total = total + int(x[0])
    else:
        continue
print(float(total/num))
