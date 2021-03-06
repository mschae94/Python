"""
* 제어문 : 프로그램의 흐름을 효율적으로 이용하기 위한 것
    0. 변수
    1. 조건문 : if 문
    2. 반복문 : for 문
* 조건문 if 문
    1) 조건문이란?
        -참과 거짓을 판단하는 문장을 의미한다.
        -주로 "비교연산자"와 함께 쓰인다.
    2) 구조
        if 조건문:
            #조건이 참일때
            실행할 문장1
            실행한 문장2
    3) 들여쓰기
        파이썬은 들여쓰기에 엄격하다!
        들여쓰기는 항상 같은깊이로

    4) 조건문 다음에 콜롬(:)을 잊지말자 !!


"""
"""
# case 1
score = int(input("점수를 입력하세요 :"))

if score >= 60:
    print("합격입니다")
    print("축하합니다")

print("점수: ", score)

# case 2
res = int(score / 60 ) # 59까지는 0 그이상은 1

# 1이면 true  ,  0 이면 false 

if res:
    print("합격입니다")
"""

# 리스트를 사용한 조건식
lst1 = []
lst2 = [2 , 3 , 4]

if not lst1:
    print("lst1 리스트가 비었습니다")

if not lst2:
    print("lst2 리스트가 비어있지않습니다")

if lst2:
    print("lst2 리스트가 비어있지않습니다")


# 문제 1) 점수를 입력받고 점수가 60 이하면
#  <= 연산자를 이용해서 불합격 을 출력해주세요

score1 = int(input("점수를 입력하세요 :"))

if score1 <= 59:
    print("불합격입니다")
    print("재도전하세요")

print("점수: ", score1)

