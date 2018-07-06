# Exam06

"""
아래 출력결과를 통해 코드를 완성해보자.

하얀 고양이:야옹!
검은 고양이:야옹!
강아지:멍멍!
"""

class Animal:
    #
    #
    def talk(self):
        return "없음"

class Cat(Animal):
    #
        return "야옹"

class Dog(Animal):
    #
        return "멍멍!"

animals = [Cat("하얀 고양이"),
           Cat("검은 고양이"),
           Dog("강아지")]

for i in animals:
    print(i.name + ": " + i.talk())

