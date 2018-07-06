#다중상속 #문제!
class Person1:
    def python(self):
        print("파이선")
    def a(self):
        print("Person1.a")
class Person2:
    def C(self):
        print("c언어")
    def a(self):
        print("Person2.a")
class Person3:
    def JAVA(self):
        print("JAVA")
    def a(self):
        print("Person3.a")
class Student(Person3 ,Person2 , Person1): # 다중상속
    pass
student1 = Student()
student1.C()
student1.JAVA()
student1.python()
student1.a()