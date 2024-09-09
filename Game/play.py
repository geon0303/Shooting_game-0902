import pygame
import random
from devil import *
from arrow import *
from ygr import *
from rich import *
from boss import *


#키 이벤트 처리하기
def eventProcess():
    global idex, over, over_1
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            val['active'] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                val['active'] = False
            if event.key == pygame.K_SPACE:
                val['player_delay'] = pygame.time.get_ticks()
                idex =1
                            #화살 시작될 위치
                x = playerImgRec.centerx - playerImgRec.width/2 - 10
                y = playerImgRec.centery - 20
                #1개의 화살을 생성
                if player_info['wepon_emo'] >= 1:
                    ar = Arrow(screen,(x,y),player_info['wepon' ])
                    arrows.append(ar)
                    snd_space_2.play()
                    
                    # print(arrows)
                    player_info['wepon_emo'] -= 1
            if event.key == pygame.K_0:
                player_info['wepon'] = 0 
            if event.key == pygame.K_1:
                player_info['wepon'] = 1
            if event.key == pygame.K_2:
                player_info['wepon'] = 2
            if event.key == pygame.K_r:
                over = False
                over_1 = False
                val['HP'] = 50
                player_info['fire_power'] = 10
                player_info['black_power'] = 5
                player_info['white_power'] = 6
                val['score'] = 0
                player_info['wepon_emo'] = 10
                player_info['rich_level'] = 1
                
                
            # if event.key == pygame.K_UP:
            #     if playerImgRec.centery > 0:
            #         playerImgRec.centery -= 50
            #     else:
            #         pass        
            # if event.key == pygame.K_DOWN:
            #     if playerImgRec.centery < 400:
            #         playerImgRec.centery += 50  
            #     else:
            #         pass
            # if event.key == pygame.K_LEFT:
            #     if playerImgRec.centerx > 0:
            #         playerImgRec.centerx -= 50
            #     else:
            #         pass
            # if event.key == pygame.K_RIGHT:
            #     if playerImgRec.centerx < 800:
            #         playerImgRec.centerx += 50
            #     else:
            #         pass            
    
    key_pressed = pygame.key.get_pressed()
    # print(key_pressed)
    
    # if playerImgRec.centerx >= 1200 or playerImgRec.centerx <= 0:
    #     if key_pressed[pygame.K_LEFT]:
    #                 playerImgRec.centerx -= 0
    # if key_pressed[pygame.K_RIGHT]:
    #                 playerImgRec.centerx += 0
        
    # if playerImgRec.centery >= 800 or playerImgRec.centery <= 0:
    #     if key_pressed[pygame.K_DOWN]:
    #                 playerImgRec.centery += 0
    # if key_pressed[pygame.K_UP]:
    #                 playerImgRec.centery -=  
        
        
    if key_pressed[pygame.K_DOWN]:
        playerImgRec.centery += 1
        if playerImgRec.bottom >= screen.get_height(): #함수를 쓰는 이유 : 값이 변해도 자동화시킬려고
            playerImgRec.bottom = screen.get_height()
                        
    if key_pressed[pygame.K_UP]:
        playerImgRec.centery -= 1 
        if playerImgRec.top <= 0:
            playerImgRec.top = 0
    
    if key_pressed[pygame.K_LEFT]:
                    playerImgRec.centerx -= 1
                    if playerImgRec.x <= 0:
                        playerImgRec.x = 0
    if key_pressed[pygame.K_RIGHT]:
                    playerImgRec.centerx += 1
                    if playerImgRec.right >= screen.get_width():
                        playerImgRec.right = screen.get_width()
    if key_pressed[pygame.K_SPACE]:
                    val['player_delay'] = pygame.time.get_ticks()
                    idex =1
                    
##=================================================
def updatePlayer():
    
    global idex
    #Player 의 활 쏘는 장면 연출하기
    if idex != 0:
        elapsed  =pygame.time.get_ticks() - val['player_delay']
#        snd_space = pygame.mixer.Sound(f'go.wav')
#        snd_space.play( )
        if elapsed >300:
            idex = 0
    screen.blit(player_imgs[idex], playerImgRec)
    
def updateArrow():
    #화살 날아가는 장면 연출  
    for i, arr in enumerate(arrows):
        if arr.draw():  #이동하며 그린다.
            del arrows[i] #삭제 

