import socket

try:
    uname = 'http://data.pr4e.org/romeo.txt'
    wname = uname.split('/')

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((wname[2], 80))
    cmd = ('GET ' + uname + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    tdata = []
    sep = []
    i = 0
    tcount = 0
    counts = 0
    while True:
        data = mysock.recv(512)
        for i in data.decode():
            counts = counts + 1
            tdata.append(i)
            if counts >= 3 and tdata[counts-4:counts] == ['\r', '\n', '\r', '\n']:
                sep.append(counts)
        if len(data) < 1:
            break
        print(data.decode())
    mysock.close()

    print(tdata[sep[0]:])

except:
    print('Error: check url again.')
