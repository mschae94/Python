class Person: # 대문자로 시작한다
    name = "1"
    age = 0

hongil = Person()
hongil.name = "홍길동"
hongil.age = "24"

print(hongil.name + "은 " + hongil.age + " 세 입니다" )


#문제 1번 person클래스를 이용해서 철수를 만들어보세요
#문제 2) Animal 클래스를 만들어보세요 요소는 이름  , 색깔 , 종류
class Animal:
    name = ""
    color = ""
    kind = ""

giraff = Animal()
giraff.name = "기린"
giraff.color = "노랑"
giraff.kind = "포유류"

