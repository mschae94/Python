class Parent:
    def __init__(self , fatherAge , motherAge): #3
        self.fatherAge = fatherAge
        self.motherAge = motherAge

    def parentMethod(self):
        print("아빠 나이 : " , self.fatherAge)
        print("엄마 나이 : " , self.motherAge)

class Child(Parent):
    def __init__(self , fatherAge , motherAge , myAge): # 1
        super().__init__(fatherAge , motherAge) #2
        self.myAge = myAge # 4
    def childMethod(self):
        super().parentMethod()
        print("나의 나이 : " , self.myAge)
c = Child(49 , 39 , 15)
c.childMethod()