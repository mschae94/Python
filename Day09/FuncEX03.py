line = "="*20
line1 = "============================="

#atm 비밀번호 //잔액조회 , 출금

# pw = int(input("비밀번호 입력: "))
# if pw == 1234:
#     print("로그인")
# else:
#     print("비밀번호를 확인해주세요")
# print(line)

# def pwCheck():
#     pw = int(input("비밀번호 입력: "))
#     if pw == 1234:
#         print("로그인")
#     else:
#         print("비밀번호를 확인해주세요")
# #문제1) 코리아은행 !! 비밀번호 체크 함수를 이용해서 완성해보세요.
# pwCheck()
# pwCheck()
# pwCheck()

#함수 2가지 씩 2가지 총 4가지
#1) 반환이 있다없다
#2) 매개변수가 있다없다
#함수는 자기역활이 끝나면 변수로 변한다.
###########################
def sum(a, b):
    result = a + b
    return result
a = sum(4, 5)
print(a)
############################
def show():
    return "Hello"
a = show()
print(a)
#############################
def sum( a , b ):
    print("%d와 %d의 합은 %d 입니다" %(a , b , a+b))
sum(10 , 20)
print(line)
#############################
def say():
    print("안녕하세요")
say()
print(line)









