class Unit:
    level = 1
    power = 10
    dex = 15
    life = 20
    mana = 50
    def __init__(self , userName):
        self.userName = userName
        print("계정이 생성되었습니다 . "
              "계정명:' %s '" % self.userName)
    def showInfo(self):
        print("=================")
        print("이름 : '%s'"  %self.userName)
        print("Level : '%d'" %self.level)
        print("=================")
    def levelUp(self):
        print("'%s'님 축하합니다. 랩업했습니다" % self.userName)
        self.level += 1
    def attack1(self):
        print("기본공격")
class BaBa(Unit):
    pass
class Magician(Unit):
    pass
player1 = BaBa("짱쌤")
player1.showInfo()
player2 = Magician("여자마법사")
player2.showInfo()