def  updateDevils():
    global over, over_1
    #악마 업데이트    
    # arrow_del = []  
    for i, boar in enumerate(devils):
        
            if boar.draw():  #이동하며 그린다.
                del devils[i] #삭제
            else:
                centerx, centery, ai = boar.checkCollision(arrows)
                if centerx is not None: 
                    # print("wow")
                    del arrows[ai]
                    if player_info['wepon'] ==0:
                        player_info['fire_power'] = 10
                        player_info['wepon_emo'] += 0.5
                        boar.devil_HP -= player_info['fire_power']
                    if player_info['wepon'] ==1:
                        player_info['white_power'] = 5
                        boar.devil_HP -= player_info['white_power']
                    if player_info['wepon'] ==2:
                        player_info['black_power'] = 5
                        boar.devil_HP -= player_info['black_power']
                    if boar.devil_HP <= 0:
                        bomblist.append([pygame.time.get_ticks(),(centerx-100, centery)])
                        del devils [i]
                        snd_space_1.play()
                        val['score'] += 1
                        items.append(ygr(screen, (centerx,centery ), 0))  
                        #print(centerx)
                else:
                    centerx, centery = boar.checkCollision_player(playerImgRec)
                    if centerx is not None:   
                        del devils[i]                 
                        val['HP'] -= 7
                        snd_space_5.play()
                        if val['HP'] <= 0:
                        #    pygame.time.delay(2000) # 약 2초동안 GAME OVER 화면 유지
                        #    val['active'] = False
                            over = True
                            over_1 = True
                            
                        
                    else:
                        centerx, centery = boar.checkCollision_playerww(playerImgRec)
                        if centerx is not None:# and boar.wepon:                    
                            val['HP'] -= 7
                            snd_space_5.play()
                            #boar.wepon = False
                            if val['HP'] <= 0:
                                # pygame.time.delay(2000) # 약 2초동안 GAME OVER 화면 유지
                                # val['active'] = False
                                over = True
                                over_1 = True          
    
    #print(bomblist)
    for i, po in enumerate(bomblist):
        time = po[0]
        screen.blit(bomb, po[1]) 
        if pygame.time.get_ticks() - time > 100:
            del bomblist[i]
    #screen.blit(bomb, (centerx, centery))
    #bomblist.append((centerx, centery))
    
    

def updateRichs():
    global over, over_1
    #리치 업데이트    
    # arrow_del = []  
    for i, rich in enumerate(richs):
        if rich.draw():  #이동하며 그린다.
            del richs[i] #삭제
        else:
            centerx, centery, ai = rich.checkCollision(arrows)
            if centerx is not None: 
                if player_info['wepon']==0:
                    player_info['fire_power'] = 5
                    rich.rich_HP -= player_info['fire_power']
                if player_info['wepon'] ==1:
                    player_info['white_power'] = 10
                    player_info['wepon_emo'] += 0.2
                    rich.rich_HP -= player_info['white_power']
                if player_info['wepon'] ==2:
                    player_info['black_power'] = 5
                    rich.rich_HP -= player_info['black_power']
                del arrows[ai]
                if rich.rich_HP <= 0:
                    del richs [i]
                    bomblist.append([pygame.time.get_ticks(),(centerx-100, centery)])
                    snd_space_1.play()
                    val['score'] += 1
                    items.append(ygr(screen, (centerx,centery ), 1))
            else:
                centerx, centery = rich.checkCollision_player(playerImgRec)
                if centerx is not None:
                    del richs[i]
                    snd_space_3.play()
                    val['HP'] -= 12
                    if val['HP'] <= 0:
                    #    pygame.time.delay(2000) # 약 2초동안 GAME OVER 화면 유지
                    #    val['active'] = False
                        over = True
                        over_1 = True
    for i, po in enumerate(bomblist):
        time = po[0]
        screen.blit(bomb, po[1])
        if pygame.time.get_ticks() - time > 500:
            del bomblist[i]
        
    # for i in arrow_del:
    #     del arrows[i]
    
