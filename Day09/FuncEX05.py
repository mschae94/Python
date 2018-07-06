#사칙연산 프로그램(2단계)
def result(num1 , num2):
    print("덧셈: %d" %(num1 + num2))
    print("뺄셈: %d" % (num1 - num2))
    print("곱셈: %d" %(num1 * num2))
    #print("나눗셈: %.1f" %(num1 / num2))

def calc(num1 , num2):
    result(num1 , num2)
    if num2 != 0:
        print("나눗셈: %.1f" % (num1 / num2))
    else:
        print("나눗셈: 0으로 나눌 수 없습니다.")

###################################################
calc(10 , 0)
