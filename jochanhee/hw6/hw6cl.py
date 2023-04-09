import socket
import time

device1_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device1_sock.connect(('localhost', 3333))
device2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device2_sock.connect(('localhost', 3334))

while True:
    user_input = input("Input (1: Device1, 2: Device2, quit: exit): ")
    
    if user_input == '1':
        device1_sock.send('Request'.encode())
        data = device1_sock.recv(1024).decode()
        print(data)
        temp, humid, illum = data.split()
        with open('data.txt', 'a') as f:
            f.write(f"{time.strftime('%c', time.localtime(time.time()))}: Device1: Temp={temp}, Humid={humid}, Illum={illum}\n")
        print("Data saved to data.txt for Device1")
    elif user_input == '2':
        device2_sock.send('Request'.encode())
        data = device2_sock.recv(1024).decode()
        print(data)
        heartbeat, steps, cal = data.split()
        print(steps)
        with open('data.txt', 'a') as f:
            f.write(f"{time.strftime('%c', time.localtime(time.time()))}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n")
        print("Data saved to data.txt for Device2")

    elif user_input == 'quit':
        device1_sock.send('quit'.encode())
        device2_sock.send('quit'.encode())
        break
device1_sock.close()
device2_sock.close()