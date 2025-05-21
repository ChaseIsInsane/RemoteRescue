import socket
from zlib import decompress
import pygame
from Message import *

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

def helper(conn, key_q, mouse_q):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()   
    try:
        while True:
            scroll = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    code = event.key
                    key = pygame.key.name(code)
                    key_q.put(key)
                if event.type == pygame.MOUSEWHEEL:
                    scroll = event.y
                pressed = pygame.mouse.get_pressed()
                mouse_q.put({'scroll' : scroll , 'pressed' : pressed})
            
            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(conn.recv(1), byteorder='big')
            size = int.from_bytes(conn.recv(size_len), byteorder='big')
            pixels = decompress(recvall(conn, size))

            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
    except socket.error:
        print('sock error')
    finally:
        pygame.quit()