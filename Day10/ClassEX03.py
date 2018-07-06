"""
__init__ (매서드)함수(생성자 , initializer)
1) 클래스가 인스턴스화(객체화) 될때 호출되는 매서드이다.
2) 객체를 생성할때 호출된다 하여 생성자라고 한다
3) 보통 초기화 작업할때 사용된다
4) 매서드 : __init__ (언더바 2개)

"""
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def say(self):
        print("이름: %s" % self.name)

p1 = Person("홍길동" , 25)
#p1.say() # 함수는 직접호출이 원칙
class Tv:
    color = ""
    brand = ""
    channel = 0
    def info(self):
        print("색상:  %s" % self.color)
        print("브랜드: %s" % self.brand)
        print("채널:  %d" % self.channel)
tv1 = Tv()
tv1.color = "black"
tv1.brand = "LG"
tv1.channel = 5
tv1.info()
class Tv2:
    color = "black"
    brand = ""
    channel = 0
    def __init__(self , color , brand , channel):

        self.color = color
        self.brand = brand
        self.channel = channel
    def info(self):
        print("색상   :  %s" % self.color )
        print("브랜드 :  %s "% self.brand)
        print("채널 :    %d" % self.channel)

t2 = Tv2("yellow" , "samsung" , 7)
t2.info()
t2.color = "Red"
t2.info()
print(Tv2.color)
