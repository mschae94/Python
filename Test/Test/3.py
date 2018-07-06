
#배경
#문제 1) 배경을 화면 중앙에 위치 시켜보세요

###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################

###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################


import pygame
# pygame 라이브러리를 import

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370
# 흰색을 표현하는 값 , 게임판의 폭 , 게임판의 높이를 전역변수로 선언

###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ##############
def back(x, y):
    global gamepad, background
    gamepad.blit(background, (x, y))
###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   ###############


def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))


def runGame():  # 게임이 구동되는 함수 init()함수에서 호출

###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    ##################
    global gamepad, clock, aircraft, background  # 전역변수 설정
###################    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    ################


    x = 100 # 비행기 x
    y = pad_height / 2 # 비행기 y
    y_change = 0 # 비행기 움직임변화


    ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   ##################
    background_x = 0 # 배경위치
    ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################


    crashed = False  # 게임종료 설정
    while not crashed:
        for event in pygame.event.get():  # 다양한이벤트 리턴

            # 종료이벤트
            if event.type == pygame.QUIT:  # 마우스창을 닫는다면
                crashed = True  # 반복문종료

            # keydown 이벤트 키를 눌렀을때
            if event.type == pygame.KEYDOWN:
                # 방향키 up
                if event.key == pygame.K_UP:
                    y_change = -5
                # 방향키 down
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            # keyup 이벤트 키에서 손땟을때
            if event.type == pygame.KEYUP:
                # 움직음을 정지한다  완벽하진않음
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change  # 위아래 움직임 적용

        gamepad.fill(WHITE)  # 마우스창을 닫지않았다면 흰색으로 채움

        ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #################
        back(background_x, 0)
        ####################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<  #################


        airplane(x, y)  # 비행기 위치 적용

        pygame.display.update()  # 위의 내용 적용

        clock.tick(60)  # 초당 60번 반복

    pygame.quit()  # pygame  라이브러리 종료
    quit()  # 게임종료


def initGame():  # 게임을 초기화 하고 시작하는함수
    global gamepad, aircraft, clock ,background # 전역변수 선언

    pygame.init()  # pygame 라이브러리 초기화

    gamepad = pygame.display.set_mode((pad_width, pad_height))
    # 게임판 크기 설정

    pygame.display.set_caption("PyFlying")
    # 게임이름 설정 - 게임 상단 에 출력

    aircraft = pygame.image.load('plane.png')  # 스크립트가 있는폴더

    ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   ################
    background = pygame.image.load('background.png')
    ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

    clock = pygame.time.Clock()
    # FPS 초당프레임 설정을 위해 클락 설정

    runGame()
    # 초기화를 끝내고 runGame() 호출


initGame()  # init함수호출