import socket
import pyautogui
import keyboard
import queue

def recieve_key(q):
    done = False
    try:
        while not done:
            dic = q.get()
            key = dic['key']
            print('recieved: ', key)
            if key == 'esc':
                done = True
                break
            if key == 'left shift':
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


def recieve_mouse(q):
    done = False
    try:
        while not done:
            dic = q.get()
            pos = dic['pos']
            pyautogui.moveTo(pos)
            print('mouse moved.')
            click_state = dic['click_state']
            scroll = dic['scroll']
            if len(click_state) > 0:
                if click_state[0] == True:
                    pyautogui.leftClick()
                if click_state[1] == True:
                    pyautogui.middleClick()
                if click_state[2] == True:
                    pyautogui.rightClick()
            pyautogui.scroll(scroll)
    except socket.error:
        print('complete')
    except Exception as e:
        print('Something went wrong:' , e)
        print('incomplete')
    finally:
        print('complete')