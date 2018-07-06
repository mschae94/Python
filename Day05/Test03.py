#학점처리 프로그램(1단계)

#문제1)
"""
이름과 국어, 영어 , 수학 3과목 대한 성적을 입력받고
총점 평균 을 구해보세요 단! 평균은 소수점 1자리 까지만 출력해보세요

#문제2)
평균 >= 90 : A
평균 >= 80 : B
평균 >= 70 : C
평균 >= 60 : D
그이하     : F
============
이름: 홍길동
총점: 250
평균: 83.7
학점: B
"""
name = input("이름:")
kor = int(input("국어성적"))
eng = int(input ("영어성적"))
math = int(input("수학성적"))
total = kor + eng + math
avg = total/3
hak = ""
if avg <= 100:
    if avg >= 90:
        hak = 'A'
    elif avg >= 80:
        hak = 'B'
    elif avg >= 70:
        hak = 'C'
    elif avg >= 60:
        hak = 'D'
    else:
        hak = 'F'
    print("이름: %s" %name)
    print("총점: %d" %total)
    print("평균: %.1f" %avg) #소수점1자리
    print("학점: %s" %hak)
else:
    print("성적을 잘못입력했습니다")




