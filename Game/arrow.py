import pygame
import random

#화살 생성하기
class Arrow():
    def __init__(self, screen,rec,wepon):#ret : 화살이 시작될 위치값
        self.screen = screen
        self.wepon = wepon
        if self.wepon == 0:
            self.img = pygame.image.load('./images/wp1.png').convert_alpha()
        elif self.wepon == 1:
            self.img = pygame.image.load('./images/wp2.png').convert_alpha()
        elif self.wepon == 2:
            self.img = pygame.image.load('./images/wp3.png').convert_alpha()
        else:
            pass
        self.img = pygame.transform.scale(self.img , (50, 50))

        #화살이 그려질 시작 위치 잡기
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]
        self.arrtak = 10
        
    # def __del__(self):
    #     print('종료')
        
    def draw(self):      
        if (self.rec.x) > 0:  
            self.rec.x -= 1
            self.screen.blit(self.img, self.rec)
            return False
        else:
            return True

            