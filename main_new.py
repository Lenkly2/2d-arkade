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
        global Location
        global Locationyx
        if Key[pygame.K_w] and self.rect.y > -50:
            if Locationy != "magaz":
                self.rect.y = self.rect.y - self.speed
            if Locationy == "magaz" and self.rect.y >= 250:
                self.rect.y = self.rect.y - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
            direct = "up"
            if self.rect.y < 0 and boss_fight == False and Locationy != 1 and Location < 4 and Locationy != "magaz" and Locationy > -1:
                Location += 1
                self.rect.y = window_height - self.h
            try:
                if self.rect.y < 0 and Locationy == -3 and Locationyx < 1:
                    Locationyx += 1
                    self.rect.y = window_height - self.h
                if self.rect.y < 0 and Locationy == -4 and Locationyx < 0:
                    Locationyx += 1
                    self.rect.y = window_height - self.h
            except:
                error = 1
        if Key[pygame.K_s] and self.rect.y < window_height - (self.h/2):
            if Locationy != "magaz":
                self.rect.y = self.rect.y + self.speed
            if Locationy == "magaz" and self.rect.y <= window_height-175:
                self.rect.y = self.rect.y + self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[1]),(self.w,self.h))
            direct = "down"
            if self.rect.y > window_height - self.h and boss_fight == False and Locationy == 0 and Location > 0:
                Location -= 1
                self.rect.y = 50
            try:
                if self.rect.y > window_height- self.h and Locationy <=-3:
                    if Locationy == -3 and Locationyx > 0:
                        Locationyx -= 1
                        self.rect.y = 0 + self.h
                    if Locationy == -4 and Locationyx > -3:
                        Locationyx -= 1
                        self.rect.y = 0 + self.h
            except:
                error = 1
        if Key[pygame.K_d] and self.rect.x < window_width - self.w:
            if Locationy != "magaz":
                self.rect.x = self.rect.x + self.speed
            if Locationy == "magaz" and self.rect.x <= window_width-100:
                self.rect.x = self.rect.x + self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[3]),(self.w,self.h))
            direct = "right"
            if self.rect.x >= window_width - self.w and boss_fight == False and Location == 1 and Locationy != "magaz":
                if Locationy > 0:
                    Locationy -=1
                    self.rect.x = 0 + self.w
            if self.rect.x >= window_width - self.w and Location == 3 and Locationy > -4: 
                Locationy -= 1
                self.rect.x = 0 + self.w
        if Key[pygame.K_a] and self.rect.x > 0:
            if Locationy != "magaz":
                self.rect.x = self.rect.x - self.speed
            if Locationy == "magaz" and self.rect.x >= 75:
                self.rect.x = self.rect.x - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[2]),(self.w,self.h))
            direct = "left"
            if self.rect.x <= 0 + self.w and boss_fight == False and Location == 1 and once_lock == 1 and Locationy != "magaz" :
                Locationy +=1
                self.rect.x = window_width - self.w
            try:
                if self.rect.x <= 0 + self.w and Locationy <= -1 and Location == 3:
                    Locationy +=1
                    self.rect.x = window_width - self.w
            except:
                error = 1

    def dash(self):
        if direct == "right":
            self.rect.x += 60
        if direct == "left":
            self.rect.x -= 60
        if direct == "up":
            self.rect.y -= 60
        if direct == "down":
            self.rect.y += 60
    def move_enemy(self):
        if self.rect.x < main_character.rect.x:
            self.rect.x += self.speed
        if self.rect.y < main_character.rect.y:
            self.rect.y += self.speed
        if self.rect.x > main_character.rect.x:
            self.rect.x -= self.speed
        if self.rect.y > main_character.rect.y:
            self.rect.y -= self.speed
    def enemy_attack(self):
        global time_for_Attack
        global pre_attack_time
        global dmgp
        global time_for_dmg
        if time.monotonic() - time_for_Attack >= 2:
            pre_attack_time = time.monotonic()+2
        
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[2]),(self.w,self.h))
            if main_character.rect.x - self.rect.x < self.w+15 and main_character.rect.x - self.rect.x > -self.w-15:
                if main_character.rect.y - self.rect.y < self.h+15 and main_character.rect.y - self.rect.y > -self.h-15:
                    main_character.hp -= self.damage
                    self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
                    pre_attack_time = time.monotonic()
                    time_for_Attack = time.monotonic()
            if time.monotonic() - time_for_Attack >= 2.3:
                self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
                pre_attack_time = time.monotonic()
                time_for_Attack = time.monotonic()
        if time.monotonic() - pre_attack_time >= 0.8:
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[5]),(self.w,self.h))
        if dmgp == 1:
            if time.monotonic() - time_for_dmg >= 2:
                    self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
                    time_for_dmg = time.monotonic()
                    dmgp = 0
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
                global boss_fight
                #func
                enemy_name.image = pygame.transform.scale(pygame.image.load(enemy_name.image_list[3]),(enemy_name.w,enemy_name.h))
                enemy_name.hp -= self.damage
                dmgp = 1
                if Locationy == -4 and Locationyx == -2:
                    boss_fight = True
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
background5 = pygame.transform.scale(pygame.image.load("ground4.png"),(window_width,window_height))
background6 = pygame.transform.scale(pygame.image.load("ground5.png"),(window_width,window_height))
background_right1 = pygame.transform.scale(pygame.image.load("ground_r.png"),(window_width,window_height))
background_right2 = pygame.transform.scale(pygame.image.load("ground_r2.png"),(window_width,window_height))
background_right3 = pygame.transform.scale(pygame.image.load("ground_r3.png"),(window_width,window_height))
background_boss = pygame.transform.scale(pygame.image.load("ground_boss.png"),(window_width,window_height))
background_boss2 = pygame.transform.scale(pygame.image.load("ground_boss2.png"),(window_width,window_height))
house = pygame.transform.scale(pygame.image.load("house.jpg"),(600,400))
house_in = pygame.transform.scale(pygame.image.load("house_in.jpg"),(window_width,window_height))
hearts = pygame.transform.scale(pygame.image.load("heart.png"),(25,25))
heart_img = pygame.transform.scale(pygame.image.load("heart.png"),(75,75))
coin = pygame.transform.scale(pygame.image.load("coin.png"),(25,25))
hotbar_img = pygame.transform.scale(pygame.image.load("hotbar.png"),(75,75))
sword_img = pygame.transform.scale(pygame.image.load("sword.png"),(75,75))
wand_img = pygame.transform.scale(pygame.image.load("magic_wand.png"),(75,75))
dash_img = pygame.transform.scale(pygame.image.load("dash.png"),(40,20))
button = pygame.transform.scale(pygame.image.load("button.png"),(50,50))
pygame.font.init()
# персонажі

