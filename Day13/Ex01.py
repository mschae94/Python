# 리스트는 인덱스의 표현이 정수로만 가능하다
lst = ['a' ,'b' , 'c']
print(lst[0])

#반면 , 딕셔너리는 대부분의 타입이 적용가능하다.

dic = {1:"hello" , 2:"world" , "python" : 3}
print(dic)
print(dic[1])
print(dic["python"])


dic = {"first": ['a', 'b' , 'c']}

print(dic["first"])

dic[3] = "하이"

print(dic)



