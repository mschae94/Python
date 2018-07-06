# Exam 04
# 아래의 코드 출력이 다음과 같이 나오도록 완성해보자.
# 현재의 value  = "42"

class FirstClass:

    def setData(self, value):
        self.data = value

    def display(self):
        print(self.data)

class SecondClass(FirstClass):

    #
    #

z = SecondClass()
z.setData(42)
z.display()


