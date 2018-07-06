import time
import random
start = time.time()
question =["Python" , "C", "JAVA" , "JSP" , "Android"]
#타자연습게임
#    문제 1) 차례대로 글자를 보여주고  맞추면 다음문제를 제시하고
# 다맞추기!! 문제가 너무 차례대로 나온다!!!
# #  문제2) 심화문제 !!! 문제 5개를 섞어보세요
#  문제3) 맞춘문제 다시 제시하지않기 # 과제
count = 0
while True:
    print("문제 : ", end="")
    print(question[count])
    answer = input()
    if question[count] == answer:
        print("통과!!!")
        count = count + 1
    else:
        print("오타 !! 다시도전 ")
    if count >= 5:
        print("모두 성공했습니다")
        end = time.time()
        result = end-start
        print ("총걸린시간은 %.1f입니다 " %result)
        break;
#문제
