import pygame
import random
import time

class Owner():
    def __init__(self,image_player,x,y,w,h,hp,speed,image_list,damage):
        self.image = pygame.transform.scale(pygame.image.load(image_player),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.speed = speed
        self.image_list = image_list
        self.damage = damage
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        Key = pygame.key.get_pressed()
        global Locationy
        global once_lock
        global direct
        if Key[pygame.K_w] and self.rect.y > -50:
            if Locationy != "magaz":
                self.rect.y = self.rect.y - self.speed
            if Locationy == "magaz" and self.rect.y >= 250:
                self.rect.y = self.rect.y - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
            direct = "up"
            if self.rect.y < 0 and Fight == False and Locationy == 0:
                global Location
                Location += 1
                self.rect.y = window_height - self.h
        if Key[pygame.K_s] and self.rect.y < window_height - (self.h/2):
            if Locationy != "magaz":
                self.rect.y = self.rect.y + self.speed
            if Locationy == "magaz" and self.rect.y <= window_height-175:
                self.rect.y = self.rect.y + self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[1]),(self.w,self.h))
            direct = "down"
            if self.rect.y > window_height - self.h and Fight == False and Locationy == 0:
                if Location > 0:
                    Location -= 1
                self.rect.y = 50
        if Key[pygame.K_d] and self.rect.x < window_width - self.w:
            if Locationy != "magaz":
                self.rect.x = self.rect.x + self.speed
            if Locationy == "magaz" and self.rect.x <= window_width-100:
                self.rect.x = self.rect.x + self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[3]),(self.w,self.h))
            direct = "right"
            if self.rect.x >= window_width - self.w and Fight == False and Location == 1 and Locationy != "magaz":
                if Locationy > 0:
                    Locationy -=1
                    self.rect.x = 0 + self.w
        if Key[pygame.K_a] and self.rect.x > 0:
            if Locationy != "magaz":
                self.rect.x = self.rect.x - self.speed
            if Locationy == "magaz" and self.rect.x >= 75:
                self.rect.x = self.rect.x - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[2]),(self.w,self.h))
            direct = "left"
            if self.rect.x <= 0 + self.w and Fight == False and Location == 1 and once_lock == 1 and Locationy != "magaz":
                Locationy +=1
                self.rect.x = window_width - self.w

    def dash(self):
        if direct == "right":
            self.rect.x += 60
        if direct == "left":
            self.rect.x -= 60
        if direct == "up":
            self.rect.y -= 60
        if direct == "down":
            self.rect.y += 60

    def attack(self,enemy_name):
        if direct == "right":
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[4]),(self.w,self.h))
        if direct == "left":
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[5]),(self.w,self.h))
        if direct == "up":
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[6]),(self.w,self.h))
        if direct == "down":
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[7]),(self.w,self.h))

        if self.rect.x - enemy_name.rect.x < enemy.w+10 and self.rect.x - enemy_name.rect.x > -enemy.w-10:
            if self.rect.y - enemy_name.rect.y < enemy.h+10 and self.rect.y - enemy_name.rect.y > -enemy.h-10:
                #global
                global dmgp
                global Fight
                global enemy_death
                global chest_fight
                #func
                enemy_name.image = pygame.transform.scale(pygame.image.load(enemy_name.image_list[3]),(enemy_name.w,enemy_name.h))
                enemy_name.hp -= self.damage
                dmgp = 1
                enemy_death = False
                if enemy == chest:
                    chest_fight = True
                else:
                    Fight = True

# вікно
window_width = 800
window_height = 600            
window = pygame.display.set_mode((window_width,window_height))
background1 = pygame.transform.scale(pygame.image.load("ground.png"),(window_width,window_height))
background2 = pygame.transform.scale(pygame.image.load("ground2.png"),(window_width,window_height))
background3 = pygame.transform.scale(pygame.image.load("ground3.png"),(window_width,window_height))
background4 = pygame.transform.scale(pygame.image.load("ground_magaz.png"),(window_width,window_height))
house = pygame.transform.scale(pygame.image.load("house.jpg"),(600,400))
house_in = pygame.transform.scale(pygame.image.load("house_in.jpg"),(window_width,window_height))
hearts = pygame.transform.scale(pygame.image.load("heart.png"),(25,25))
heart_img = pygame.transform.scale(pygame.image.load("heart.png"),(75,75))
coin = pygame.transform.scale(pygame.image.load("coin.png"),(25,25))
hotbar_img = pygame.transform.scale(pygame.image.load("hotbar.png"),(75,75))
sword_img = pygame.transform.scale(pygame.image.load("sword.png"),(75,75))
wand_img = pygame.transform.scale(pygame.image.load("magic_wand.png"),(75,75))
dash_img = pygame.transform.scale(pygame.image.load("dash.png"),(40,20))
pygame.font.init()
# персонажі

