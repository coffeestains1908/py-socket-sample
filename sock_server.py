import socket
import threading
import hashlib
import uuid

from sock_client import Client


class Server:
    port = None
    __server_stopped__ = False
    __server_thread__ = None
    __shutdown_key__ = 'neuon-qqq'
    __close_signature__ = ''

    def __init__(self, port=8080):
        self.port = port
        self.__close_signature__ = str(uuid.uuid4())

    def __start_server__(self):
        while True:
            if self.__server_stopped__:
                break

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', self.port))
                s.listen()
                print(f'Server listening on port {self.port}')
                conn, addr = s.accept()
                try:
                    with conn:
                        print('connected => ', addr)
                        while True:
                            if self.__server_stopped__:
                                break
                            try:
                                print('Awaiting incoming connection ...')
                                data = conn.recv(1024)
                                data = data.decode('utf8')
                                client_host, client_port = conn.getpeername()
                                print(client_host, client_port)
                                if data == self.__close_sign__() and client_host == '127.0.0.1':
                                    self.__server_stopped__ = True
                                    print('Server shutdown command received')
                                print(f'Received "{data}" from client')
                                print('Sending back response')
                                conn.sendall(b'OK')
                            except Exception as e1:
                                print(e1)

                            conn.sendall(b'')
                except Exception as e:
                    print(e)
                conn.close()

    def start(self):
        print(f'Starting server')
        self.__server_thread__ = threading.Thread(target=self.__start_server__)
        self.__server_stopped__ = False
        self.__server_thread__.start()
        # self.__server_thread__.join()

    def __close_sign__(self):
        return self.__shutdown_key__ + self.__close_signature__

    """
    server stop only if a specific string is received from localhost  with a random fingerprint
    """
    def stop(self):
        print("Stopping server")
        c = Client('127.0.0.1', self.port)
        c.send_string(self.__close_sign__())
