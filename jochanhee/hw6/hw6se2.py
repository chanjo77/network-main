import socket
import random
from datetime import datetime

def get_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    return f"{heartbeat} {steps} {cal}"

device2_port = 3334
device2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device2_sock.bind(('localhost', device2_port))
device2_sock.listen(1)

while True:
    conn, addr = device2_sock.accept()
    while True:
        data = conn.recv(1024).decode()
        if data == 'Request':
            response = get_data()
            conn.send(response.encode())
        elif data == 'quit':
            break
    conn.close()