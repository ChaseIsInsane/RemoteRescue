import socket
from threading import Thread
from Screen_Share import retreive_screenshot
from Client_Control import *
from Message import *
import queue


def Client(host='192.168.1.111', port=5000):
    #Create a connection to the screen sharing port.
    sock = socket.socket()
    sock.connect((host, port))
    print('connected successfully')
    # Create queue storing mouse and keyboard inputs from the Helper.
    mouse_q = queue.Queue() 
    keyboard_q = queue.Queue()
    #Begin threads activity.
    mouse = Thread(target=recieve_mouse, args= (mouse_q,))
    mouse.start()
    keys = Thread(target=recieve_key, args=(keyboard_q,))
    keys.start()
    ss = Thread(target=retreive_screenshot,args=(sock,))
    ss.start()
    #Create conditionals for closing the program.
    threads = [ss, mouse, keys]
    done = False
    try:
        while not done: 
            for i in threads: #Check if one thread has finished then finish them all.
                if i.is_alive() == False:
                    done = True
                    break
            if not done:
                print('recieving...')
                command = deserialize(sock.recv(1024).decode())
                print('recived: ' , command)
                if command['type'] == 'mouse':
                    mouse_q.put(command) 
                elif command['type'] == 'keyboard':
                    keyboard_q.put(command)
                else:
                    continue
    except socket.error:
        pass
    #except Exception as e:
        #print('Something went wrong: ', e)
    finally:
       # mouse.join()
        keys.join()
        ss.join()
        print('Finished!')

    