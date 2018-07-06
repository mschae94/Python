#튜플은 요소를 수정할수없다(immutable)
t1 = ( 1,  2 , 'a' , 'b')
print(t1[0])
#t1[0] = 10
#del t1[1]

#리스트가 포함되어있으면 수정가능
t1 = (1 , 2 , [3 , 4 , 5] , 6 , 7)
t1[2][0] = 10
print(t1)

# 곱셈연산자 로 요소 할당하기
tup1 =(1,2,3)
tup2 = tup1 * 2
print(tup2)

# 덧셈 연산자로 튜플 결합
tup1 = (1, 2, 3)
tup2 = ("a" , "b" , "c")
print(tup1 + tup2)

#in연산자로 튜플 요소 확인하기
print("a" in tup2)

student1 , student2 , stundet4 = tup2








