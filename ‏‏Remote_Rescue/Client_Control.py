import socket
import pyautogui
import keyboard
import queue

def recieve_key(conn, q):
    done = False
    try:
        while not done:
            dic = q.get()
            key = dic['key']
            if key == 'esc':
                done = True
                break
            if key == 'shift':
                keyboard.press('shift')
                dic = q.get()
                key = dic['key']
                keyboard.press_and_release(key)
                keyboard.release('shift')
            else:
                keyboard.press_and_release(key)
    except socket.error:
        print('complete')
    except Exception as e:
        print('Something went wrong :' , e)
        print('incomplete')
    finally:
        keyboard.release('shift')
        print('complete')


def recieve_mouse(conn, q):
    done = False
    try:
        while not done:
            dic = q.get()
            pos = dic['pos']
            pyautogui.moveTo(pos)
    except socket.error:
        print('complete')
    except Exception as e:
        print('Something went wrong:' , e)
        print('incomplete')
    finally:
         print('complete')