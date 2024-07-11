print("hello python student")

def auto_oper (a,b) :
    print("더하기를 실행합니다.")
    print("{} + {} = {}".format(a, b, a+b))
    print("빼기를 진행합니다.")
    print("{} - {} = {}".format(a, b, a-b))
    print("나누기를 진행합니다.")
    print("{} / {} = {}".format(a, b, a/b))
    print("곱하기를 진행합니다.")
    print("{} X {} = {}".format(a, b, a*b))

a = int(input("정수 입력 : "))
b = int(input("정수 입력 : "))

 

auto_oper(a,b)

def input_stu ():
    stu_list=[]
    print("프로그램을 시작합니다.")
    while True :
        print("1. 학생 추가\n2. 학생 삭제\n3. 프로그램 종료")
        input_num = int(input("실행할 프로그램을 선택해주세요(정수입력) : "))
        if input_num == 1 :
            input_name = input("학생의 이름을 입력해주세요 : ")
            stu_list.append(input_name)
            print("등록완료 되었습니다.")
        elif input_num == 2 :
            input_del = input("삭제할 학생의 이름을 입력해주세요. : ")
            if input_del in stu_list :
                stu_list.remove(input_del)
                print("삭제 완료되었습니다.")
            else :
                print("등록된 학생이 아닙니다.")
        elif input_num == 3 :
            print("학생 등록 프로그램을 종료합니다.")
            print("등록된 학생 : {}".format(stu_list))
            break
        else :
            print("잘못입력하셨습니다. 다시 입력하여 주십시오.")
            continue

input_stu()