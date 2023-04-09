from socket import *

server_ip = "127.0.0.1"
server_port = 3333
BUFFER_SIZE = 1024

client_sock = socket(AF_INET, SOCK_STREAM)
client_sock.connect((server_ip, server_port))

while True:
    user_input = input("> ")
    client_sock.sendall(user_input.encode())

    if user_input == "quit":
        break

    response = client_sock.recv(BUFFER_SIZE).decode()
    print(response.strip())

client_sock.close()