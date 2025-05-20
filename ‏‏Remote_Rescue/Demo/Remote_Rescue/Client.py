import socket
from threading import Thread
from Screen_Share import retreive_screenshot
from terminate import *
import keyboard

def CheckEscape(): #Checks if the user has pressed Esc, signaling he wants to quit the program.
    done = False
    while not done:
        if keyboard.is_pressed(1): 
            done = True
    raise RescueException('User has exited the program.')

def main(host='172.16.10.245', port=5000):
    #Create a thread constantly checking if the client has press Esc.
    escape = Thread(target=CheckEscape)
    escape.start()
    #Create a connection to the server
    sock = socket.socket()
    sock.connect((host, port))
    print('connected successfully')
    thread = Thread(target=retreive_screenshot, args=(sock,))
    thread.start()
    #Check if the program has been stopped and close it properly.
    while True:
        if GetStopFlag() == True:
            break

    thread.join()
    sock.close()
    escape.join()
if __name__ == '__main__':
    main()