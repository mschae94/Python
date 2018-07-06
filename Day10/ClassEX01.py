# 객체지향 프로그래밍 ==
#  실력
# 객체 = 속성 + 기능
# 자동차를 예로들면 ..
# 18인치 바퀴를 가지고 2000CC 엔진 을 가진 빨간차 는 // 속성
# 전진 후진 좌회전 우회전 을 할수있다 // 기능
# def 이름 :
class Car :
    wheelSize = 16
    Displacement = 2000
    color = "red"
    def forward(self):
        print("전진")
        pass
    def backward(self):
        print("후진")
        pass
    def turnLeft(self):
        print("좌회전")
        pass
    def turnRight(self):
        print("우회전")
        pass
myCar1 = Car()
myCar2 = Car()
print(myCar1.color)
#print(myCar1.forward())
#print(myCar2.turnRight())
myCar1.color = "blue"
print(myCar1.color)
print(myCar2.color)

# 객체 지향을 하는 이유!!
# 핸드폰 (결합성이 떨어저요) << == >> 조립pc(데스크탑)(결합성)

# 게임 ! 20년된게임 " 바람의 나라 " " 리니지 "
