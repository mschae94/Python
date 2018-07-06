#리스트의 인덱싱
#리스트도 문자열과 마찬가지로 인덱스 번호로 구분할수 있다.
#  0 부터 시작한다
numList = [10 , 22 , 63]
print(numList[0])
print(numList[1])
print(numList[2])
# 2차원 리스트의 인덱싱
lst = [  [1,2,3]  ,  [4,5,6]  ,  [7,8,9]  ]
print("0행 : " , lst[0])
print("1행 : " , lst[1])
print("2행 : " , lst[2])

print("0행0열" , lst[0][0])
print("1행1열" , lst[1][1])
print("2행2열" , lst[2][2])

lst = [1,2,3,[4,5,6]]
print("0행" , lst[0])
print("3행0열", lst[3][0])
print(lst[3])

