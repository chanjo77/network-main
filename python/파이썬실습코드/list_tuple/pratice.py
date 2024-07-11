# 리스트
# print(list1)
# print(list1[0])
# print(list1[1] + list1[3])

# 리스트 슬라이싱
# print(list1[0:1])
# print(list1[0:4:2])

# 리스트 다중 리스트
# list1 = [1,2,3,4,5,[1,2,3,4,5,[1,2,3,4,5]]]
# print(list1[5][0])
# print(list1[5][5][0])

# 리스트 연산과 함수
# print(len(list1))
# # print(list1 + list1)
# # print(list1 * 2)
# print( 1 in list1)
# print( 7 not in list1)
# print(min(list1))
# print(max(list1))

# 함수
list1 = [1,2,3,4,5]


# list1.append(6)
# print(list1)
# list1.insert(2, 7)
# print(list1)
# list1.extend([6,7,8,9,0])
# list1 += [6,7,8,9,0]
# list1.pop(0)
# print(list1)
# print(list1.pop(0))
# print(list1)
# list1.remove(4)
# list1.clear()
# print(list1.count(3))
# list1.extend([1,2,3,4,5])
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)

# 튜플
# 인덱싱, 슬라이싱, 더하기 ,곱하기
# tuple1 = 1,2,3,4
# tuple2 = ('a', 'b', 'c', 'd')

# # 튜플 더하고 곱하기
# new_tuple = tuple1 + tuple2
# print(new_tuple)
# # new_tuple = (1, 2, 3, 4, 'a', 'b', 'c', 'd')
# print(tuple2*3)
# print(len(new_tuple))
# print(new_tuple[0])
# print(new_tuple[:3])

# 집합 자료형
# set이라는 것을 사용합니다.
# set 동일한 값은 하나로 취급합니다. (중복된값)
# set1 = set("hello hellen")
# print(set1)
# list1 = list(set1)
# print(list1)
# 리스트로 변환을 해서 인덱싱이나 슬라이싱을 할 수 있죠.

# 교집합 / 합집합 / 차집합
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])

# 합집합을 구하는 공식
print(set1 | set2)
print(set1.union(set2))

# 차집합을 구하는 공식
print( set1 - set2)
print( set1.difference(set2))

# 교집합을 구하는 공식
print( set1 & set2)
print( set1.intersection(set2))

# 집합 자료형의 함수
set1.add(5)
print(set1)
set2.update([1,2])
print(set2)
set1.remove(5)
print(set1)