def updateBosses():
    global over, over_1
    #보스 업데이트    
    # arrow_del = []  
    for i, boss in enumerate(bosses):
        if boss.draw():  #이동하며 그린다.
            del bosses[i] #삭제
        else:
            centerx, centery, ai = boss.checkCollision(arrows)
            if centerx is not None: 
                if player_info['wepon']==0:
                    player_info['fire_power'] = 5
                    boss.boss_HP -= player_info['fire_power']
                if player_info['wepon'] ==1:
                    boss.boss_HP -= player_info['white_power']
                    player_info['white_power'] = 5
                    snd_space_1.play()
                if player_info['wepon'] ==2:
                    player_info['black_power'] = 10
                    boss.boss_HP -= player_info['black_power']
                del arrows[ai]
                if boss.boss_HP <= 0:
                    del bosses [i]
                    snd_space_1.play()
                    val['score'] += 1
                    items.append(ygr(screen, (centerx,centery ), 2))
                    
            else:
                centerx, centery = boss.checkCollision_player(playerImgRec)
                if centerx is not None:
                    del bosses[i]
                    snd_space_5.play()
                    val['HP'] -= 12
                    if val['HP'] <= 0:
                    #    pygame.time.delay(2000) # 약 2초동안 GAME OVER 화면 유지
                    #    val['active'] = False
                        over = True
                        over_1 = True
                else:
                    centerx, centery = boss.checkCollision_playerww(playerImgRec)
                    if centerx is not None:
                        snd_space_3.play()
                        val['HP'] -= 15
                        if val['HP'] <= 0:
                                # pygame.time.delay(2000) # 약 2초동안 GAME OVER 화면 유지
                                # val['active'] = False
                                over = True
                                over_1 = True     
                        
    # for i in arrow_del:
    #     del arrows[i]
        
    #악마 생성하기
    elapsed_time = (pygame.time.get_ticks() - val['devil_delay'])
    if elapsed_time > 800:
        val['devil_delay'] = pygame.time.get_ticks()
        if player_info['rich_level'] == 1:
            devils.append(Devil(screen, (val['screen'][0],val['screen'][1])))   
##=================================================     
    #리치 생성하기
    elapsed_time = (pygame.time.get_ticks() - val['rich_delay'])
    if elapsed_time > 1200:
        val['rich_delay'] = pygame.time.get_ticks()
        if player_info['rich_level'] == 2:
            richs.append(Rich(screen, (val['screen'][0],val['screen'][1])))    
##=================================================
    #보스 생성하기    
    elapsed_time = (pygame.time.get_ticks() - val['boss_delay'])
    if elapsed_time > 7000:
        val['boss_delay'] = pygame.time.get_ticks()
        if player_info['rich_level'] == 3:
            bosses.append(Boss(screen, (val['screen'][0],val['screen'][1])))    
##=================================================

def updateygr(): #함수는 호출할 때 실행함
    #용과리 업데이트    
    # arrow_del = []  
    global idex
    for i, item in enumerate(items):
            if item.idex ==0:
                if item.draw():  #이동하며 그린다.
                    del items[i] #삭제
                else:
                    centerx, centery = item.checkCollision_player(playerImgRec)
                    if centerx is not None:
                        # if item.ide==0:
                            # pass
                        #print('geon')
                        del items[i]
                        
                        # print(f"Hp {val['HP']}:", end='')
                        val['HP'] += 5
                        if val['HP'] > 50:
                            val['HP'] = 50
                        player_info['wepon_emo'] += 0.5
                            
                        # print(f"{val['HP']}")
                            
            elif item.idex ==1:
                if item.draw():  #이동하며 그린다.
                    del items[i] #삭제
                else:
                    centerx, centery = item.checkCollision_player(playerImgRec)
                    if centerx is not None:
                        # if item.ide==0:
                            # pass
                        #print('geon')
                        del items[i]
                        
                        # print(f"Hp {val['HP']}:", end='')
                        val['HP'] += 5
                        if val['HP'] > 50:
                            val['HP'] = 50
                        player_info['wepon_emo'] += 0.5
                            
                        # print(f"{val['HP']}")
                        
            elif item.idex == 2:
                if item.draw():  #이동하며 그린다.
                    del items[i] #삭제
                else:
                    centerx, centery = item.checkCollision_player(playerImgRec)
                    if centerx is not None:
                        # if item.ide==0:
                            # pass
                        #print('geon')
                        del items[i]
                        
                        # print(f"Hp {val['HP']}:", end='')
                        val['HP'] += 5
                        if val['HP'] > 50:
                            val['HP'] = 50
                        player_info['wepon_emo'] += 5
                            
                        # print(f"{val['HP']}")
def Box():
    if player_info['wepon'] == 0:
        mtext_4 = mFont30.render(f"  WEPON ▶ 1 : fire  {player_info['fire_power']} emo  {player_info['wepon_emo']:0.1f}", True, 'yellow')
        screen.blit(mtext_4, (400, 10)) 
    elif player_info['wepon'] == 1:
        mtext_4 = mFont30.render(f"  WEPON ▶ 2 : white  {player_info['white_power']} emo  {player_info['wepon_emo']:0.1f}", True, 'yellow')
        screen.blit(mtext_4, (400, 10)) 
    elif player_info['wepon'] == 2:
        mtext_4 = mFont30.render(f"3 : black  {player_info['black_power']} emo  {player_info['wepon_emo']:0.1f} ", True, 'yellow')
        screen.blit(mtext_4, (400, 10)) 
