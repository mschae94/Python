class Cal:

    def __init__(self, a , b): # 매직함수
        self.a = a
        self.b = b

    def plus(self):
        result = self.a + self.b
        return result

cal = Cal(19 , 9)
print(cal.plus())


