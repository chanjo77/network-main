import socket
import threading
import time

clients = {}  # 클라이언트의 소켓과 ID를 저장하는 딕셔너리

def handle_client(client_socket, client_addr):
    global clients
    client_id = client_socket.recv(1024).decode()
    clients[client_socket] = client_id

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"new client {client_addr}")
    print(f"{current_time} {client_addr}가 연결되었습니다. ID: {[client_id]}")

    # 현재 접속한 클라이언트 ID 목록 전송
    client_ids = ', '.join(clients.values())
    client_socket.sendall(f"채팅방 인원 : {client_ids}".encode())

    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            print(f"사물 채팅방 ({client_id}): {msg.decode()}")

            for client in clients:
                if client != client_socket:
                    client.sendall(f"{client_id}: {msg.decode()}".encode())
        except Exception as e:
            print(f"클라이언트 {client_id} 처리 중 오류 발생: {e}")
            break

    print(f"클라이언트 {client_id}와의 연결이 종료되었습니다.")
    clients.pop(client_socket)
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 9000))
server_socket.listen(5)

print("멀티 스레드 채팅 서버가 시작되었습니다. 클라이언트를 기다리는 중...")

while True:
    client_socket, client_addr = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
    client_thread.daemon = True
    client_thread.start()