#검사할 조건이 둘이상이라면,
#if - elif문
#ex01) 정수를 입력받아, 그수가 양수 , 0 , 음수인지 판단해보자.
# num = int(input("정수를 입력하세요"))
# result = ""
# if num > 0 :
#     result = "양수"
# elif num == 0 :
#     result = "0"
# elif num < 0 :
#     result = "음수"
# print("%d(은)는 %s 입니다"%(num , result))
#문제1) 홍콩반점 매뉴 4개 만들어보세요~

print("*** 홍콩반점 ***\n"
      "1. 쟁반짜장 : 10000원\n"
      "2. 간짜장   :  5000\n"
      "3. 불짱뽕   :  8000\n"
      "4. 볶음밥   :  6000\n")
#난지금 6000원이 있다
number = int(input("주문할번호를 입력해주세요: "))
if number == 1:
     print("쟁반짜장")
elif number ==2:
     print("간짜장")
elif number ==3:
     print("불짬뽕")
elif number ==4:
     print("볶음밥")

