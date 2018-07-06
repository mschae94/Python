# while 문

"""
1.구조
    while 조건문:
        수행문1
        수행문2
2. 조건문이 참일 동안 while문 안의 문장들이 반복해서 수행된다.
3. 반복횟수를 당장에 모르거나 특정한 조건으로 멈추고 싶을때 사용한다.
    조건문사용을 주의해야한다
"""
#10번찍어서 안넘아가는 나무는 없다!
orderCount = 0
turn = 3
while orderCount < turn:
    orderCount = orderCount + 1
    print("*** 홍콩반점 ***\n"
          "1. 쟁반짜장 : 10000원\n"
          "2. 간짜장   :  5000\n"
          "3. 불짱뽕   :  8000\n"
          "4. 볶음밥   :  6000\n")
    number = int(input("주문할번호를 입력해주세요: "))
    if number == 1:
        print("쟁반짜장")
    elif number == 2:
        print("간짜장")
    elif number == 3:
        print("불짬뽕")
    elif number == 4:
        print("볶음밥")
    print("%d 회 주문받았습니다" % orderCount)

#문제 1 ) 홍콩반점 주문 5번 받기!!! 주문횟수 출력하세요
# 주문을 1번 2번 3번 4번 5번 받았습니다!!!!

#문제 2) 주문한 음식의 합계를 출력해주세요!!!