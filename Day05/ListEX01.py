#리스트 자료형
"""
1. 리스트란?
- 여러개의 대상을 함께 묶어서 저장하거나 모아두는것을 의미한다.
예) 운동 = ['수영' , '축구' , '배구' , '야구']
2. 리스트 만드는 법과 사용법
리스트명 = [요소1 , 요소2 , 요소3......]
3. 리스트의 특징
리스트의 크기는 제한이 없다.
리스트안에는 어떠한 자료형도 포함된다.
"""
#5명의 학생 점수를 저장할려고한다.
score1 = 100
score2 = 30
score3 = 80
score4 = 50
score5 = 10
score =[100, 40, 55 , 85, 97]
#리스트안에 어떠한 자료형도 포함시킬수있다
a = [] #비어있는 리스트[]
b = [1,2,3]
c = ['python', 'c언어', 'java']
d = [1 ,2 , 'python' , "c언어"]
e = [1, 2, ['python' , 'c언어' , 'java']] #리스트 안에 리스트를 포함
print(a)
print(b)
print(c)
print(d)
print(e)
pocket = ['paper' , 'cellphone', 'money']
a = 10
b = "asdasd"
if 'money' in pocket:
    print("택시타자")
else:
    print("걸어가자")
pocket2 = ['paper' , 'card' , 'cellphone']

if 'money' not in pocket2 and 'card':
    print("걸어가자")
else :
    print("택시타자")
#변수 if while


