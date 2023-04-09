import socket
import random
from datetime import datetime

def get_data():
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    illum = random.randint(70, 150)
    return f"{temp} {humid} {illum}"

device1_port = 3333
device1_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device1_sock.bind(('localhost', device1_port))
device1_sock.listen(1)

while True:
    conn, addr = device1_sock.accept()
    while True:
        data = conn.recv(1024).decode()
        if data == 'Request':
            response = get_data()
            conn.send(response.encode())
        elif data == 'quit':
            break
    conn.close()