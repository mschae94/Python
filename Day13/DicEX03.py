#집합(SET)

"""
1. 집합에 관련된 것들을 쉽게 처리하기 위한 자료형
2. 순서가없다.
"""
ss = set([1 , 2 , 3])
print(ss)

s1 = set([1,2,3,4,5,6])
s2 = set([3,4,7,8])

#교집합 : &     # 쉬프트 + 7
print(s1 & s2)
#합집합 : |     # 우리나라원표시  + 쉬프트
print(s1 | s2)
#차집합 : -
print(s1 - s2)
# add(): 집합에 한개의 요소 추가하기
s1.add(100)
print(s1)
# update() : 집합에 여러개의 요소 추가하기
s1.update([19 , 30])
print(s1)
# remove() : 집합에 요소 삭제하기
s1.remove(2)
print(s1)

#문제 2)
a = set(["korea" , "c" , "it" , "java"])
b = set(["python , korea , c++ , it  "])
#1) 두개의 리스트에 공통적으로 속한 이름
#2) 각각의 리스트에 다른리스트와 중복되지않은 이름


