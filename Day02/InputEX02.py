"""
num1 = int(input("첫번째 정수: "))
num2 = input("두번째 정수: ")
num3 = input("세번째 정수: ")
print(int(num2) + int(num3))
"""

name = input("이름을 입력하세요: ")
korScore = int(input("국어점수는: ")) #카멜식표기법
mathScore = int(input("수학점수는: "))
engScore = int(input("영어점수는: "))
total = korScore + mathScore + engScore
avr = total / 3
print("%s 님의 총점은 %d점이고 , 평균은 %.1f 입니다"  %(name , total  , avr ))


