import pygame
import random

#리치 생성하기
class Rich():
    def __init__(self,screen,rec):    
        self.screen = screen    
        self.screen_width = rec[0]
        self.screen_height = rec[1]
        self.img = pygame.image.load('./images/pm2.png').convert_alpha()
        self.img = pygame.transform.scale(self.img , (90, 80))
        self.imgw = pygame.image.load('./images/wow.png').convert_alpha()
        self.imgw = pygame.transform.scale(self.imgw , (90, 80))
        self.imgww = pygame.image.load('./images/k_10.webp').convert_alpha()
        self.imgww = pygame.transform.scale(self.imgww, (60, 5))
        
        #비행기
        self.rec = self.img.get_rect()        
        self.rec.x = random.randint(0,40)
        self.rec.y = random.randint(0,self.screen_height) 
        
        self.ticks = pygame.time.get_ticks()
        self.pos = None   
        self.rich_HP = 30
        self.arrtaks = 10
        self.width = 700
         
        
        self.hpFont = pygame.font.SysFont("굴림", 26)
         
    def draw(self): #이미지 이동하며 그리는 곳 
        if self.rec.y > self.width:
            self.rec.y -= 1
        if self.rec.y < 0:
            self.rec.y += 1
        offset = random.randint(0, 2)
        # print(offset)
        self.rec.x += random.randint(-1, 1)#+offset
        self.rec.y += random.randint(-1, 1)
        
        
        elapsed_time = (pygame.time.get_ticks() - self.ticks)
        if elapsed_time > 10:
            self.ticks = pygame.time.get_ticks()
            self.rec.x += random.randint(0,10) 
            self.rec.y += random.randint(-5,5) 
        
        # self.rec = self.img.get_rect()
        # self.rec.x = rec[0] 
        # self.rec.y = rec[1]
        
        # if (self.rec.x) < 0:  
        #     self.rec.x += 1
        #     self.screen.blit(self.imgww, self.rec)
        #     return False
        # else:
        #     return True
        
        mtext_2 = self.hpFont.render(f"HP : {self.rich_HP}", True, 'yellow')
        self.screen.blit(mtext_2, (self.rec.x, self.rec.y-10))  
                    
        if self.rec.x<self.screen_width:
            self.pos = self.screen.blit(self.img, self.rec)
            return False
        else:
            return True  
                
    def checkCollision(self, arrows): #충돌했는지 확인

        for i, arr in enumerate(arrows):            
            if self.pos.colliderect(arr.rec):
                #  self.rich_HP -= 10
                # print(111)
                # if self.rich_HP > 0:
                #     return None, None,None  
                centerx = arr.rec.centerx
                centery = arr.rec.centery
                # print('충돌')
                #self.screen.blit(self.imgw, (centerx, centery))
                return centerx,centery , i        
        return None, None, None
    
    def checkCollision_player(self,playerImgRec):
            if self.pos.colliderect(playerImgRec):
                centerx_2 = playerImgRec.centerx
                centery_2 = playerImgRec.centery
                # print(f'dkj')                    
                return centerx_2, centery_2
            return None, None 
                            
            