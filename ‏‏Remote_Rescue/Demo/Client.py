from socket import socket
from zlib import decompress
import pyautogui
import pygame
import msvcrt

WIDTH = 1920
HEIGHT = 1080

def CheckEscape(): #Checks if the user has pressed Esc, signaling he wants to quit the program.
    num = 0
    done = False
    while not done:

        if msvcrt.kbhit() and msvcrt.getwch() == 27:
            pyautogui.alert('You have pressed the Esc button, the program shall now quit.')
            done = True
    return True

def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def main(host='127.0.0.1', port=5000):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True    

    sock = socket()
    sock.connect((host, port))
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
                
            
            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            pixels = decompress(recvall(sock, size))

            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)

            if CheckEscape() == True:
                pygame.quit()
                
    finally:
        sock.close()


if __name__ == '__main__':
    main()