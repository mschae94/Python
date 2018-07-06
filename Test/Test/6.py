#총알발사
# 문제1) 총알 여러발 발사 지금은 한발만 (난이도 상)
import pygame
# pygame 라이브러리를 import

###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################

###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################
import random

WHITE = (255, 255, 255)
pad_width = 740 # 740 으로 바꿔야함 어떻게 작용하는지 보여줌
pad_height = 370
background_width = 740 #  배경길이
# 흰색을 표현하는 값 , 게임판의 폭 , 게임판의 높이를 전역변수로 선언


def drawObject(obj , x  , y):
    global gamepad
    gamepad.blit(obj,(x,y))


def back(background , x, y):  #코드를 바꿈
    global gamepad
    gamepad.blit(background, (x, y))


def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():  # 게임이 구동되는 함수 init()함수에서 호출
    global gamepad, clock, aircraft, background ,background2 # 전역변수 설정

    ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
    global bat,fire1 ,fire2 ,bullet
    ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

    x = 100 # 비행기 x
    y = pad_height / 2 # 비행기 y
    y_change = 0 # 비행기 움직임변화
    background_x = 0 # 배경위치
    background2_x = background_width

    bat_x = pad_width
    bat_y = random.randrange(0,pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)

    fire_x2 = pad_width
    fire_y2 = random.randrange(0, pad_height)

    ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
    canFire = 0 # 총알 발사여부
    bullet_x = 0
    bullet_y = 0
    ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

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
                ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
                #스페이스 키로 총알발사
                elif event.key == pygame.K_SPACE:
                    if canFire == 0:
                        bullet_x = x
                        bullet_y = y
                        canFire = 1
                 ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

            # keyup 이벤트 키에서 손땟을때
            if event.type == pygame.KEYUP:
                # 움직음을 정지함  완벽하진않음
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change  # 위아래 움직임 적용

        background_x -=2
        background2_x -= 2
        # 배경 스크롤


        bat_x -=7
        if bat_x <=0:
            bat_x = pad_width
            bat_y = random.randrange(0 , pad_height)

        fire_x -= 15

        if fire_x <=0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)

        # 배경이 넘어가면 뒤에붙여줌
        if background_x == -background_width:
            background_x = background_width;
        if background2_x == -background_width:
            background2_x = background_width;

        ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
        #총알 움직임
        bullet_x += 10
        if bullet_x > pad_width:
            canFire =0
        ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################


        gamepad.fill(WHITE)  # 마우스창을 닫지않았다면 흰색으로 채움

        back(background , background_x,  0)
        back(background2 , background2_x , 0 ) #배경위치 적용


        drawObject(bat , bat_x , bat_y)
        drawObject(fire1,  fire_x , fire_y)

        ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
        #충돌안됬을때만 그리기
        if canFire ==1:
            drawObject(bullet , bullet_x , bullet_y)
        ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

        airplane(x, y)  # 비행기 위치 적용

        pygame.display.update()  # 위의 내용 적용

        clock.tick(60)  # 초당 60번 반복

    pygame.quit()  # pygame  라이브러리 종료
    quit()  # 게임종료


def initGame():  # 게임을 초기화 하고 시작하는함수
    global gamepad, aircraft, clock ,background , background2 # 전역변수 선언

    ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
    global bat , fire1 ,fire2 ,bullet
    ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

    pygame.init()  # pygame 라이브러리 초기화

    gamepad = pygame.display.set_mode((pad_width, pad_height))
    # 게임판 크기 설정

    pygame.display.set_caption("PyFlying")
    # 게임이름 설정 - 게임 상단 에 출력

    aircraft = pygame.image.load('plane.png')  # 스크립트가 있는폴더
    background = pygame.image.load('background.png')
    background2 = background.copy() #배경카피 배경을 2장을 만듬

    bat = pygame.image.load('bat.png')
    fire1 = pygame.image.load('fireball.png')
    fire2 = pygame.image.load('fireball2.png')

    ###################   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  #################
    bullet = pygame.image.load('bullet.png')
    ###################   <<<<<<<<<<<<<<<<<<<<<<<<<<<<   #################

    clock = pygame.time.Clock()
    # FPS 초당프레임 설정을 위해 클락 설정

    runGame()
    # 초기화를 끝내고 runGame() 호출

initGame()  # init함수호출