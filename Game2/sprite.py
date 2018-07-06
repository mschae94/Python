import pygame as pg # 줄임말
from Game2.settings import * #(*) 다가져온다

vec = pg.math.Vector2 # (x , y)  // x + y 하나로 합친구조체

class Player(pg.sprite.Sprite):
    def __init__(self  , game ):  # 메인의 게임 클래스 정보를 넘겨준다 # 9/29
        pg.sprite.Sprite.__init__(self)# 부모 생성자 실행

        self.game = game        # 9/29  메인파일의 Game클래스 정보를 저장

        self.image = pg.Surface((20 , 40)) # 사각형만들기
        self.image.fill(BLACK) # 색깔
        self.rect = self.image.get_rect() # 사각형 정보만 저장
        self.rect.center = (WIDTH/2 , HEIGHT/2) #사각형 중앙구하기
        self.pos = vec(WIDTH/2 , HEIGHT/2) # 플레이어 위치
        self.vel = vec(0,0) # 속도  x + y 전부
        self.acc = vec(0,0) # 가속도  x 축만

    def update(self):
        self.acc = vec(0,PLAYER_GRAV) # 가속도 초기화
        keys = pg.key.get_pressed() # 키입력받음
        if keys[pg.K_LEFT]: #왼쪽키
            self.acc.x = -PLAYER_ACC #-5
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.pos.x += self.acc.x        # 가속도 적용
        self.vel.y += self.acc.y        # 중력 적용
        self.pos.y += self.vel.y        # 중력 적용
        self.rect.midbottom = self.pos # 위치계산 적용

    def jump(self):  # 9/ 29 일 점프기능 추가
        # sprite 클래스에서 main파일의 Game클래스를 사용
        hits = pg.sprite.spritecollide(self, self.game.platforms , False )
        if hits:
            self.vel.y = -20


class Platform(pg.sprite.Sprite):
    def __init__(self , x , y, w , h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



