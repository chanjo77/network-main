# 예제

# 변수명 : station / bus_num / min

# 예제 1번
# 다음 문장을 위 변수명을 사용하여 완성해 보세요.
# 서울역행 207버스가 7분 후 도착합니다.
# 인천공항행 405번 버스가 3분 후 도착합니다.
station = '서울역'
bus_num = 207
min = 7
print(station + "행 " + str(bus_num) + "버스가 " + str(min) + "분 후 도착합니다.")
station = '인천공항'
bus_num = 405
min = 3
print(station + "행 " + str(bus_num) + "버스가 " + str(min) + "분 후 도착합니다.")

# 예제 2번
# 질문에 대한 답을 True/False로 나타내보세요.
# 질문 : 인천공행행 버스는 잠시 후에 도착하나요? (도착시간이 5분보다 적으면 잠시후 도착이라고 함.)
soon_arrive = min <= 5
print(station+"행 버스는 잠시 후 도착합니까?" + str(soon_arrive))

# 예제 3번
# 위에서 나타낸 변수의 값과 변수의 데이터 타입을 나타내시오. (사용하는 변수는 마지막 변수와 값을 사용)
print("station 값 : " + station + "\n" + "station 타입 : " + str(type(station)))
print("bus_num 값 : " + str(bus_num) + "\n" + "bus_num 타입 : " + str(type(bus_num)))
print("min 값 : " + str(min) + "\n" + "min 타입 : " + str(type(min)))
print("soon_arrive 값 : " + str(soon_arrive) + "\n" + "soon_arrive 타입 : " + str(type(soon_arrive)))

