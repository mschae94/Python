#중첩 if문
"""
성별과 나이를 입력받아
남자 , 여자 , 성인 , 미성년 을 구분하는 프로그램을 작성해보자.
"""

"""
gender = int(input("성별: ( 남:1 ,여:2"))
age = int(input("나이:"))
if gender:
    if age >= 18:
        print("남자 성인")
    else:
        print("남자 미성년")
else:
    if age >= 18:
        print("여자 성인")
    else:
        print("여자 미성년")
        
"""

#문제1)  놀이기구 키제한
#1. 사용자로부터 키를 입력받는다.
#2. 키가 150이상이면 통과
#3. 키가 150 미만이라면 , 1) 부모동반 ok 2)아니면 no
stature = int(input("키?"))
if stature >=150:
    print("통과")
else:
    answer =int(input("부모?"))
    if answer ==1:
        print("통과")
    else :
        print("노!")

