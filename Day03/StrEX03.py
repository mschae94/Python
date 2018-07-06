# 문자열 슬라이싱
"""
1. 슬라이싱(slicing 이란?
- 무언인가를 '잘라낸다' 는 의미이다

2. 슬라이싱을 통해 문자열을 나눌 수있다.

3. 슬라이싱 방법
- 변수명[시작번호:끝번호]
"""
line = "-------------------------"
"""
a = "Korea Academy"
# Korea 만 출력해보자 !!
print(a[0:4])
print(a[0:5])
print(line)
#문제1) Academy 만출력해보세요
print(a[6:13])
print(a[6:])
print(a[:5])
#print(a[:5])
print(a[:])
#print(a[:])
print(a[6:-3])
#print(a[6:-3])
#print(a[6:-9])
print(a[6:-9])
"""
import datetime
date1 = datetime.date.today()
print(type(date1))
date1 = str(date1)
print(date1)
#문제 1) 위의 결과를 다음과 같이 변경하여서 출력해보자!
# 2017년 09월 11일
year = date1[:4]
month = date1[5:7]
day = date1[8:]
print(year)
print(month)
print(day)
print("%s년 %s월 %s일" %(year , month , day))
print(line)




