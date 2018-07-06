#변수의 형변환
"""
1.변수의 형변환이란 , 변수의 자료형을 변환시키는것을 의미한다
2. 방법 : 변환할 자료형(값)
"""
"""
x = 1.5
print(type(x))
print(x) # 1.5
y = int(x)
print(y) #1  값의 손실이 발생한다

#변수의 형변환은 문자열 을 숫자로 변환할때 , 많이 사용한다.
"""
strNum1 = "3"
strNum2 = "7"

result = strNum1 + strNum2
print(result)

result = int(strNum1) + int(strNum2)
print(result)

