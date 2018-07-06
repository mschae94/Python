#1 ~ 10 까지의 홀수를 출력해보자!

# While 활용!
a = 0
# while a < 10:
#     a += 1 # a = a + 1
#     #print(a)
#     if a % 2 == 1:
#         print(a)

while a < 10:
    a += 1   # a의 숫자1씩 증가
    if a % 2 == 0: # 짝수면
        continue  # 밑에 문장들을 실행시키지않고 다시 돌아간다
    else:
        print(a)