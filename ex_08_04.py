try:
    fname = input('Enter file:')
    fhand = open(fname)
except:
    print('No file is found, please check the name.')
inp=fhand.read()
words=inp.split()

wordlist = []
i=0
wdl = len(words)

while i < wdl:
    if words[i] not in wordlist:
        wordlist.append(words[i])
    i=i+1
wordlist.sort()

print(wordlist)

