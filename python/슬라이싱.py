# 예제
# 에피노 레일에서 새로운 기차를 발명해서 이름을 지으려고합니다.
# 다음 조건에 맞춰 이름을 지어주세요.

# 조건 1 : EFFINO에서 앞에 3글자를 사용
# 슬라이싱 , index
# 조건 2 : EFFINO에서 F의 갯수 사용
# count
# 조건 3 : EFFINO의 총 글자 갯수를 사용
# len
# 조건 4 : 만들어진 글자에서 BUS를 붙힌 후에 BUS를 TRAIN으로 변경해주세요.
# replace
# 조건 5 : 만들어진 이름에서 TRAIN만 소문자로 변경해주세요.
# lower replace

# 출력문은 포맷을 사용해서 출력해주세요.
# "EFFINO레일의 새로운 기차 이름은 EFF26train입니다." 

# 조건1 
name = "EFFINO"
new_Name = name[:name.index('I')]
print(new_Name)

# 조건2
new_Name = new_Name + str(name.count("F"))
print(new_Name)

# 조건3
new_Name = new_Name + str(len(name))
print(new_Name)

# 조건4
new_Name = new_Name + "BUS"
print(new_Name)
new_Name = new_Name.replace("BUS", "TRAIN")
print(new_Name)

# 조건 5
new_Name = new_Name.replace("TRAIN", new_Name[5:].lower())
print(new_Name)

# 출력문
print("{}레일의 새로운 기차 이름은 {}입니다".format(name, new_Name))

#출력값
# EFF
# EFF2
# EFF26
# EFF26BUS
# EFF26TRAIN
# EFF26train
# EFFINO레일의 새로운 기차 이름은 EFF26train입니다