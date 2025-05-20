from threading import Thread
import socket
from Screen_Share import *
from terminate import *
from Helper_GUI import helper


def Server(host='0.0.0.0', port=5000):
    sock = socket()
    sock.bind((host, port))
    try:
        sock.listen(1)
        print('Server started.')
        count = 0
        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            begin = Thread(target=helper,args=(conn,))
            begin.start()
            #Checking if another user has attempted to connect.
            count += 1
            if count > 1:
                raise RescueException('Another user has attempted to connect, exiting now.') 
    except RescueException():
        pass
    finally:
        begin.join()
        sock.close()

