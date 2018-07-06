import random #랜덤모듈

rnd = random.randint(0,1)# 랜덤숫자 저장0~1
#print(rnd)#테스트

count = 0 # 0 이나 1을 세는거!!
turn = 0 # 반복횟수 동전을 몇번던질꺼냐
while(turn < 1000000): #반복문
    turn = turn +1 # 반복횟수 증가
    rnd = random.randint(0,1)  #동전던지기
    if rnd ==0: #동전이 앞이면 체크
        count = count + 1


print(count)



