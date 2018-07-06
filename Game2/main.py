import pygame
import random
from Game2.settings import * #  (*)다 가져온다
from Game2.sprite import Player
from Game2.sprite import Platform

class Game:
    def __init__(self): #저절로 처음에한번 실행되는 함수
        pygame.init() # 파이게임 초기화
        self.screen = pygame.display.set_mode((WIDTH , HEIGHT)) #화면구성
        pygame.display.set_caption(TITLE) #제목
        self.clock = pygame.time.Clock() # 시간가저오기
        self.running = True #업데이트 구동

    def new(self): # 초기화 작업을할곳
        self.all_sprites = pygame.sprite.Group()# 모든객체 저장 할곳
        self.platforms = pygame.sprite.Group() # 플랫폼 객체들만 따로 모아 저장

        self.player = Player(self) #플레이어객체 생성  # 9/29

        self.all_sprites.add(self.player)  #플레이어등록
        self.plaform1 = Platform(WIDTH /2 - 75, HEIGHT - 200 , 150 , 30)
        self.plaform2 = Platform(0, HEIGHT - 30, WIDTH, 30) #좌표 , 크기
        self.all_sprites.add(self.plaform1) # 플랫폼 등록  모든객체 등록
        self.platforms.add(self.plaform1) #플랫폼 등록   플랫폼객체 만 모아놓은 리스트
        self.all_sprites.add(self.plaform2)
        self.platforms.add(self.plaform2)

        self.run()
    def run(self): # 업데이트
        self.playing =True
        while self.playing:
            self.clock.tick(30)
            self.event()
            self.update()
            self.draw()
    def update(self): # 업데이트 2
        self.player.update()
        self.all_sprites.update() # 이안에 담겨있는 객체들 업대이트함수를 한번에실행

        if self.player.pos.y > 0: # 플레이어가 화면안에있으면
            hits = pygame.sprite.spritecollide(self.player , self.platforms ,  False)
            # 충돌함수 들어오는 2번째매개변수 값이 그룹이여야된다.
            if hits:
                self.player.pos.y = hits[0].rect.top  # 첫번째 부딪힌 렉트에 위치 고정
                self.player.vel.y = 0 # 중력값 0

    def event(self): # 이벤트만 담당
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running =False
            if event.type ==pygame.KEYDOWN:   # 9/29 점프 키 셋팅
                if event.key == pygame.K_SPACE:
                    self.player.jump()


    def draw(self):  # 그리기 담당

        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()    # 최종적으로 전부 갱신

    def show_start_screen(self):pass # 시작화면
    def show_go_screen(self):pass # 종료화면

g = Game()
#g.show_start_screen()
while g.running:
    g.new()

pygame.quit()


