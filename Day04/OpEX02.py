#비교연산자
#비교연산자는 연산의 결과를 True or False 로 반환한다.

num1 = 10
num2 = 5
"""
# print(num1 < num2)
# print(num1 > num2)
# print(num1 == num2) # 왜 같다는 == 두개를 쓸까 ?  대입(=)이 더 많이 쓰여서 양보
# print(num1 != num2) # 다르다
# print(num1 >= num2)
# print(num1 <= num2)
"""
#논리 연산자
# x or y : x 가 참이거나 y 가 참이면 참
# x and y : x 가 참이고 y 도 참이면 참
# not x  : x 가 거짓이면 참

a , b , c , d = 10 , 9 , 8 , 7
print(a < b and c > d)
print(a > b and c > d)

print(a < b or c < d)
print(a > b or c < d)


