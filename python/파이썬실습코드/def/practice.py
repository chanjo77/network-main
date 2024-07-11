# 함수
# def sum (a,b) :
#     result = a+b
#     return result

# print(sum (1,2))

# 결과값이 없을 수도 있다.

# def bank_open(name) :
#     print("%s님의 계좌가 개설되었습니다."%name)

# bank_open("에피노")

# 입력값이 없는 함수
# def hello_bank() :
#     print("안녕하세요. 에피노뱅크입니다.")

# hello_bank()

# 초기값도 미리 설정할 수 있습니다. 
# def bank_open(name, bank_num, open=True):
#     if open == True :
#         print("%s님의 계좌가 개설되었습니다."%name)
#         print("%s님의 계좌번호는 %s입니다."%(name, bank_num))
#     else :
#         print("%s님의 계좌 개설이 거부되었습니다."%name)

# bank_open("에피노", "010-1111-1111")

# lambda 함수
# def add(a,b):
#     return a+b

# print(add(1,2))

# add = lambda a,b : a+b # 함수와 똑같은 역할을 한다
# print(add(1,2))

# list1 = [lambda a,b :a+b, lambda a,b : a/b] #리스트에 추가가 가능하다. def같은 함수는 리스트에 추가가 불가능
# print(list1[1](2,1))


