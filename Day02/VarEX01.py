#변수 (Varrable)

"""
1. 변수란?
-데이터를 담을 수있는 상자와 같다.

2. 변수의 사용
    변수명 = 변수에 저장할 값
    num = 10
    num = "안녕"
    num = 'a'
    num = 1.3
    cf) 다른 프로그램이 언어와 달리 파이썬은 변수의 자료형을 쓸 필요가없다.
        파이썬은 변수에 저장된 값을 판단하여 자료형을 알아낸다.

3. 프로그래밍에서는 등로(=)를
    대입연산자 또는 할당연산자 라고 한다.
    오른쪽의 값을 왼쪽의 변수에 "대입" 한다는 의미다.

"""
line = "==================================="
print(line)
#정수 : int(Integer)
num1 = 10
print(type(num1))
#실수 : float
num2 = 2.32
print(type(num2))

#문재 : str
char1 = 'c'
print(type(char1))

str1 = "방가워요"
print(type(str1))

#문제 1) 삼각형과 사각형의 면적을 구하는 공식을 작성해보세요
#길이 = 20 , 높이 = 10

(20*10)/2
20*10

length = 20
height = 10

triArea = ( length * height ) / 2
recArea = length * height
print(line)
print("삼각형의 면적: %d" % triArea)
print("사각형의 면적: %d" % recArea)
print(line)
x = 10
y = 5
#문제 2) [출력] 더하기 : 3 + 2 = 5  , 빼기 , 곱하기 , 나누기
print("더하기 : %d + %d = %d" %(x , y , x + y))
print(line)



