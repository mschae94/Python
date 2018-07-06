import pygame # 파이게임모듈

WHITE = (255, 255, 255) #배경색
#문제1) 레드. 블루 그린 화면을 만들어보세요
RED = (255,0,0)
padWidth = 1024
padHeight = 512
#문제2) 박쥐를 오른쪽 중앙에 배치해보세요
# def aricraft(x ,y):
#     global  gamePad , aircraft
#     gamePad.blit(aircraft , (x , y))
def runGame():
    global gamePad, clock  , aircraft  , bat#글로벌변수
    ##############################################
    playerX = 100 #비행기위치
    playerY = padHeight/2
    changeY = 0
    batX = 1000
    batY = 200
    crashed = False #종료조건
    while not crashed:#종료조건이 트루가 될때까지 반복
        for event in pygame.event.get(): #모든 이벤트를 검사함
            if event.type == pygame.QUIT: # X을 눌렀을때
                 crashed = True  #종료를 트루로한다
            #문제 아래 왼족 오른족 만들어보세요

            if event.type == pygame.KEYDOWN: #아무키가 눌렸을때
                if event.key == pygame.K_UP: #아무키가 방향키업일때
                    changeY = -5
                if event.key == pygame.K_DOWN:  # 아무키가 방향키업일때
                    changeY = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    changeY = 0

        gamePad.fill(WHITE) #색깔
        ###################################
        playerY += changeY
        gamePad.blit(aircraft ,  (playerX , playerY)) # blit(객체 , 위치) #배치함수

        #문제 3) 박쥐가 왼쪽으로 날라가게 해보세요
        batX -= 10
        if batX == 0:
            batX = 1000
        #문제 4) 박쥐가 대각선으로 날라가게 해보세요
        #문제 4 - 1) 박쥐가 위에부딪히면 아래대각선 아래부딪히면 위대각선으로 이동시켜보세요
        gamePad.blit(bat , (batX , batY))

        ###################################
        pygame.display.update()  # 내용갱신
        clock.tick(60)  # 갱신횟수

def InitGame(): # 초기화
    global gamePad , clock , aircraft , bat

    pygame.init() #파이게임초기화
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption("pyFlying")
    clock = pygame.time.Clock() # 시간가져오기

    ############    스크립트가 있는폴더   #########################
    aircraft = pygame.image.load("plane.png") #비행기 이미지 로드
    bat = pygame.image.load("bat.png")
    ###############################################################


    runGame()# 런게임 함수실행

InitGame()





