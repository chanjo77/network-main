# if문
# day = "금요일"
# if day == "공휴일" :
#     print("출근 안해")
# elif day == "금요일" :
#     print("오전에만 일합시다.")
# else :
#     print("출근하는 날")

# if 기본 유형
# if 조건문 :
#     if 조건문 :
#         실행명령문
#         if 조건문 :
#             실행명령문
#     elif :
#     else :
# elif 조건문 :
#     실행명령문
# else :
#     실행명령문

# for 기본형식
# for 변수 in 리스트, 튜플, 문자열 :
#     실행 명령문
# for i in [1,2,3,4] :
#     print(i)
# room = [101, 102, 103, 104, 105, 201, 202, 203, 204, 205]

# for i in room :
#     print("{}호가 배정 되었습니다.".format(i))

# for range
# for room in range(100,111) :
#     print("%d호가 배정되었습니다."%room)
# print("\n")
# for room in range(100,111,2) :
#     print("%d호가 배정되었습니다."%room)

# # for if
# score = [90, 60, 70, 30, 40, 100]
# num = 0
# for sco in score :
#     num += 1
#     if sco == 100 :
#         print("{}번 시험자는 100점으로 합격하였습니다. 장학생 대상자입니다.".format(num))
#     elif sco >= 60 :
#         print("{}번 시험자는 합격입니다. 축하드립니다.".format(num))
#     else :
#         print("{}번 시험자는 불합격입니다.".format(num))

# 이중 포문
# for i in range(1,5) :
#     for j in range(1,5) :
#         print(" i : {}, j : {}".format(i,j))

# 구구단
# for i in range(2,10) :
#     print("-----{}단 시작!-----".format(i))
#     for j in range(1,10) :
#         print("{} X {} = {}".format(i, j, i*j))

# while문 기본 형식
# while 조건문 :
#     수행할 문장
#     수행할 문장
#     수행할 문장
#     수행할 문장
#     수행할 문장

# while문의 continue와 break사용하기
num = 0
leave = [6, 17, 20, 30]
while num < 30 :
    num += 1
    if num in leave :
        continue
    elif num == 18 :
        print("죄송합니다. 재료가 모두 소진되었습니다.")
        break
    print("{}번 손님 입장해주세요!".format(num))
