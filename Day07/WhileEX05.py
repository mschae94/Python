#랜덤!!!!
#컴터와 숫자 맞추기 게임
import time
import random
start = time.time()
comNum = random.randint(1, 10)
myNum = 0
while comNum != myNum:
   myNum = int(input("번호를 입력하세요"))
   if(myNum > comNum):
       print("myNum이 크다")
   elif(myNum < comNum):
       print("myNum이 작다")
   else:
       print("성공")
end = time.time()
print("걸린시간 %d" % (end-start) )

#문제 ) 커피 자판기 !! 자판기에는 커피가 5잔밖에 안남았어요
# 커피는 종류 2개 한개는 3천원 , 3백원짜리커피
#나는 현재 돈이 6천원 !!!

# 종료조건 커피가 다떨어지면 종료!
# 내돈이 다떨어지면 종료!0