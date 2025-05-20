from socket import socket
from zlib import decompress
import pygame
from threading import Thread
from terminate import *

WIDTH = 1920
HEIGHT = 1080



def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf

def helper(conn):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()   
    watching = True
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            
            
            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(conn.recv(1), byteorder='big')
            print('done1')
            size = int.from_bytes(conn.recv(size_len), byteorder='big')
            print('done2')
            pixels = decompress(recvall(conn, size))
            print('done3')
            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            print('done4')

            # Display the picture
            screen.blit(img, (0, 0))
            print('done5')
            pygame.display.flip()
            print('done6')
            clock.tick(60)
            print('done7')

            #Check if the program needs to close
            #if GetStopFlag() == True:
                #pygame.quit()
    except Exception as e:
        print("\n")
        print(e)
        print("\n")
    finally:
        pass
    