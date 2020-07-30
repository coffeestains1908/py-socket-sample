import socket

host = '127.0.0.1'
port = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.send(b'')
    data = s.recv(1024)

print('received from server', repr(data))
