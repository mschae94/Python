# Exam01

class SayMyName:
    def __init__(self, myname):
        self.myname = myname

    def say(self):
        print("나의 이름은", self.myname, "입니다.")

# 나의 이름은 이정우 입니다.
# 위의 문장이 출력될 수 있도록 코드를 작성해보자.



# Exam02
# 다음 코드의 비어있는 3개의 문장을 완성해보자.

class Meeting:

    #
    #
    #

    def talk(self):
        print("%s님과 대화 중입니다." % self.name)
    ################################################3

f1 = Meeting("이병재")
f2 = Meeting("박영호")

f1.talk()
f2.talk()

# 이병재님 어서오세요!
# 박영호님 어서오세요!
# 이병재님과 대화 중입니다.
# 박영호님과 대화 중입니다.