[0]

             
                     
        
##=================================================
def setText():
    mtext = mFont30.render(f"score : {val['score']}", True, 'yellow')
    screen.blit(mtext, (10, 10))
    
    mtext_2 = mFont20.render(f"HP : {val['HP']}", True, 'yellow')
    screen.blit(mtext_2, (playerImgRec.centerx - 20, playerImgRec.centery - 80))
    
    mtext_3 = mFont30.render(f"level : {player_info['rich_level']}", True, 'yellow')
    screen.blit(mtext_3, (150, 10))
    
    
        # pygame.draw.rect(screen, (255,255,255),(500,10,204,24), 1)  
def part():
    if val['score'] == 25:
        if player_info['rich_level'] != 2:
            player_info['rich_level'] = 2
            val['partmsg'] = f"level {player_info['rich_level']}"
            player_info['wepon_emo'] = 30
            snd_space_4.play()
        if player_info['wepon_emo'] > 60:
            player_info['wepon_emo'] = 60
        
        
    if val['score'] == 40:
        if player_info['rich_level'] != 3:
            player_info['rich_level'] = 3  
            val['partmsg'] = f"level {player_info['rich_level']}" 
            player_info['wepon_emo'] = 60
            snd_space_4.play()
            val['HP'] = 100
        if player_info['wepon_emo'] > 100:
            player_info['wepon_emo'] = 100
    if val['score'] == 50:
        # mFont = pygame.font.SysFont("malgungothic", 100)
        # img = mFont.render(f"GAME CLEAR", True, 'yellow')
        # rect = img.get_rect()
        # rect.centerx = screen.get_width() / 2
        # rect.centery = screen.get_height() / 2
        # screen.blit(img, rect)
        val['clearmsg'] = f'GAME CLEAR'
        
        
         
    if val['partmsg'] is not None: #None이 아닐 때 들어온다. 나중에 None 메세지 바뀜
        if val['partmsgtick'] == 0:
            val['partmsgtick'] = pygame.time.get_ticks() #현재 시간 저장
        mtext_5 = mFont70.render(val['partmsg'], True, 'blue')
        screen.blit(mtext_5, (500, 350))
        
    if pygame.time.get_ticks() - val['partmsgtick'] > 1500: #시간을 저장했을 때부터 지금까지 1500이 지났다면 실행
        val['partmsgtick'] = 0
        val['partmsg'] = None
        
    if val['clearmsg'] is not None:
        if val['clearmsgtick'] == 0:
            val['clearmsgtick'] = pygame.time.get_ticks()
            print("geonsss")
        mtext_6 = mFont70.render(val['clearmsg'], True, 'blue')
        screen.blit(mtext_6, (500, 350))

            
    if pygame.time.get_ticks() - val['clearmsgtick'] > 5000:
        val['clearmsgtick'] = 0
        val['clearmsg'] = None
        
def emo():
    # if val['emotick'] ==0:
    #     val['emotick'] = pygame.time.get_ticks()
    if pygame.time.get_ticks() - val['emotick'] > 1000:
        player_info['wepon_emo'] += 0.1
        val['emotick'] =pygame.time.get_ticks()
            
    # if player_info['wepon_emo'] > 60:
    #     player_info['wepon_emo'] = 60
    
def gameover():
    if over_1 == False:
        pass
    elif over_1 == True:
        mFont = pygame.font.SysFont("굴림", 40)
        mtext = mFont.render(f"GAME OVER[R]", True, 'yellow')
        screen.blit(mtext, (500, 400))
        val['HP'] = 0
        player_info['wepon_emo'] = 10
        player_info['rich_level'] = 1
        val['score'] = 0
    else:
        pass      
    

def bx():
    global bgx_1, bgx_2
    if bgx_1 ==val['screen'][0]:
        bgx_1 = 0
        bgx_2 =-val['screen'][0]
##======================================self.rec.x===========
#1. pygame 초기화
pygame.init()
pygame.display.set_caption("Shooting Game")

mFont30 = pygame.font.SysFont("malgungothic", 30) # 윈도우에서 폰트를 불러오는 것이기 때문에 여기에 놔야 시간이 많이 절약된다.
mFont20 = pygame.font.SysFont("malgungothic", 20)
mFont70 = pygame.font.SysFont("malgungothic", 70)

# 변수 선언과 초기화
idex = 0
over_1 = False

