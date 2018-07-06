
"""
for문의 기본구조
    for 변수 in (리스트,문자열,튜플):
        실행할 문장1
        실행할 문장2

리스트 , 튜플, 문자열의 첫번째 요소부터
마지막요소까지 차례대로 변수에 대입되어
for문 안의 수행할 문장이 실행된다

리스트  []  리스트는 안의 값을 마음대로 변경가능
튜플   ()  튜플은 안에 값을 변경불가
"""
# for i in range(5):
#     print("hello world")
#
# for i in [10 , 20 , 30 , 40 , 5]:
#     print("%d" % i)
# for i in (10 , 20 , 30 , 40 , 50):
#     print("%d" % i)
#
# lst = [30,40]
# for i in lst:
#     print("%d" % i)
#
# lstlst  = [[1,2] , [3,4], [5,6]]
#
# for i in lstlst:
#     print(i , end = " " )

lstlst2 = [ ["학생1" , 100] , ["학생2" , 80] , ["학생3" , 60]]

for (i  , j) in lstlst2:
    print("%s 의 점수 : %d " % (i , j))

#문제 1) 총 5명의 학생이 시험을 보았는데,
# 시험 점수가 60점이상이면 합격이고 그이하 불합격 결과를 보여주자.

score = [90 , 30 , 67 , 60 , 59]

num = 0
for i in score:
    num += 1
    if i >= 60:
        print ("%d번 학생은 %d 점으로 합격" %(num, i))
    else:
        print( "%d번 학생은 %d 점으로 불합격 " %(num , i))

#문제 2) 양수의 갯수와 음수의 갯수를 출력해보세요
lst = [1 , - 10 , 40 , 50 , -40]
countPlus  = 0
countMinus = 0

for i in lst:
    if i > 0:
        countPlus +=1
    else:
        countMinus +=1
print("양수의 개수:" , countPlus)
print("음수의 개수:" , countMinus)







