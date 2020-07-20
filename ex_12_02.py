import socket

try:
    uname = input('Enter URL:')
    wname = uname.split('/')

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((wname[2], 80))
    cmd = ('GET ' + uname + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    tdata = []
    i = 0
    tcount = 0
    counts = 0
    while True:
        data = mysock.recv(512)


        for i in data.decode():
            counts = counts + 1
            if counts <= 3000:
                tdata.append(i)
            else:
                break
        tcount = tcount + len(data)

        if len(data) < 1:
            break

    mysock.close()

    print('First 3000 characters are:', tdata)
    print('The length is :', len(tdata))
    print('Total number of characters:', tcount)

except:
    print('Error: check url again.')
