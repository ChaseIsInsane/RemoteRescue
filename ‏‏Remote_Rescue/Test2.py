import socket
import keyboard
import json
import pyautogui

def main():
    try:
        sock = socket.socket()
        sock.bind(('0.0.0.0', 5000))
        sock.close()
        sock.listen(1)
    except socket.error:
        print('whhopsy daisy:')
    #print('connected')

  #  for i in range(100):
    #    key = sock.recv(1024).decode()
    #    if key == 'shift':
    #        keyboard.press('shift')
    #        key = sock.recv(1024).decode()
    #        keyboard.press_and_release(key)
     #       keyboard.release('shift')
     #   else:
     #       keyboard.press_and_release(key)

   # key = json.loads(sock.recv(1024).decode())
    #print(key)


    #sock.close()

    

    x, y = pyautogui.position()
    print(x)
    print(y)
    print(type(x))
    print(type(y))
    pyautogui.moveTo((500, 1000))
    x, y = pyautogui.position()
    print(x)
    print(y)



if __name__ == '__main__':
    main()