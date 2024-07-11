
# 주석이란?
# - 코드를 설명하는 설명문 같은 것! 협업에 굉장히 중요하게 쓰임.

# 한줄 주석을 나타냅니다.

'''
작은따옴표 3개는 
여러줄 주석이 가능해요!
쭉쭉
무한대로 할수 있어요
'''

# 엇 이거 주석이 필요해
# 이것도 주석이 필요해!

# 문자형 자료형 나타내기
# print ("Hello python")
# print ("안녕 파이썬")
# print ("안녕"*7)

# 익스케이프 문자
# print ("안녕하세요.")
# print ('저는 홍길동입니다.')
# print ('안녕하세요. \n저는 홍길동입니다.')
# print ('김밥 : 3000원 \t 방문포장 : 2000원')
# print ('여자들은 떡볶이를 좋아해.\r남자분들은')

# 숫자형 자료형
# 정수형
# print(7)
# print(-7)

# # 실수형
# print(3.14)
# print(-3.14)

# # 숫자를 표현하는 여러가지 방법
# print(10000000)
# print(3+4)
# print(-3+-4)

# boolean 자료형
# 참/ 거짓을 나타내는 자료형

# print ( 3 > 4 ) # 거짓 false
# print ( 3 < 4) # 참 True
# print (not(3>4)) # 거짓 --> 부정 --> 참

# 변수
# 공간을 주고, 그 공간 안에 값을 집어 넣어주는 것을 의미

# name = '홍길동'
# print (name)
# name1, name2 = '파이썬', '학생'
# print (name1, name2)
# name1 = name2 = "자바"
# print (name1, name2)

# print ("철수는 남자아이이고, 17살 입니다.")
# name = "철수"
# gender = "남자"
# age = 17
# is_highschool= age>=17

# print (name + "는 " + gender +"아이이고, " + str(age) + "살 입니다.")
# print (name, "는", gender, "아이이고", str(age), "살입니다.")
# print (name + "는 " + gender +"아이이고, " + str(age) + "살 입니다."+"\n"+ name + "는 고등학생입니까?" + str(is_highschool))
# print (name + "는 " + gender +"아이이고, " + str(age) + "살 입니다."+"\n"+ name + "는 고등학생입니까?" + str(is_highschool))

# 데이터 타입 알아보기
name = "에피노"
gender = "여자"
age = 15
num = 17.1
is_highschool = age>=17
print(type(name))
print(type(age))
print(type(is_highschool))
print(type(num))

