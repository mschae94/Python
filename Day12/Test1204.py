class Animal:
    def __init__(self, name , age , color):
        self.name = name
        self.age = age
        self.color = color
    def info(self):
        print("이름 : " , self.name)
        print("나이 : " , self.age)
        print("색깔 : " , self.color)
    def play(self):
        print("놀기")
    def sleep(self):
        print("잠자기")
class Dog(Animal):
    def sleep(self):
        print("쿨쿨자기")
    def walk(self):
        print("산책가기")
class Cat(Animal):
    pass
dog = Dog("해피" , 3 , "갈색")
dog.info()
dog.play()
dog.sleep()
cat = Cat("나비" , 2 , "흰색")
cat.info()

