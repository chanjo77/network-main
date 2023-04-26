import socket
import threading

def receive_messages(sock):
    while True:
        msg = sock.recv(1024).decode()
        print(msg)

server_ip = "127.0.0.1"
server_port = 9000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((server_ip, server_port))

# 서버로부터 메시지를 수신하는 스레드 생성
receiver_thread = threading.Thread(target=receive_messages, args=(client_sock,))
receiver_thread.daemon = True
receiver_thread.start()

# ID 입력 및 서버로 전송
my_id = input("ID를 입력하세요: ")
client_sock.sendall(my_id.encode())

while True:
    user_input = input()
    client_sock.sendall(user_input.encode())

    if user_input == "quit":
        break

client_sock.close()