main_images = ['main_character_back.png','main_character_front.png','main_character_left.png','main_character_right.png','main_character_right_attack.png',"main_character_left_attack.png","main_character_back_attack.png","main_character_front_attack.png"]
main_character = Owner(main_images[1],50,450,50,70,3,3,main_images,3)
golem_images = ['golem_left.png','golem_right.png','golem_attack.png','golem_left_dmg.png','golem_right_dmg.png','golem_pre_attack.png']
enemy_golem1 = Owner(golem_images[0],500,100,70,80,50,2,golem_images,1)
enemy_golem2 = Owner(golem_images[0],1500,200,70,80,50,2,golem_images,1)
enemy_golem3 = Owner(golem_images[0],1500,300,70,80,50,2,golem_images,1)
enemy_golem4 = Owner(golem_images[0],1500,100,70,80,50,2,golem_images,1)
enemy_golem5 = Owner(golem_images[0],1500,200,70,80,50,2,golem_images,1)
enemy_golem6 = Owner(golem_images[0],1500,300,70,80,50,2,golem_images,1)

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

#ціна в магазині
wand_price = 20
hp_price = 15
sword_price = 10
#змінні
direct = "up"
mfont = pygame.font.Font(None,20)
Fight = False
time_for_Attack = time.monotonic()
time_for_cooldown = time.monotonic()
time_for_style = time.monotonic()
dash_time = time.monotonic()
dash_col = 3
dmgp = 0
boss_fight = False
spawn = True
Loc = -1
attack_style = 0
once_attack = 0
tm = 5
once_lock = 1
hp_resiste = time.monotonic()
time_for_dmg = time.monotonic()
pre_attack_time = time.monotonic()
coins = 0
Location = 0
Locationy = 0
Locationyx = 0
hotbar = 1
shop = 0
magic_sharp = []
enemys_death = []
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
                if hotbar == 1:
                    if time.monotonic() - time_for_cooldown >= 0.7:
                        main_character.attack(enemy)
                        main_character.attack(enemy_golem1)
                        main_character.attack(enemy_golem2)
                        main_character.attack(enemy_golem3)
                        main_character.attack(enemy_golem4)
                        main_character.attack(enemy_golem5)
                        main_character.attack(enemy_golem6)
                        time_for_cooldown = time.monotonic()
        if Location == 4:
            m_b_x, m_b_y =  pygame.mouse.get_pos()       
            if m_b_x >= 60 and m_b_x <= 110:
                if m_b_y >= 250 and m_b_y <= 300:
                    if pygame.mouse.get_pressed()[0]:
                        enemy_golem1.rect.x = 200
                        enemy_golem2.rect.x = 200
                        enemy_golem3.rect.x = 200
                        enemy_golem4.rect.x = 600
                        enemy_golem5.rect.x = 600
                        enemy_golem6.rect.x = 600
        if Locationy == "magaz":
            m_p_x, m_p_y =  pygame.mouse.get_pos()         
            if m_p_x >= 95 and m_p_x <= 150:
                if m_p_y >= 150 and m_p_y <= 160:
                    if pygame.mouse.get_pressed()[0] and shop == 1:
                        if coins >= wand_price:
                            wand = 1
                            coins = coins - wand_price
            if m_p_x >= 195 and m_p_x <= 250:
                if m_p_y >= 150 and m_p_y <= 160:
                    if pygame.mouse.get_pressed()[0] and shop == 1:
                        if coins >= hp_price and main_heart <= 50:
                            main_character.hp += 2
                            main_heart += 2
                            coins = coins - hp_price
            if m_p_x >= 295 and m_p_x <= 350:
                if m_p_y >= 150 and m_p_y <= 160:
                    if pygame.mouse.get_pressed()[0] and shop == 1:
                        if coins >= sword_price:
                            main_character.damage += 1
                            coins = coins - sword_price

    
        if e.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_1]:
                hotbar = 1
            if key[pygame.K_2]:
                hotbar = 2
            if key[pygame.K_3]:
                hotbar = 3
            if key[pygame.K_SPACE]:
                if dash_col > 0:
                    main_character.dash()
                    dash_col -= 1
            if key[pygame.K_e] and main_character.rect.x > 330 and main_character.rect.x < 400 and main_character.rect.y > 220 and main_character.rect.y < 260:
                if Locationy == 1 or Locationy == -3 and Locationyx == 1:
                    Locationy = "magaz"
            if key[pygame.K_e] and main_character.rect.x > 100 and main_character.rect.x < 150 and main_character.rect.y > 340 and main_character.rect.y < 440:
                if Locationy == "magaz":
                    Locationy = 1
                if Locationyx == 1:
                    Locationy = -3
            if key[pygame.K_f]:
                if Locationy == "magaz" and main_character.rect.x > 230 and main_character.rect.x < 320 and main_character.rect.y > 250 and main_character.rect.y < 300:
                    shop = 1
                if Locationy != "magaz" or main_character.rect.x < 230 or main_character.rect.x > 320 or main_character.rect.y < 250 or main_character.rect.y > 300:
                    shop = 0   
    #відновлення ривка
    if time.monotonic() - dash_time >= 5:
        if dash_col < 3:
            dash_col += 1
        dash_time = time.monotonic()
    #фон локацій
    if Location == 0:
        window.blit(background1,(0,0))
    if Location == 1:
        if Locationy == 0:
            window.blit(background2,(0,0))
        #магаз
        if Locationy == 1:
            window.blit(background4,(0,0))
            window.blit(house,(100,50))
            once_lock = 0
        if Locationy == "magaz":
            window.blit(house_in,(0,0))
            if shop == 1:
                window.blit(hotbar_img,(100,75))
                window.blit(wand_img,(100,75))
                window.blit(coin,(100,30))
                window.blit(mfont.render(str(wand_price),True,(0,0,0)),(130,30))
                window.blit(mfont.render("Купити",True,(0,0,0)),(100,150))

                window.blit(hotbar_img,(200,75))
                window.blit(heart_img,(200,75))
                window.blit(mfont.render(str(hp_price),True,(0,0,0)),(230,30))
                window.blit(mfont.render("Купити",True,(0,0,0)),(200,150))
                window.blit(coin,(200,30))

                window.blit(hotbar_img,(300,75))
                window.blit(sword_img,(300,75))
                window.blit(coin,(300,30))
                window.blit(mfont.render(str(sword_price),True,(0,0,0)),(330,30))
                window.blit(mfont.render("Купити",True,(0,0,0)),(300,150))
            once_lock = 0
        if Locationy != 1 and Locationy != "magaz":
            once_lock = 1

    if Location == 2:
        window.blit(background3,(0,0))
    if Location == 3:
        if Locationy == 0:
            window.blit(background5,(0,0))
        if Locationy == -1:
            window.blit(background_right1,(0,0))
        if Locationy == -2:
            window.blit(background_boss,(0,0))
        if Locationy == -3:
            if Locationyx == 0:
                window.blit(background_right2,(0,0))
            if Locationyx >= 1:
                window.blit(background4,(0,0))
                window.blit(house,(100,50))
        if Locationy == "magaz":
            window.blit(house_in,(0,0))
            if shop == 1:
                window.blit(hotbar_img,(100,75))
                window.blit(wand_img,(100,75))
                window.blit(coin,(100,30))
                window.blit(mfont.render(str(wand_price),True,(0,0,0)),(130,30))
                window.blit(mfont.render("Купити",True,(0,0,0)),(100,150))

                window.blit(hotbar_img,(200,75))
                window.blit(heart_img,(200,75))
                window.blit(mfont.render(str(hp_price),True,(0,0,0)),(230,30))
                window.blit(mfont.render("Купити",True,(0,0,0)),(200,150))
                window.blit(coin,(200,30))

                window.blit(hotbar_img,(300,75))
                window.blit(sword_img,(300,75))
                window.blit(coin,(300,30))
                window.blit(mfont.render(str(sword_price),True,(0,0,0)),(330,30))
                window.blit(mfont.render("Купити",True,(0,0,0)),(300,150))
        if Locationy == -4:
            if Locationyx == 0:
                window.blit(background_right3,(0,0))
            if Locationyx == -1:
                window.blit(background1,(0,0))
            if Locationyx == -2:
                window.blit(background_boss2,(0,0))
            if Locationyx <= -3:
                window.blit(background4,(0,0))
    if Location >= 4:
        window.blit(background6,(0,0))
        window.blit(button,(60,250))
    # ворог на локації
    if Location == 0:
        enemy = enemy_golem1
        try:
            if enemys_death.index(0):
                spawn = False
        except:
            if spawn == True:
                enemy.rect.x = 500
                enemy.hp = 50
    if Location == 1:
        chest.reset()
        try:
            if enemys_death.index(1):
                spawn = False
        except:
            if spawn == True and Locationy == 0:
                if chest.hp > 0:
                    chest.rect.x = 200
            if chest.hp < 0 or Locationy != 0:
                chest.rect.x = 1000

        if Fight == False:
            if enemy == enemy_golem1:
                enemy.rect.x = 1000
            enemy = chest

    if Location == 2:
        enemy = enemy_golem1
        try:
            if enemys_death.index(2):
                spawn = False
        except:
            if spawn == True:
                enemy.rect.x = 500
                enemy.hp = 50

    if Location == 3:
        #під нові локації
        enemy = enemy_golem1
        try:
            if enemys_death.index(3):
                spawn = False
        except:
            if spawn == True:
                enemy.rect.x = 500
                enemy.hp = 50
            
    # виведення
    enemy_golem1.reset()
    enemy_golem2.reset()
    enemy_golem3.reset()
    enemy_golem4.reset()
    enemy_golem5.reset()
    enemy_golem6.reset()
    main_character.reset()
    window.blit(mfont.render(str(enemy.hp),True,(0,0,0)),(enemy.rect.x,enemy.rect.y))
    window.blit(mfont.render(str(enemy_golem1.hp),True,(0,0,0)),(enemy_golem1.rect.x,enemy_golem1.rect.y))
    window.blit(mfont.render(str(enemy_golem2.hp),True,(0,0,0)),(enemy_golem2.rect.x,enemy_golem2.rect.y))
    window.blit(mfont.render(str(enemy_golem3.hp),True,(0,0,0)),(enemy_golem3.rect.x,enemy_golem3.rect.y))
    window.blit(mfont.render(str(enemy_golem4.hp),True,(0,0,0)),(enemy_golem4.rect.x,enemy_golem4.rect.y))
    window.blit(mfont.render(str(enemy_golem5.hp),True,(0,0,0)),(enemy_golem5.rect.x,enemy_golem5.rect.y))
    window.blit(mfont.render(str(enemy_golem6.hp),True,(0,0,0)),(enemy_golem6.rect.x,enemy_golem6.rect.y))
    window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(30,10))
    window.blit(mfont.render(str(coins),True,(0,0,0)),(30,40))
    window.blit(hearts,(5,10))
    window.blit(coin,(5,30))
    window.blit(hotbar_img,(window_width-80,15))
    window.blit(hotbar_img,(window_width-80,90))
    window.blit(hotbar_img,(window_width-80,165))
    window.blit(sword_img,(window_width-80,15))
    if dash_col == 3:
        window.blit(dash_img,(110,window_height-40))
    if dash_col >= 2:
        window.blit(dash_img,(60,window_height-40))
    if dash_col >= 1:
        window.blit(dash_img,(10,window_height-40))
    # функції
    if Location == Loc:
        spawn = False
    if Location != Loc:
        spawn = True

    if Fight == True:
        if Location != 4:
            if enemy != chest:
                enemy.move_enemy()
                #????
                if main_character.hp <= 0:
                    enemy.hp = 50
                    main_character.rect.y = window_height - main_character.h
                    main_character.hp = main_heart
                    Fight = False
                Loc = Location
                enemy.enemy_attack()

                if enemy.hp <= 0:
                    enemy.rect.x = 1000
                    coins += 5
                    enemys_death.append(Location)
                    Fight = False
                    main_character.hp = main_heart
        if Location == 4:
            enemy_golem1.move_enemy()
            enemy_golem2.move_enemy()
            enemy_golem3.move_enemy()
            enemy_golem4.move_enemy()
            enemy_golem5.move_enemy()
            enemy_golem6.move_enemy()

            enemy_golem1.enemy_attack()
            enemy_golem2.enemy_attack()
            enemy_golem3.enemy_attack()
            enemy_golem4.enemy_attack()
            enemy_golem5.enemy_attack()
            enemy_golem6.enemy_attack()
            if main_character.hp <= 0:
                enemy.hp = 50
                main_character.rect.y = window_height - main_character.h
                main_character.hp = main_heart
                Fight = False

        if enemy == chest:
            if enemy.hp <= 0:
                enemy.rect.x = 1000
                coins += 5
                Loc = Location
                Fight = False
    clock.tick(100)
    main_character.move()
    pygame.display.update()



# if Boss_Fight == True:
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