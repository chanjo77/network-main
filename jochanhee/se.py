import socket
s = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)
while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'ok ' + addr[0].encode())
    data = client.recv(1024)
    print(data.decode())
    name = 20171503
    data1 = name.to_bytes(4,'big')
    client.send(data1)
    client.close()
