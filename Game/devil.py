import pygame
import random

#악마 생성하기
class Devil():
    def __init__(self,screen,rec): 
        self.screen = screen    
        self.screen_width = rec[0]
        self.screen_height = rec[1]
        self.img = pygame.image.load('./images/em2.png').convert_alpha()
        self.img = pygame.transform.scale(self.img , (90, 90))
        self.imgw = pygame.image.load('./images/wow.png').convert_alpha()
        self.imgw = pygame.transform.scale(self.imgw , (90, 80))
        self.imgww = pygame.image.load('./images/k_10.webp').convert_alpha()
        self.imgww = pygame.transform.scale(self.imgww, (45, 5))
        
        self.devil_HP = 10
        self.width = 700
        self.wepon = True
        self.imgw = None
        self.bombtick = 0
        
        self.hpFont = pygame.font.SysFont("굴림", 26)
        
    
        #비행기
        self.rec = self.img.get_rect()
        self.rec.x = random.randint(0,40)
        self.rec.y = random.randint(0,self.screen_height) 
        
        #총알
        self.rec_ww = self.imgww.get_rect()
        self.rec_ww.x = self.rec.centerx + 30
        self.rec_ww.y = self.rec.centery
        
        self.ticks = pygame.time.get_ticks()
        self.pos = None   
         
    def draw(self): #이미지 이동하며 그리는 곳
        if self.rec.y > self.width:
            self.rec.y -= 1
        if self.rec.y < 0:
            self.rec.y += 1
        elapsed_time = (pygame.time.get_ticks() - self.ticks)        
        if elapsed_time > 1:
            self.ticks = pygame.time.get_ticks()
            self.rec.x += random.randint(0,2)  
            self.rec.y += random.randint(-1, 1)  
            mtext_2 = self.hpFont.render(f"HP : {self.devil_HP}", True, 'yellow')
            self.screen.blit(mtext_2, (self.rec.x, self.rec.y-10))                
        if self.rec.x<self.screen_width:
            
            self.rec_ww.x += 3
            self.rec_ww.y += 0
            
            self.screen.blit(self.imgww, self.rec_ww)
            self.pos = self.screen.blit(self.img, self.rec)
            self.posww = self.screen.blit(self.imgww, self.rec_ww)
            return False
        else:
            return True    
                
    def checkCollision(self, arrows): #충돌했는지 확인
        for i, arr in enumerate(arrows):            
            if self.pos.colliderect(arr.rec):
                centerx = arr.rec.centerx
                centery = arr.rec.centery
                #self.screen.blit(self.imgw, (centerx, centery))
                return centerx,centery , i           
        return None, None, None
    
    def checkCollision_player(self,playerImgRec):
            if self.pos.colliderect(playerImgRec):
                centerx = playerImgRec.centerx
                centery = playerImgRec.centery
                # print(f'dkj')                    
                return centerx, centery
            return None, None
        
    def checkCollision_playerww(self,playerImgRec):
        if self.wepon and self.posww.colliderect(playerImgRec):
            self.wepon = False
            centerx = playerImgRec.centerx
            centery = playerImgRec.centery
            #print(f'dkj')                    
            return centerx, centery
        return None, None
        