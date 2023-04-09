from socket import *

server_port = 3333
BUFFER_SIZE = 1024
server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(('', server_port))
server_sock.listen(1)

mailbox = {}

print("서버가 실행 중입니다. 클라이언트를 기다리는 중...")

while True:
    conn, addr = server_sock.accept()
    print(f"클라이언트 {addr}가 연결되었습니다.")

    while True:
        data = conn.recv(BUFFER_SIZE).decode()
        if not data:
            break

        tokens = data.split()
        cmd, mbox_id = tokens[0], tokens[1]

        if cmd == "send":
            message = " ".join(tokens[2:])
            if mbox_id in mailbox:
                mailbox[mbox_id].append(message)
            else:
                mailbox[mbox_id] = [message]
            conn.sendall("OK\n".encode())

        elif cmd == "receive":
            if mbox_id in mailbox and len(mailbox[mbox_id]) > 0:
                message = mailbox[mbox_id].pop(0)
                conn.sendall((message + "\n").encode())
            else:
                conn.sendall("No messages\n".encode())

        elif cmd == "quit":
            conn.close()
            server_sock.close()
            print("서버가 종료되었습니다.")
            exit(0)

    conn.close()