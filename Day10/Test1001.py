def pwCheck():
    count = 0
    while count <= 2:
        pw = int(input("비밀번호"))
        if pw == 1234:
            print("로그인")
        else:
            print("비밀번호를 확인해주세요")
        count += 1
#pwCheck()

def EvenOdd(num):
    if num % 2 ==0:
        return "짝수"
    elif num % 2 == 1:
        return "홀수"
#num = int(input("정수1개"))

#result = EvenOdd(num)
#print(result)

#문제 3 ) 값을 3개 입력받고 가장큰수를 출력하는함수를
#만들어보세요
def Max(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else :
        return c
print(Max(10 ,200 , 30))

