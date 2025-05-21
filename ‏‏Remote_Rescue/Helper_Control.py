import socket
import keyboard
import time
from Message import Keyboard
from Message import Mouse
import queue
import pygame
import pyautogui


def send_key(conn, q):
    try:
        #inp = keyboard.read_key()
        inp = q.get()
        temp = inp
        key = Keyboard(inp)
        conn.send(key.serialize())
        done = False
        while not done:
            #inp = keyboard.read_key()
            inp = q.get()
            if inp == 'escape':
                done = True
                break
            if temp == inp:
                time.sleep(0.1)
                temp = ''
                continue
            else:
                temp = inp
                key.SetKey(inp)
                conn.send(key.serialize())
    except socket.error:
        print('complete')
    except Exception as e:
        print(e)
        print('incomplete')
    finally:
        conn.close()
        print('complete')

def send_mouse(conn, q):
    done = False
    try:
        while not done:
            pos = pyautogui.position()
            dic = q.get()
            print(dic)
            scroll = dic['scroll']
            click_state = dic['pressed']
            mouse = Mouse(pos, click_state, scroll)
            conn.send(mouse.serialize())
    except socket.error:
        print('complete')
    except Exception as e:
        print('Something went wrong:' , e)
        print('incomplete')
    finally:
        conn.close()
        print('complete')