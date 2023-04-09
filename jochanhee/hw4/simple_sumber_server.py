from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        try:
            # 계산식 파싱
            num1, op, num2 = data.split()
            # 연산 수행
            if op == '+':
                result = int(num1) + int(num2)
            elif op == '-':
                result = int(num1) - int(num2)
            elif op == '*':
                result = int(num1) * int(num2)
            elif op == '/':
                result = round(float(num1) / float(num2), 1)
            else:
                raise ValueError
        except:
            client.send(b'Invalid input')
        else:
            client.send(str(result).encode())
    client.close()