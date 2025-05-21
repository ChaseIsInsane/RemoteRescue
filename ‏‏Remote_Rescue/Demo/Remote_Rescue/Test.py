import keyboard
from terminate import *
from threading import Thread

def CheckEscape(): #Checks if the user has pressed Esc, signaling he wants to quit the program.
    done = False
    while not done:
        if keyboard.is_pressed(1): 
            done = True
    raise RescueException('User has exited the program.')


def main():
    escape = Thread(target=CheckEscape)
    escape.start()
    escape.join()
    print(11)





if __name__ == '__main__':
    main()