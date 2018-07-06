menu = """
***코리아 까페***
1.아메리카노 : 3000
2.까페라떼   : 3500
5.종료
"""
num = 0
sum = 0
while num != 10:
    num = int(input(menu + "\n 메뉴를 선택하세요 : "))
    if num == 1:
        sum += 3000
        print("아메리카노주문했습니다")
    elif num == 2:
        sum += 3500
    elif num == 5:
        print("주문을 종료합니다")
        num = 10
#문제) 5를 눌르면 주문종료시켜보세요
print("주문하신 금핵은 총 %d원 입니다 ." % sum)