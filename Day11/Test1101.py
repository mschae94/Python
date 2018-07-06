
#문제 1) 돈을 입력받고 (ex)65321원  화폐매수를 구해보세요
#50000 1매   10000 1매 5천원 1매 100원 3개  10 2개 1원 1개 #과제
#문제 2번 )
"""
     *
    ***
   *****
  *******
 *********
"""
line = "=============================="
for i in range(1,6):
    #print(i)
    for j in range (1 , i +1):
        #print(j)
        print('*' , end='')
    print()
print(line)

for i in range(1,6):
    for j in range (1 , 7 - i):
        print('*' , end='')
    print()
print(line)

for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ' , end='')
    for j in range(1 , i +1):
        print('*' , end='')
    print()
print(line)






