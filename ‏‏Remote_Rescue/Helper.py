from threading import Thread
import socket
from Screen_Share import *
from Helper_GUI import helper
from Helper_Control import *

def main(host = '0.0.0.0', port = 5000):

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    print('Server listening...')
    conn, addr = sock.accept()
    print('Client connected: ' , addr)
    try:
        mouse = Thread(target=send_mouse, args=(conn, ))
        mouse.start()
        key = Thread(target=send_key, args=(conn, ))
        key.start()
        t = Thread(target=helper, args= (conn, ))
        t.start()
        threads = [mouse, key, t]
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
        print('Finished!')
        

if __name__ == '__main__':
    main()