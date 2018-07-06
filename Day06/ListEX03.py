#리스트의 슬라이싱

lst = [1,2,3,4,5]

print(lst[0:4]) # 0 ~ 1
b = lst[:4]
print(b)

c = lst[2:] # 3 ~ 5
print(c)

lst = [1 , 2 , 3 ,['a' , 'b' , 'c'] , 4 , 5 ]
#문제1) 아래와 같이 출력해보세요

#   ['a' , 'b']
#  [3 , ['a' , 'b' , 'c'] , 4]

print(lst[3][:2])
print(lst[2:5])