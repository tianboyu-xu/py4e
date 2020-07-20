import urllib.request, urllib.parse, urllib.error

try:
    uname = input('Enter URL:')
    fhand = urllib.request.urlopen(uname)

    tdata = []
    i = 0
    tcount = 0
    counts = 0

    for lines in fhand:
        line = lines.decode()
        for i in line:
            counts = counts + 1
            if counts <= 3000:
                tdata.append(i)
            else:
                break
        tcount = tcount + len(lines)

    print('First 3000 characters are:', tdata)
    print('The length is :', len(tdata))
    print('Total number of characters:', tcount)

except:
    print('Error: check url again.')
