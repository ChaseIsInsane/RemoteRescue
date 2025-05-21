from threading import Thread
import socket
from Screen_Share import *


def main(host='0.0.0.0', port=5000):
    sock = socket()
    sock.bind((host, port))
    try:
        sock.listen(1)
        print('Server started.')

        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            thread = Thread(target=retreive_screenshot, args=(conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()