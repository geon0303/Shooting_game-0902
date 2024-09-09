import pygame
import random

#아이템 생성하기
class ygr():
    def __init__(self,screen,rec,idex):
        self.screen = screen  
        self.idex = idex
        if self.idex ==0:  
            self.img = pygame.image.load('./images/item1.png').convert_alpha()
            self.ide =0
        elif self.idex ==1:
            self.img = pygame.image.load('./images/item2.png').convert_alpha()
            self.ide =3
            
        elif self.idex ==2:
            self.img = pygame.image.load('./images/item3.png').convert_alpha()
            self.ide = 2
            
        self.img = pygame.transform.scale(self.img , (50, 50))
        #self.imgw = pygame.image.load('./images/wow.png')
        #self.imgw = pygame.transform.scale(self.imgw , (90, 80))
        self.ide=1
        
    
        
        self.rec = self.img.get_rect()
        self.rec.x = rec[0]-150
        self.rec.y = rec[1]
        self.ticks = pygame.time.get_ticks()
        self.pos = None   
         
    def draw(self): #이미지 이동하며 그리는 곳
        elapsed_time = (pygame.time.get_ticks() - self.ticks)        
        if elapsed_time > 1:
            self.ticks= pygame.time.get_ticks()
            self.rec.x+= random.randint(0,2)  
            self.rec.y += random.randint(-1, 1)                
        if self.rec.x<self.screen.get_width():
            self.pos = self.screen.blit(self.img, self.rec)
            return False
        else:
            return True    
    
    def checkCollision_player(self,playerImgRec):
            if self.pos.colliderect(playerImgRec):
                centerx_2 = playerImgRec.centerx
                centery_2 = playerImgRec.centery
                # print(f'dkj')                    
                return centerx_2, centery_2
            return None, None
    