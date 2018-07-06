
# 정보 은닉
"""
클래스 내에 정의된 함수를
클래스 밖에서 함부로 접근하면 안되는 값이 있다면,
데이터를 숨길 필요가 있다.
c++ c#
"""
class MyCounter:
    cnt1 = 0
    __cnt2 = 0      #변수이름 앞에 언더바 2개를 붙이면
                    # 클래스외부에서 볼수없다
    def count(self):
        self.cnt1 +=1
        print("cnt1:" , self.cnt1)

        self.__cnt2 += 1
        print("cnt2: " , self.__cnt2)

c = MyCounter()
c.count()
print(MyCounter.cnt1)
print(MyCounter.__cnt2) #에러

#print(MyCounter.MyCounter.__cnt2) # 다음시간





















#문제 정렬알고리즘  # 주말 과제 !!
values = [80, 10 , 243 , 20 , 56, 1 , 9]
"""
10 80  
10 80  243 
10 80  20  243
10 80  20   56  243
10 80  20   56   1  243
10 80  20   56   1   9   243
10 80
10 20  80
10 20  56   80
10 20  56   1   80
10 20  56   1    9   80
10 20  1    56
10 20  1     9   56
10 1  20
10 1   9   20
1  10
1  9   10

"""
#직접구현을 해보세요
#

#print(values)