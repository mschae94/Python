#타자연습게임
import random
def Shuffle(question):
    print(question)
    for i in range(1000):
        length = len(question)
        index1 = random.randint(0 , length -1)
        index2 = random.randint(0 , length -1)
        temp1 = question[index1]
        question[index1] = question[index2]
        question[index2] = temp1
    print(question)
question = ["a" , "b" , "c" , "d" , "e"]
#Shuffle(question)
print(question)
random.shuffle(question)
print(question)

#문제1) 섞어보자!!


