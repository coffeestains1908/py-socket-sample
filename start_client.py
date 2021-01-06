from sock_client import Client

if __name__ == '__main__':
    c = Client('127.0.0.1', 6000)
    c.send_string('hello my dear friend this message might be too long for  you to receive but i do hope all things go as planned. Happy new year!')
