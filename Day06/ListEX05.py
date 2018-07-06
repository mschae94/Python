# 리스트의 수정, 변경 삭제

# 1. 리스트에서 하나의 값 수정하기
lst = [1 , 2 , 4]
lst[2] = 10
print(lst)

lst1 = ['a' , 'b' , 'c']
lst1[0] = "k"
print(lst1)
lst1[2] = 100
print(lst1)

# case 1
lst1[0] = ['u' , 'i' , 'o']
print(lst1)

# case 2
print(lst1[1:2])
lst1[1:2] = [1, 2 ,3]
print(lst1)

# 둘사이는 큰차이가 있다!!!!!


