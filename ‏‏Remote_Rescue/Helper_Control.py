import socket
import pyautogui
import keyboard
import time
from Message import Keyboard
from Message import Mouse


def send_key(conn):
    try:
        inp = keyboard.read_key()
        temp = inp
        key = Keyboard(inp)
        conn.send(key.serialize())
        done = False
        while not done:
            inp = keyboard.read_key()
            if inp == 1:
                done = True
                break
            if temp == inp:
                time.sleep(0.1)
                temp = ''
                continue
            else:
                temp = inp
                key.SetKey(inp)
                conn.send(key.serialize)
    except socket.error:
        print('complete')
    except Exception as e:
        print(e)
        print('incomplete')
    finally:
        conn.close()
        print('complete')

def send_mouse(conn):
    done = False
    try:
        while not done:
            x, y = pyautogui.position()
            mouse = Mouse(x, y)
            conn.send(mouse.serialize())
    except socket.error:
        print('complete')
    except Exception as e:
        print('Something went wrong:' , e)
        print('incomplete')
    finally:
        conn.close()
        print('complete')