main_images = ['main_character_back.png','main_character_front.png','main_character_left.png','main_character_right.png','main_character_right_attack.png',"main_character_left_attack.png","main_character_back_attack.png","main_character_front_attack.png"]
main_character = Owner(main_images[1],50,450,50,70,3,3,main_images,3)
golem_images = ['golem_left.png','golem_right.png','golem_attack.png','golem_left_dmg.png','golem_right_dmg.png','golem_pre_attack.png']
enemy_golem = Owner(golem_images[0],500,100,70,80,50,2,golem_images,1)
chest_images = ['chest.png','chest.png','chest.png','chest.png']
chest = Owner(chest_images[0],1000,200,90,80,3,0,chest_images,None)
bl_atacck = ['attack_bl_right.png','attack_bl_up.png','attack_bl_upr.png','attack_bl_upl.png']
block_atack = Owner(bl_atacck[1],1000,200,20,60,0,5,bl_atacck,1)
block_atack1 = Owner(bl_atacck[1],1000,200,20,60,0,5,bl_atacck,1)
block_atack2 = Owner(bl_atacck[0],1000,200,60,20,0,5,bl_atacck,1)
block_atack3 = Owner(bl_atacck[0],1000,200,60,20,0,5,bl_atacck,1)
block_atack4 = Owner(bl_atacck[2],1000,200,55,55,0,5,bl_atacck,1)
block_atack5 = Owner(bl_atacck[2],1000,200,55,55,0,5,bl_atacck,1)
block_atack6 = Owner(bl_atacck[3],1000,200,55,55,0,5,bl_atacck,1)
block_atack7 = Owner(bl_atacck[3],1000,200,55,55,0,5,bl_atacck,1)

#змінні
direct = "up"
mfont = pygame.font.Font(None,20)
Fight = False
time_for_Attack = time.monotonic()
time_for_Attack_player = time.monotonic()
time_for_style = time.monotonic()
dash_time = time.monotonic()
dash_col = 3
dmgp = 0
Location = 0
enemy_death = False
chest_fight = False
spawn = True
Loc = 0
attack_style = 0
once_attack = 0
tm = 5
once_lock = 1
hp_resiste = time.monotonic()
time_for_dmg = time.monotonic()
pre_attack_time = time.monotonic()
hp_resister = 0
coins = 0
death = 0
Locationy = 0
hotbar = 0
shop = 0
magic_sharp = []
main_heart = 3
clock = pygame.time.Clock()

