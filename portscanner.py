import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

for port in range(1,1025):
    try:
        s.connect((socket.gethostname(), port))
        print('Port {} is open'.format(port))
        s.close()
    except socket.error:
        print('Port {} is closed'.format(port))
