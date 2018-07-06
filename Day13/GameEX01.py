import pygame
#pygame 라이브러리를 import

WHITE = (0, 255, 255)
pad_width = 1024
pad_height =512
#흰색을 표현하는 값 , 게임판의 폭 , 게임판의 높이를 전역변수로 선언

def runGame():  #게임이 구동되는 함수 init()함수에서 호출

    global  gamepad , clock #전역변수 설정

    crashed = False  #게임종료 설정
    while not crashed:
        for event in pygame.event.get(): # 다양한이벤트 리턴
            if event.type ==pygame.QUIT:  # 마우스창을 닫는다면
                crashed = True  #반복문종료

        gamepad.fill(WHITE)
        pygame.display.update()
        # 마우스창을 닫지않았다면 흰색으로 채우고임판다시그림

        clock.tick(60) #초당 60번 반복

    pygame.quit() # 게임종료
def initGame(): #게임을 초기화 하고 시작하는함수
    global gamepad , clock # 전역변수 선언

    pygame.init() # pygame 라이브러리 초기화

    gamepad = pygame.display.set_mode((pad_width , pad_height))
    #게임판 크기 설정

    pygame.display.set_caption("PyFlying")
    #게임이름 설정 - 게임 상단 에 출력

    clock = pygame.time.Clock()
    # FPS 초당프레임 설정을 위해 클락 설정

    runGame()
    #초기화를 끝내고 runGame() 호출

initGame() #init함수호출