import threading
from signal import signal, SIGINT
from sys import exit

from sock_server import Server


def exit_handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    server.stop()
    exit(0)


if __name__ == '__main__':
    # required because socket listening cannot simply be ctrl+c
    signal(SIGINT, exit_handler)

    server = Server(port=6000)
    server.start()

    print('Running. Press CTRL-C to exit.')
    while True:
        pass
