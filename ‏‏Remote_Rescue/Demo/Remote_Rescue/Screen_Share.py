from zlib import compress
from terminate import *

from mss import mss


WIDTH = 1920
HEIGHT = 1080


def retreive_screenshot(conn):
    with mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while True: 
            # Capture the screen
            img = sct.grab(rect)
            print('done1')
            # Tweak the compression level here (0-9)
            pixels = compress(img.rgb, 6)
            print('done2')
            # Send the size of the pixels length
            size = len(pixels)
            print('done3')
            size_len = (size.bit_length() + 7) // 8
            print('done4')
            conn.send(bytes([size_len]))
            print('done5')

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            print('done6')
            conn.send(size_bytes)
            print('done7')

            # Send pixels
            conn.sendall(pixels)
            print('done8')

            #if GetStopFlag() == True: #Checking stop flag
                #break
