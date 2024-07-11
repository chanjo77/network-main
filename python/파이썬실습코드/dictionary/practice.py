# dictonary 사전

# # json 형식
# api = {
#     name:"에피노"
#     성별 : "남자"
#     전화번호 : "010-1111-1111"
#     회원가입 일자 : "2021-12-01"
# }

# 함수
# dic = {'a' : 1, 'b' : 2 , 'c': 3 }
# print(dic)
# print(dic['a'])

# dic = {'a' : [1,2], 'b' : 2 ,'b' : 3}
# print(dic)
# print(dic['b'])


# # update
# dic.update({'f' : 5})
# print(dic)

# # del (삭제)
# del dic['f']
# print(dic)

#fromkeys
# list1 = ['a','b','c','d']
# tuple1 = 1,2,3,4
# dic1 = {}.fromkeys(list1)
# dic2 = {}.fromkeys(list1, 1)
# dic3 = {}.fromkeys(tuple1)
# dic4 = {}.fromkeys(tuple1, 1)

# print(dic1)
# print(dic2)
# print(dic3)
# print(dic4)

# keys / values / items / get
dic = {'a' : 1, 'b' : 2 , 'c':3 , 'd' : 4}
# print(dic.keys())
# print(dic.values())s
# print(dic.items()) # 키와 값을 튜플형식으로 반환을 합니다.
# print(dic.get('a'))
# print(dic.get('f'))
# print(dic.get('f', "값이 존재하지 않습니다."))

# pop/popitem
# print(dic.pop('a'))
# print(dic)
# print(dic.popitem()) # 맨마지막 키 밸류만 튜플로 보여주고 삭제
# print(dic)

# 반복문을 통한 응용
# for k in dic.keys():
#     print("키 : " + k)
# for v in dic.values() :
#     print("값 : " + str(v))
# for k,v in dic.items():
#     print("키 : "+k )
#     print("값 : " + str(v))