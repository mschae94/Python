#while 문을 통해 무한반복을 하다가
#커피 10잔이 다 떨어지면, 반복을 종료해보자!
coffee = 3
while True:
    money = int(input("돈을 넣어 주세요:"))
    if money == 300:
        print("커피를 받으세요")
        coffee -= 1
    elif money >300:
        print("커피를 받으세요")
        print("거스름돈은 %d원 입니다" % (money -300))
        coffee -= 1
    elif coffee ==0:
        print("커피가 다 떨어졌습니다." )
        break
    else:
        print("돈이 부족합니다")
    if not coffee:
        print("커피가 다 떨어졌습니다.")
        break