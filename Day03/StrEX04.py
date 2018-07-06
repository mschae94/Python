#문자열 포맷팅

print("나는 사과 %d개를 먹었어요" % 10)
print("성공할 확률은 %d%% 입니다" % 99)

#포맷문자를 사용해서 문자의 정렬과 공백처리
print("%5s" % "hi")

#고급 문자열 포맷팅
# 1. 숫자 바로 대입하기
print("i ate {} ice cream".format(3))

# 2. 숫자 값을 가진 변수로 대입하기

print("i ate {} apples".format("five"))

# 3 . 두개 이상의 값을 넣기
day = 11
month = "9"

print("오늘은 {} 월 {} 일 입니다".format(month, day))








