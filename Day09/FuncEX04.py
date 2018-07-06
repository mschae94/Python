line = "----------"
num1 = 20
num2 = 30

def calc(num1 , num2):
    print("덧셈: %d" %(num1 + num2))
    print("뺄셈: %d" % (num1 - num2))
    print("곱셈: %d" %(num1 * num2))
    print("나눗셈: %.1f" %(num1 / num2))
#num1 = int(input("정수1"))
#num2 = int(input("정수2"))
#calc(num1 ,num2)
print(line)
def showMax(a , b):
    if a> b:
        print(a , "은 최대값")
    elif a ==b:
        print(a , "와" , b , "는 같다")
    else:
        print(b , "은 최대값")
showMax(10 , 20)
print(line)