# гра
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if time.monotonic() - time_for_Attack_player >= 0.7:
                    main_character.attack(enemy)
                    time_for_Attack_player = time.monotonic()
        if e.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                if dash_col > 0:
                    main_character.dash()
                    dash_col -= 1
            if key[pygame.K_e] and main_character.rect.x > 330 and main_character.rect.x < 400 and main_character.rect.y > 220 and main_character.rect.y < 260:
                if Locationy == 1:
                    Locationy = "magaz"

            if key[pygame.K_e] and main_character.rect.x > 100 and main_character.rect.x < 150 and main_character.rect.y > 340 and main_character.rect.y < 380:
                if Locationy == "magaz":
                    Locationy = 1
            if key[pygame.K_f]:
                if Locationy == "magaz" and main_character.rect.x > 230 and main_character.rect.x < 320 and main_character.rect.y > 250 and main_character.rect.y < 300:
                    shop = 1
                if Locationy != "magaz":
                    shop = 0
    #відновлення ривка
    if time.monotonic() - dash_time >= 5:
        if dash_col < 3:
            dash_col += 1
        dash_time = time.monotonic()
    
    #возродження
    if death == 1:
        death = 0
    #фон локацій
    if Location == 0:
        window.blit(background1,(0,0))

    if Location == 1:
        if Locationy == 0:
            window.blit(background2,(0,0))
        if spawn == True and Locationy == 0:
            if chest.hp > 0:
                chest.rect.x = 200
        else:
            chest.rect.x = 1000
        #магаз
        if Locationy == 1:
            window.blit(background4,(0,0))
            window.blit(house,(100,50))
            once_lock = 0
        if Locationy == "magaz":
            window.blit(house_in,(0,0))
            if shop == 1:
                window.blit(hotbar_img,(100,100))
                window.blit(wand_img,(100,100))
                window.blit(coin,(100,30))
                window.blit(hotbar_img,(200,100))
                window.blit(heart_img,(200,100))
                window.blit(coin,(200,30))
                window.blit(hotbar_img,(300,100))
                window.blit(coin,(300,30))
            once_lock = 0
        if Locationy != 1 and Locationy != "magaz":
            once_lock = 1

    if Location == 2:
        window.blit(background3,(0,0))

    if Location >= 3:
        window.blit(background3,(0,0))

    # ворог на локації
    if Location == 0:
        enemy = enemy_golem
        enemy_golem.reset()

    if Location == 1:
        enemy = chest
        chest.reset()

    if Location == 2:
        enemy = enemy_golem
        enemy_golem.reset()
        if spawn == True:
            enemy.rect.x = 500
            enemy.hp = 80

    if Location >= 3:
        #під нові локації
        enemy = enemy_golem
        enemy_golem.reset()
        if spawn == True:
            enemy.rect.x = 500
            enemy.hp = 80
            
    # виведення
    main_character.reset()
    window.blit(mfont.render(str(enemy.hp),True,(0,0,0)),(enemy.rect.x,enemy.rect.y))
    window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(30,10))
    window.blit(mfont.render(str(coins),True,(0,0,0)),(30,40))
    window.blit(hearts,(5,10))
    window.blit(coin,(5,30))
    window.blit(hotbar_img,(window_width-75,15))
    window.blit(hotbar_img,(window_width-75,90))
    window.blit(hotbar_img,(window_width-75,165))
    window.blit(sword_img,(window_width-75,15))
    if dash_col == 3:
        window.blit(dash_img,(110,window_height-40))
    if dash_col >= 2:
        window.blit(dash_img,(60,window_height-40))
    if dash_col >= 1:
        window.blit(dash_img,(10,window_height-40))
    # функції
    
    if Location == Loc:
        spawn = False
    else:
        spawn = True

    if chest_fight == True:
        if enemy.hp <= 0:
            enemy.rect.x = 1000
            coins += 5
            enemy_death = True
            Loc = Location
            chest_fight = False
    
    if Fight == True:
        direct_enemy_x = main_character.rect.x
        direct_enemy_y = main_character.rect.y
        if enemy.rect.x < direct_enemy_x:
            enemy.rect.x += enemy.speed
        if enemy.rect.y < direct_enemy_y:
            enemy.rect.y += enemy.speed
        if enemy.rect.x > direct_enemy_x:
            enemy.rect.x -= enemy.speed
        if enemy.rect.y > direct_enemy_y:
            enemy.rect.y -= enemy.speed
        #????
        if main_character.hp <= 0:
            death = 1
        if death == 1:
            enemy.hp = 50
            main_character.rect.y = window_height - main_character.h
            main_character.hp = main_heart
            Fight = False
        Loc = Location
        if attack_style == 0:
            if time.monotonic() - time_for_Attack >= 2.5:
                pre_attack_time = time.monotonic()+2
                enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[2]),(enemy.w,enemy.h))
                if main_character.rect.x - enemy.rect.x < enemy.w+15 and main_character.rect.x - enemy.rect.x > -enemy.w-15:
                    if main_character.rect.y - enemy.rect.y < enemy.h+15 and main_character.rect.y - enemy.rect.y > -enemy.h-15:
                        main_character.hp -= enemy.damage
                    pre_attack_time = time.monotonic()
                    enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
                    time_for_Attack = time.monotonic()
            if time.monotonic() - pre_attack_time >= 1:
                enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[5]),(enemy.w,enemy.h))

        if dmgp == 1:
            if time.monotonic() - time_for_dmg >= 2:
                    enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
                    time_for_dmg = time.monotonic()
                    dmgp = 0

        if enemy.hp <= 0:
            enemy.rect.x = 1000
            coins += 5
            enemy_death = True
            Fight = False
            main_character.hp = 3
        
    clock.tick(100)
    main_character.move()
    pygame.display.update()



