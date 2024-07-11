# input
# a = int(input("정수 입력 : "))
# print("a의 값 : {}".format(a))
# print(type(a))

# 리스트를 만들어보기
# input_list = []

# for i in range(1,6) :
#     i += 1
#     val = input("정수 입력 : ")
#     input_list.append(val)

# print(input_list)

# input과 while문 사용해보기

# password = "0322"

# while True :
#     print("택배를 찾아가시려면 비밀번호를 입력해주세요.")
#     input_pass = input("비밀번호 입력 : ")
#     if input_pass == password :
#         print("보관함의 문이 열렸습니다. 택배를 가져가주세요.")
#         break
#     elif input_pass != password :
#         print("비밀번호가 틀렸습니다. 다시 입력해주세요.")

# 다양한 입출력
# print("에피노", "자바", "파이썬", sep="vs")
# print("뭘할래?" + "축구", "야구", "농구", sep = "vs", end="?")

# 오른쪽 정렬(rjust) 왼쪽 정렬(ljust)
# menu = {"김밥" : 3000, "순대" : 2000, "라면" :4500 }
# for menu1, pey in menu.items():
#     # print(menu1,pey)
#     print(menu1.ljust(5), str(pey).rjust(10), sep=":")

# # zfill 
# num = 0
# while num <= 10 :
#     print("대기번호 : "+ str(num).zfill(5))
#     num += 1

# 3자리마다 콤마 1,000원
# print("내월급 : {0:,}원".format(2000000))
# print("내자산 : {0:+,}원".format(2000000))

# 정렬
# print("{0: >5}".format(10))
# print("{0: <5}".format(10))
# print("{0: >+5}".format(10))
# print("{0: >+5}".format(-10))

# # 빈칸채우기
# print("{0:*>10}".format(10))
# print("{0:*<10}".format(10))

