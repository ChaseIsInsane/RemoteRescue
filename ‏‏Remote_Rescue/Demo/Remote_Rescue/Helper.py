from threading import Thread
import socket
from Screen_Share import *
from terminate import *
from Helper_GUI import helper

def main(host = '0.0.0.0', port = 5000):
    sock = socket.socket()
    sock.bind((host, port))
    try:
        sock.listen(1)
        print('Server started.')
        conn, addr = sock.accept()
        print('Client connected IP:', addr)
        helper(conn)
    #except Exception:
        #print('Something went wrong!')
    finally:
        conn.close()


if __name__ == '__main__':
    main()