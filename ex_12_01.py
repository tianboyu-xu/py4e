import socket

try:
    uname = input('Enter a url address:')
    wname = uname.split('/')

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((wname[2], 80))
    cmd = ('GET ' + uname + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print('Error: check url again.')

