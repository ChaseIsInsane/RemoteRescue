import keyboard
from threading import Thread
import socket
import time
import json
import queue

def CheckEscape(): #Checks if the user has pressed Esc, signaling he wants to quit the program.
    done = False
    while not done:
        if keyboard.is_pressed(1): 
            done = True
    raise Exception('User has exited the program.')


def main():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 5000))
    print('Server started.')
    sock.listen(1)
    conn, addr = sock.accept()
    print('Client connected: ' , addr)
    key = {
        'x' : False ,
        'y' : 500
    }
    conn.send(json.dumps(key).encode())
    #key = keyboard.read_key()
    #temp = key
    #conn.send(key.encode())

    #for i in range(100):
        #key = keyboard.read_key()
        #if temp == key:
            #time.sleep(0.1)
            #temp = ''
           # continue
       # else:
         #   temp = key
        #    conn.send(key.encode())
        
    sock.close()





if __name__ == '__main__':
    main()