#1번
# 변수명 : station / bus_num / min
# 서울역행 207버스가 7분 후 도착합니다.
#인천공항행 405번 버스가 3분 후 도착합니다.

station = '서울역'
bus_num = 207
min = 7
print(station+"행" + str(bus_num)+"버스가" +str(min)+"분 후 도착합니다.")

station = '인천공항'
bus_num = 405
min = 3
print(station+"행" + str(bus_num)+"버스가" +str(min)+"분 후 도착합니다.")

#2번
#질문에 대한 답을 Ture/False로 나타내기
# 질문 : 인천공항행 버스는 잠시 후에 도착하나요? (5분보다 적으면 잠시후)
soon_arrive = min <=5
print(station+"행 버스는 잠시 후 도착합니까?" + str(soon_arrive))


#3번
#위에서 나타낸 변수의 값과 변수의 데이터 타입을 나타내시오.

print("station 값 : " + station + "\n" + "station 타입 : " + str(type(station)) )
print("bus_num 값 : " + str(bus_num) + "\n" + "bus_num 타입 : " + str(type(bus_num)) )
print("min 값 : " + str(min) + "\n" + "station 타입 : " + str(type(min)) )
print("soon_arrive 값 : " + str(soon_arrive) + "\n" + "station 타입 : " + str(type(soon_arrive)) )

#출력 
# 서울역행207버스가7분 후 도착합니다.
#인천공항행405버스가3분 후 도착합니다.
#인천공항행 버스는 잠시 후 도착합니까?True
#station 값 : 인천공항
#station 타입 : <class 'str'>
#bus_num 값 : 405
#bus_num 타입 : <class 'int'>
#min 값 : 3
#station 타입 : <class 'int'>
#soon_arrive 값 : True
#station 타입 : <class 'bool'>
