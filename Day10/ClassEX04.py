
#문제 1) Card 클래스 를 만들어보세요
#조건1)  width , height 이건         : 클래스 변수
#조건2)  kind , number  ( __init__ ) : 객체 변수
# 카드 스패이드 5 , 다이아  7 을 만들어보세요
class Card:
    width = 100
    height = 200
    # kind = ""
    # number = 0
    def __init__(self , kind , number):
        self.kind = kind
        self.number = number
c1 = Card("space" , 5)
c2 = Card("heart" , 7)
print("c1 의 종류 %s"  % c1.kind)
print("c1 의 숫자 %d"  % c1.number)
print("c1 의 가로 %d"  % c1.width)
print("c1 의 세로 %d"  % c1.height)
print("c2 의 종류 %s"  % c2.kind)
print("c2 의 숫자 %d"  % c2.number)
print("c2 의 가로 %d"  % c2.width)
print("c2 의 세로 %d"  % c2.height)
Card.width = 200
Card.height = 500
print("c1 의 종류 %s"  % c1.kind)
print("c1 의 숫자 %d"  % c1.number)
print("c1 의 가로 %d"  % c1.width)
print("c1 의 세로 %d"  % c1.height)
print("c2 의 종류 %s"  % c2.kind)
print("c2 의 숫자 %d"  % c2.number)
print("c2 의 가로 %d"  % c2.width)
print("c2 의 세로 %d"  % c2.height)
#섯다 추후 과제~~ 1~10 두종
