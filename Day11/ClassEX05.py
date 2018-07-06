#공장 , 붕어빵틀 ,
a = int()
a = list()
a = float()
a = str()
class Payment:
    counter = 0 # 클래스변수(횟수)
    def __init__(self , price , count):
        self.price = price # 객체 변수
        self.count = count
        Payment.counter += 1
    def Init(self , price , count):
        self.price  = price
        self.count = count
        Payment.counter += 1
    def calc(self):
        self.total = self.price * self.count
    def display(self):
        print(str(Payment.counter) + "번째 손님입니다")
        print("정가 : " , self.price)
        print("수량 : " , self.count)
        print("금액 : " , self.total)
#클래스 = 속성 + 기능   (변수 + 함수)
# obj1 = Payment()
# obj1.Init(10000, 3)
obj1 = Payment(10000 , 3)
obj1.calc()
obj1.Discount(0.3)
obj1.display()
#문제 1번 ) 할인기능 가격을 할인해주는 함수를 만들어보세요
#문제 2번 ) 2 + 1 행사기능 함수 만들어보세요  과제!!

