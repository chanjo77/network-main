# 문자열 표현하기
# sentence = "hello my name is python"
# print(sentence)
# sentence = "python is useful"
# print(sentence)
# sentence = 'python\'s favorite language is java'
# print(sentence)
# sentence='''hello my name is python
# python is useful
# python's favorite language is java'''
# print(sentence)

# 인덱싱
# word = "Python"
# print(word[0])
# print(word[3])
# print(word[-1])
# word = "2021-python"
# print(word[0:2])
# print(word[:4])
# print(word[4:])
# #print(word[이상:미만:간격])
# word = "1234567"
# print(word[::2])
# print(word[1:6:3]) #2,5

# 포맷
# a = "파이썬님의 무게는 70.5kg입니다."
# name = "파이썬"
# weight = 70.544
# print( name + "님의 무게는  "+ str(weight) +"kg입니다.")
# print("%s님의 무게는 %0.1fkg입니다"%(name, weight))
# # %d = 정수 %s = 문자 %f = 실수형을 의미합니다. 
# print("%s님의 무게는 %skg입니다."% (name,weight))
# print("{}님의 무게는 {:0.1f}kg 입니다.".format(name, weight))
# print("{name}님의 무게는 {weight}kg 입니다.".format(name="자바", weight=60.8))

# 문자열 관련 함수
# find, index, count, upper, lower, strip, replace, split, len
# word = 'apple'
# print(word.find('p')) # 단어를 쭉 보다가 제일먼저 발견된 인덱스의 번호를 출력 1
# print(word.count('p')) # 단어를 보다가 p라는 것이 값에 몇개 있는지 출력 해라.
# print(word.index('p')) # 단어를 쭉 보다가 제일먼저 발견된 인덱스의 번호를 출력 1 # find
# print(len(word)) # 값의 길이를 나타내주는 것
# print(word.upper()) # 소문자를 대문자로
# print(word[0].upper()) # 0번째 인덱스의 문자를 대문자로 바꿔라.
# word = '    APPLE    '
# print(word.lower()) # 대문자를 소문자로 바꿔라
# print(word.strip()) # 공백 삭제
# word = 'my name is python'
# print(word.replace('python', 'effino')) # 파이썬을 에피노로 바꿔라 
# print(word.split()) # 문자열을 단어 단위로 쪼개서 보여줍니다. 
