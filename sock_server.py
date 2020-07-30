import socket

host = '127.0.0.1'
port = 1024

my_variable = b'test'

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        try:
            with conn:
                print('connected by', addr)
                while True:
                    try:
                        data = conn.recv(1024)
                        if data:
                            my_variable = data
                    except Exception as e1:
                        print(e1)
                    conn.sendall(my_variable)
        except Exception as e:
            print(e)
