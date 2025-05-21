import json
import socket
import pygame
from Message import Mouse

WIDTH = 1500
HEIGHT = 780

def main():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 5000))
    print('Server started.')
    sock.listen(1)
    conn, addr = sock.accept()
    print('Client connected: ' , addr)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEWHEEL:
                print(event.y)


                
        state = pygame.mouse.get_pressed()
        conn.send(json.dumps(state).encode())
        #pos = pygame.mouse.get_pos()
        #conn.send(json.dumps(pos).encode())
                
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)  
        





if __name__ == '__main__':
    main()