# if Fight == True:
#         #відображення атаки
#         block_atack.reset()
#         block_atack1.reset()
#         block_atack2.reset()
#         block_atack3.reset()
#         block_atack4.reset()
#         block_atack5.reset()
#         block_atack6.reset()
#         block_atack7.reset()
#         #????
#         if main_character.hp <= 0:
#             death = 1
#         if death == 1:
#             enemy.hp = 50
#             main_character.rect.y = window_height - main_character.h
#             main_character.hp = main_heart
#             Fight = False
#         Loc = Location
#         if time.monotonic() - time_for_style >= tm:
#             attack_style = random.randint(0,1)
#             once_attack = 1
#             if attack_style == 0:
#                 tm = 5
#                 time_for_style = time.monotonic()
#             if attack_style == 1:
#                 tm = 6
#                 time_for_style = time.monotonic()

#         if attack_style == 0:
#             if time.monotonic() - time_for_Attack >= 5:
#                 enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
#                 time_for_Attack = time.monotonic()
#                 pre_attack_time = time.monotonic()
#             if time.monotonic() - time_for_Attack >= 3:
#                 pre_attack_time = time.monotonic()+5
#                 enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[2]),(enemy.w,enemy.h))
#                 if main_character.rect.x - enemy.rect.x < enemy.w+15 and main_character.rect.x - enemy.rect.x > -enemy.w-15:
#                     if main_character.rect.y - enemy.rect.y < enemy.h+15 and main_character.rect.y - enemy.rect.y > -enemy.h-15:
#                         main_character.hp -= enemy.damage
#                     time_for_Attack = time.monotonic()
#             if time.monotonic() - pre_attack_time >= 1:
#                 enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[5]),(enemy.w,enemy.h))
#         if attack_style == 1:
#             if once_attack == 1:
#                 enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
#                 block_atack.rect.x = enemy.rect.x+enemy.w-(enemy.w/2)
#                 block_atack.rect.y = enemy.rect.y-enemy.h

#                 block_atack1.rect.x = enemy.rect.x+enemy.w-(enemy.w/2)
#                 block_atack1.rect.y = enemy.rect.y+enemy.h

#                 block_atack2.rect.x = enemy.rect.x-enemy.w
#                 block_atack2.rect.y = enemy.rect.y+enemy.h-(enemy.h/2)

#                 block_atack3.rect.x = enemy.rect.x+enemy.w
#                 block_atack3.rect.y = enemy.rect.y+enemy.h-(enemy.h/2)

#                 once_attack = 0
#                 time_for_Attack = time.monotonic()
                
#             if time.monotonic() - time_for_Attack >= 1.5: 
#                 block_atack.rect.x = enemy.rect.x+enemy.w-(enemy.w/2)
#                 block_atack1.rect.x = enemy.rect.x+enemy.w-(enemy.w/2)
#                 block_atack2.rect.x = enemy.rect.x-enemy.w
#                 block_atack3.rect.x = enemy.rect.x+enemy.w
#                 time_for_Attack = time.monotonic()+5
                
#             if time.monotonic() - time_for_style >= 2.5: 
#                 block_atack2.rect.x -= 5
#                 block_atack3.rect.x += 5
#                 block_atack.rect.y -= 5
#                 block_atack1.rect.y += 5

#                 if pygame.sprite.collide_rect(main_character,block_atack) or pygame.sprite.collide_rect(main_character,block_atack1) or pygame.sprite.collide_rect(main_character,block_atack2) or pygame.sprite.collide_rect(main_character,block_atack3):
#                     if time.monotonic() - hp_resiste >= 2:
#                         main_character.hp -= 1
#                         hp_resiste = time.monotonic()
            
#             if time.monotonic() - time_for_style >= 5:
#                 block_atack.rect.x = 1000
#                 block_atack1.rect.x = 1000
#                 block_atack2.rect.x = 1000
#                 block_atack3.rect.x = 1000
#                 block_atack4.rect.x = 1000
#                 block_atack5.rect.x = 1000
#                 block_atack6.rect.x = 1000
#                 block_atack7.rect.x = 1000
#                 time_for_Attack = time.monotonic()

#         if dmgp == 1:
#             if time.monotonic() - time_for_dmg >= 2:
#                     enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
#                     time_for_dmg = time.monotonic()
#                     dmgp = 0

#         if enemy.hp <= 0:
#             enemy.rect.x = 1000
#             coins += 5
#             enemy_death = True
#             Fight = False
#             main_character.hp = 3