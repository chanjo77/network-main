# 예제1
# 두개의 숫자를 입력받아 더하기,빼기,나누기,곱하기
# 를 출력하는 프로그램을 제작하세요.
# 첫 입력 : a
# 두번째 입력 : b 

# def num_oper (a,b) :
#     print("더하기를 진행합니다.")
#     print("{} + {} = {}".format(a, b, a+b))
#     print("빼기를 진행합니다.")
#     print("{} - {} = {}".format(a, b, a-b))
#     print("나누기를 진행합니다.")
#     print("{} / {} = {}".format(a, b, a/b))
#     print("곱하기를 진행합니다.")
#     print("{} * {} = {}".format(a, b, a*b))

# a = int(input("정수 입력 : "))
# b = int(input("정수 입력 : "))

# num_oper(a, b)


# 예제 2
# 학교의 학생의 이름을 추가하고 삭제하는 프로그램을 제작하세요.
# 조건 1 학생의 이름은 프로그램 종료 전까지 계속 추가할 수 잇어야한다.
# 조건 2 프로그램 종료 시 맨마지막에 추가한 모든 학생의 이름을 출력한다.
# 조건 3 다른 숫자를 입력하면 잘못입력하였다고 알려주고 다시 입력 받는다.
# 조건 4 삭제하려는 학생이 이름이 없을 시에는 등록되지 않았다고 알려주고 다시 처음부터
#        프로그램을 시작한다.
# 조건 5 프로그램 시작과 종료를 알려준다.

def stu_upd () :
    stu_list=[]
    print("학생 등록 프로그램을 시작합니다.")
    while True :
        print("1. 학생 등록\n2. 학생 삭제\n3. 종료")
        input_num = int(input("프로그램할 번호 입력 : "))
        if input_num == 1 :
            print("학생을 등록하겠습니다.")
            input_name = input("학생의 이름을 입력해주세요. : ")
            stu_list.append(input_name)
            print("등록이 완료되었습니다.")
        elif input_num == 2 :
            print("학생을 삭제하겠습니다.")
            input_name = input("학생의 이름을 입력해주세요. : ")
            if input_name in stu_list :
                print("학생 삭제를 완료 하였습니다.")
                stu_list.remove(input_name)
            else :
                print("잘못입력 하였습니다.")
        elif input_num == 3 :
            print("학생 등록 프로그램을 종료 하겠습니다.")
            print("등록된 학생 : {}".format(stu_list))
            break
        else :
            print("잘못입력하셨습니다. 다시 입력해주세요.")

stu_upd()



#출력값
# 학생 등록 프로그램을 시작합니다.
# 1. 학생 등록
# 2. 학생 삭제
# 3. 종료
# 프로그램할 번호 입력 :
