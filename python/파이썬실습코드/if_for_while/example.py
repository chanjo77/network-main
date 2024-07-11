#예제

num_list = [1,5,3,19,7,0,40,15,41] 

# 1조건 리스트에 20,37,23을 추가하세요.
# 2조건 리스트를 정렬하세요.
# 3조건 리스트에서 홀수와 짝수를 서로 다른 리스트에 포함시키세요.
# 출력문 
# 리스트에서 홀수는 []입니다.
# 리스트에서 짝수는 []입니다.

# 1조건
num_list.extend([20,37,23])
print(num_list)
# num_list.append(20)
# num_list.append(37)
# num_list.append(23)
# num_list += [20,37,23]

# 조건2
num_list.sort()
print(num_list)

# 조건 3
i = 0
even_num = []
odd_num = []

while i < len(num_list):
    if num_list[i] % 2 == 1 :
        odd_num.append(num_list[i])
        i+=1
    elif num_list[i] == 0 :
        print("홀수도 짝수도 아닌 0입니다.")
        i+=1
    elif num_list[i] % 2 == 0 :
        even_num.append(num_list[i])
        i+=1 

# 출력문
print("리스트에서 홀수는" + str(odd_num) + "입니다.")
print("리스트에서 짝수는" + str(even_num) + "입니다.")


# 예제 2
# 다음과 같이 별을 찍으세요.

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********

for i in range(1,9):
    print("*"*(i))