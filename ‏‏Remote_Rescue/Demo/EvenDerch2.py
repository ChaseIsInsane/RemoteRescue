import pyautogui
import socket
import threading
import json

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

    def connect(self, peer_host, peer_port):
        try:
            connection = self.socket.connect((peer_host, peer_port))
            self.connections.append(connection)
            print(f"Connected to {peer_host}:{peer_port}")
        except socket.error as e:
            print(f"Failed to connect to {peer_host}:{peer_port}. Error: {e}")

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Listening for connections on {self.host}:{self.port}")

        while True:
            connection, address = self.socket.accept()
            self.connections.append(connection)
            print(f"Accepted connection from {address}")
            break
    
    def send_data(self, data):
        for connection in self.connections:
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f"Failed to send data. Error: {e}")

    def recieve_data(self):
        for connection in self.connections:
            try:
                return connection.recv(1024).decode()
            except:
                print('Error recieving a message.')

    def start(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()

def cursor_MOVE(x=0, y=0):
    pyautogui.moveTo(x, y, 1)
    print('Cursor moved to {0}, {1}', x, y)

def main():
    p1 = Peer('192.168.1.111', 2121)
    p1.listen()
    command = p1.recieve_data()
    if command == 'MOVE':
        cursor_MOVE()
    else:
        print('Invalid command.')


if __name__ == '__main__':
    main()