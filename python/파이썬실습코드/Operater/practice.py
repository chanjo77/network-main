# 연산자

# print ( 1 + 1) # 2
# print ( 2 - 1 ) # 1
# print ( 5 * 3) # 15
# print (int( 4 / 2)) # 2

# print ( 2**2 ) # 2^2 = 4
# print ( 3**4 ) # 3^4 = 81
# print ( 7%5 ) # 나머지 : 2
# print ( 5//2 ) # 몫 : 2
# print ( 5%2 ) # 나머지 : 1 

# print ( 1 > 3 ) # False 
# print ( 1 <= 6) # True
# print ( 7==7 ) # True
# print ( 7!=7) # False

# 논리 연산
# print (1>2) and (2>3) # False --> and는 두 연산자가 모두 True인 경우에만 True 보여줌
# print (1<2) and (2<3)
# print (1>2 & 2>3) # 두 연산자 간의 and 연산 진행
# print (1<2) or (2<3) # True --> or 연산은 두 연산자가 모두 false 경우에만 false 값을 보여줌
# print (1<2) or (2>3) 
# print (1<2 | 2>3) # 두 연산자 간의 or 연산 진행

# 맴버 연산
# print ( 1 in (1,2,3,4)) # True ==> 왼쪽의 값이 오른쪽의 피연산자의 맴버에 값에 있을 경우 True
# print ( 1 not in (2,3,4,5)) # True ==> " 없을 경우 True

# # 간단한 연산
# print ( 3 + 4 + 5 ) 
# print ( 3+ 4 * 5)
# print ( (3+4) * 5 )
# number = (3+4)*5
# print (number)
# number = number + 1
# print (number) # 36
# number = number + 1
# print (number) # 37
# number += 1
# print (number)#38
# number *= 2
# print (number)

# 최소/절대/최대/반올림
# print (min(7,9)) # 7
# print (max(7,9)) # 9
# print (abs(-7)) # 7
# print (round(3.14)) # 3
# print (round(3.91)) # 4

# 랜덤한 값 구하기
from random import *

print (random()) # 0.0부터 1.0미만의 실수가 나오게됩니다.
#정수로 바꾸는 방법
print (int(random()*10))
# 1~10까지의 랜덤한 숫자를 구하고 싶다!
print (int(random()*10)+1) # 1부터 10까지의 랜덤한 숫자를 나타냅니다.
print (randint(1,10)) # 1부터 10이하의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.
print (randrange(1,10)) # 1부터 10미만의 랜덤한 숫자가 나타납니다.

