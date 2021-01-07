import socket


class Client:
    host = None
    port = None

    def __init__(self, target_host, target_port):
        self.host = target_host
        self.port = target_port

    def send_string(self, str_to_send):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            print('Awaiting server response ...')
            s.send(bytes(str_to_send, encoding='utf8'))
            data = s.recv(1024)
            s.detach()

        print('Received from server', repr(data))
        return data