# 효과음
pygame.mixer.music.load(f'./music/ws.mp3') # 폰트와 같은 이유
pygame.mixer.music.play(-1)
snd_space_1 = pygame.mixer.Sound(f'./music/launch.mp3')
snd_space_2 = pygame.mixer.Sound(f'./music/H_hit.mp3')
snd_space_3 = pygame.mixer.Sound(f'./music/D_hit.mp3')
snd_space_4 = pygame.mixer.Sound(f'./music/bomb.mp3')
snd_space_5 = pygame.mixer.Sound(f'./music/hd.mp3')
# pygame.mixer.music.set_volume(0.1) #볼륨

#딕셔러리로 변수를 선언하여 정리한다. in과 같은 연산 같은 곳에서 리스트보다 빠름 리스트는 여러 타입의 데이터 저장 가능
#딕셔너리는 자료 분류와 정리를 편리하게 할 수 있다. 
val = {
        'active':True,
        'screen':(1200,800),
        'score':0,
        'player_delay':0,
        'devil_delay': 0,
        'wow.png' : (50, 50),
        'HP':30,
        'health_delay':0,
        'rich_delay':0,
        'over' : False,
        'boss_delay' : 0,
        'partmsg' :None,
        'partmsgtick' :0,
        'clearmsg' : None,
        'clearmsgtick' : 0,
        'emotick' : 0,
        'emomsg' : None,
         }
player_info = {
            'wepon':0,
            'fire_power':10,
            'white_power': 10,
            'black_power':10,
            'rich_level':1,
            'boar_level':1,
            'wepon_emo' : 10
}
bomb = {
    'bombtick' : 0,
    'bombmsg' : None,
}

arrows = []
devils = []
richs = []
bosses = []

items = []
clock = pygame.time.Clock()   
screen = pygame.display.set_mode(val['screen'])
arrtak = 10
richss = 30

#3.이미지 가져오기
# 1)배경
bg = pygame.image.load('./images/sp3.jpg').convert_alpha()
bg = pygame.transform.scale(bg, val['screen'])
bgx_1 = 0
bgx_2 = -1200

# 2)Player
file_player = ["./images/em1.png", "./images/em11.png"]


player_imgs = []
for file in file_player:
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img , (65, 120))
    img = pygame.transform.rotate(img , 10)
    # img = pygame.transform.flip(img)
    player_imgs.append(img)

bomblist = []
bomb = pygame.image.load('./images/wow.png').convert_alpha()
bomb = pygame.transform.scale(bomb , (90, 80))

# 3)이미지 좌표값 가져와서 재 설정하기
playerImgRec = player_imgs[0].get_rect() 
playerImgRec.centerx = val['screen'][0] - playerImgRec.width/2 - 10 #오른쪽 중간
playerImgRec.centery = val['screen'][1]/2

    
##=================================================
#3. 반복문
while(val['active']):
    bgx_1 += 1.5
    bgx_2 += 1.5
    screen.blit(bg, (bgx_1, 0))
    screen.blit(bg, (bgx_2, 0))
    
    
    # ellip = []
    
    # ellip.append(pygame.time.get_ticks())
    bx() #배경 코딩
    # ellip.append(pygame.time.get_ticks())
    # ellip.append(pygame.time.get_ticks())
    eventProcess() #키 이벤트 코딩
    # ellip.append(pygame.time.get_ticks())
    updatePlayer() #활 쏘는 장면 코딩
    # ellip.append(pygame.time.get_ticks())
    updateArrow() #화살이 날라가는 장면 연출
    # ellip.append(pygame.time.get_ticks())
    updateDevils() #악마 코딩
    # ellip.append(pygame.time.get_ticks())
    updateRichs() #리치 코딩
    # ellip.append(pygame.time.get_ticks())
    updateygr() #적을 죽일시 획득하는 아이템 코딩
    # ellip.append(pygame.time.get_ticks())
    setText() #게임 화면에 나오는 텍스트 코딩
    # ellip.append(pygame.time.get_ticks())
    gameover() #게임오버 화면 코딩
    # ellip.append(pygame.time.get_ticks())
    Box() #무기 텍스트 코딩
    emo()
    
    # ellp = ellip[0]
    # for i,ell in enumerate(ellip):
    #     if i != 0:
    #         print(f" {ell - ellp:05}",end=' ')
    #     ellp = ell
    # print()
    updateBosses() #보스 코딩
    part() #단계가 올라가는 기준 코딩
    pygame.display.update()
    clock.tick(400) #1초에 화면을 400번 그리기
    
    # pyinstaller -w -F .\play.py