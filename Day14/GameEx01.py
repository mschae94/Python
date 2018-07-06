import pygame # 파이게임모듈

WHITE = (255, 255, 255) #배경색
#문제1) 레드. 블루 그린 화면을 만들어보세요
RED = (255,0,0)
padWidth = 1024
padHeight = 512
padWidth2 = 500
padHeight2 = 100
def runGame():
    global gamePad, clock #글로벌변수
    crashed = False #종료조건
    while not crashed:#종료조건이 트루가 될때까지 반복
        for event in pygame.event.get(): #모든 이벤트를 검사함
            if event.type == pygame.QUIT: # X을 눌렀을때
                 crashed = True  #종료를 트루로한다
        #gamePad.fill(WHITE)
        gamePad.fill(RED)   #색깔
        pygame.display.update()  # 내용갱신
        clock.tick(60)  # 갱신횟수
def InitGame():
    global gamePad , clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    #gamePad = pygame.display.set_mode((padWidth2, padHeight2))
    pygame.display.set_caption("pyFlying")
    #pygame.display.set_caption("SBS")
    clock = pygame.time.Clock()
    runGame()

InitGame()





