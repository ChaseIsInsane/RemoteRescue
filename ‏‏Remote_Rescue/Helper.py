from threading import Thread
import socket
from Screen_Share import *
from Helper_GUI import helper
from Helper_Control import *
import queue

def main(host = '0.0.0.0', port = 5000):

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    print('Server listening...')
    conn, addr = sock.accept()
    conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    print('Client connected: ' , addr)
    keys = queue.Queue()
    scrolls = queue.Queue()
    try:
        mouse = Thread(target=send_mouse, args=(conn,scrolls))
        mouse.start()
        key = Thread(target=send_key, args=(conn,keys))
        key.start()
        t = Thread(target=helper, args=(conn,keys,scrolls))
        t.start()
        threads = [t, key, mouse]
        done = False
        while not done:
            for i in threads:
                if i.is_alive() == False:
                    done = True
                    conn.close()
    except socket.error:
        pass
    except Exception as e:
        print('Something went wrong: ', e)
    finally:
        sock.close()
        mouse.join()
        key.join()
        t.join()
        print('Finished!')
if __name__ == '__main__':
    main()