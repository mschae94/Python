#2중for문을 이용해 구구단을 만들어봅시다

for i in range(2, 10): # 첫번째 부터 마지막 직전까지 2~9
    print("****%d단***" %  i)
    for j in range(1 , 10):   # 첫번째 포문 한번에 두번째 포문전체
        print("%d * %d = %d" %(i , j , i * j))
