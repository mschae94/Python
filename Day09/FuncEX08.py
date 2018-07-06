# 리턴값의 유형

def calc(a , b):
    return a + b #함수 종료
    return a - b
result = calc(10 ,5)
print(result)

def calc(a, b):
    return a+b , a - b

result = calc( 10 , 6)
print(result)

sum , sub = calc(10 , 6)
print (sum)
print (sub)


