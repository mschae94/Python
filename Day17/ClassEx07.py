"""
# static 메서드

1. 클래스 안에서 self 가 아닌 함수를 만들기위해서 사용
2. 따라서 매서드를 정의할때 self 매개변수를 기술하지 않는다.
3. 메서드 정의 위에 데코레이터 를 기술한다.
4. 객체를 생성하지않고도 매서드를 호출할수있다.
5. 클래스 이름과 객체 이름으로 모두 실행할수있다.

"""
class Payment:

    counter = 0 # 객체 생성 숫자세기
    discount = 0.5 #전체적으로 적용되는 내용
    def __init__(self , price , count):
        self.price = price
        self.count = count
        Payment.counter += 1
    def calc(self):
        self.pay = self.price * self.count
        self.dcPay = self.pay -(self.pay * Payment.discount)
    def display(self):
        print(str(Payment.counter)  + "번째 제품입니다.")
        print("정가 : " , self.price)
        print("수량 : " ,self.count)
        print("정상가격 :" , self.pay)
        print("할인가격 : " , int(self.dcPay))

    @staticmethod
    def message():
        print("어서오세요")
        print("할인행사 중입니다")

    @classmethod
    def dcUpdate(cls , value):
        while(value >= 1) or (value <= 0):
            value = float(input("할인율을 다시 입력해주세요"))
        cls.discount = value

Payment.dcUpdate(1.5)
Payment.message() # 객체 생성이 되지않았는데도 쓸수있다.
                  # 스태틱영역에 생성됨 #프로그램이 시작되자마자

obj = Payment(10000, 5)
obj.calc()
obj.display()
#obj.message()

#제목학원 : 한탕하고 한국을 뜨겠다

#샴푸 : 10000000000


