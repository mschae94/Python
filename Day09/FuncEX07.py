#예상할수 없는 인수를 갖는 함수
"""
    def 함수명(*매개변수):
        실행할문장1
"""
def sum(*num):  # 마치 리스트자료형처럼
    total = 0
    for i in num:
        total += i
    return total
result = sum(19,29,39)
print(result)
result = sum (1,2,3,4,5,6)
print(result)

def calc(result , *num):
    if result == "sum" :
        total = 0
        for i in num:
            total +=i
    elif result == "mul":
        total = 1
        for i in num:
            total *=i
    return total

result = calc("mul" , 1 , 3 , 4 , 20)
print(result)
result = calc("sum" , 30 , 40 , 50 , 1)
print(result)
