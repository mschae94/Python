"""
클래스매서드
1. 클래스 변수를 다루기 위해 사용한다.
2. 클래스를 구분하는 cls를 첫번째 매개변수 로 기술한다
3. 매서드 정의 위에 데토레이터 @classmethod 를 기술한다.
4. 객체를 생성하지 않고 매서드를 실행할수있다.
5. 클래스 이름과 객체 이름으로 모두 실행할수 있다.
"""
class Test:
    easy = 0
    def __init__(self):
        self.easy = 10
    @classmethod
    def tt(cls):
        cls.easy = 100

print(Test.easy)
t1 = Test()
print(t1.easy)
t1.tt()
print(t1.easy)
print(Test.easy)

