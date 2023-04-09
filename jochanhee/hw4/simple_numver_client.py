from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))
while True:
    # 계산식 입력받기
    msg = input('계산식을 입력하세요: ')
    if msg == 'q':
        break
    # 서버로 계산식 전송
    s.send(msg.encode())
    # 서버로부터 결과 수신
    result = s.recv(1024).decode()
    # 결과 출력
    print('결과: ', result)
s.close()