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
        if Key[pygame.K_w] and self.rect.y > -50:
            self.rect.y = self.rect.y - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
            if self.rect.y < 0 and Fight == False and enemy_death == True:
                global Location
                Location += 1
                self.rect.y = window_height - self.h
        if Key[pygame.K_s] and self.rect.y < window_height + self.h:
            self.rect.y = self.rect.y + self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[1]),(self.w,self.h))
            if self.rect.y > window_height - self.h and Fight == False:
                if Location > 0:
                    Location -= 1
                self.rect.y = 50
        if Key[pygame.K_d] and self.rect.x < window_width - self.w:
            self.rect.x = self.rect.x + self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[3]),(self.w,self.h))
        if Key[pygame.K_a] and self.rect.x > 0:
            self.rect.x = self.rect.x - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[2]),(self.w,self.h))

    def attack(self,enemy_name):
        self.image = pygame.transform.scale(pygame.image.load(self.image_list[4]),(self.w,self.h))
        if self.rect.x - enemy_name.rect.x < 150 and self.rect.x - enemy_name.rect.x > -30:
          
            if self.rect.y - enemy_name.rect.y < 155 and self.rect.y - enemy_name.rect.y > - 20:

                enemy_name.image = pygame.transform.scale(pygame.image.load(enemy_name.image_list[3]),(enemy_name.w,enemy_name.h))
                enemy_name.hp -= self.damage
                global dmgp
                dmgp = 1
                global Fight
                global enemy_death
                enemy_death = False
                global chest_fight
                if enemy == chest:
                    chest_fight = True
                else:
                    Fight = True
                time_for_Attack_player = time.monotonic()
                    

# вікно
window_width = 800
window_height = 600            
window = pygame.display.set_mode((window_width,window_height))
background1 = pygame.transform.scale(pygame.image.load("ground.png"),(window_width,window_height))
background2 = pygame.transform.scale(pygame.image.load("ground2.png"),(window_width,window_height))
background3 = pygame.transform.scale(pygame.image.load("ground3.png"),(window_width,window_height))
pygame.font.init()
# персонажі

main_images = ['main_character_back.png','main_character_front.png','main_character_left.png','main_character_right.png','main_character_right_attack.png']
main_character = Owner(main_images[1],50,450,50,70,3,2,main_images,3)
golem_images = ['golem_left.png','golem_right.png','golem_attack.png','golem_left_dmg.png']
enemy_golem = Owner(golem_images[0],600,50,70,80,50,3,golem_images,1)
chest_images = ['chest.png','chest.png','chest.png','chest.png']
chest = Owner(chest_images[0],1000,200,90,80,3,0,chest_images,None)
bl_atacck = ['attack_bl_right.png','attack_bl_up.png']
block_atack = Owner(bl_atacck[1],1000,200,30,80,0,5,bl_atacck,1)
block_atack1 = Owner(bl_atacck[1],1000,200,30,80,0,5,bl_atacck,1)
block_atack2 = Owner(bl_atacck[0],1000,200,80,30,0,5,bl_atacck,1)
block_atack3 = Owner(bl_atacck[0],1000,200,80,30,0,5,bl_atacck,1)
block_atack4 = Owner(bl_atacck[0],1000,200,80,30,0,5,bl_atacck,1)
block_atack5 = Owner(bl_atacck[0],1000,200,80,30,0,5,bl_atacck,1)
block_atack6 = Owner(bl_atacck[0],1000,200,80,30,0,5,bl_atacck,1)
block_atack7 = Owner(bl_atacck[0],1000,200,80,30,0,5,bl_atacck,1)

#змінні
mfont = pygame.font.Font(None,20)
global Fight
Fight = False
global time_for_Attack
time_for_Attack = time.monotonic()
global time_for_Attack_player
time_for_Attack_player = time.monotonic()
time_for_style = time.monotonic()
dmgp = 0
Location = 0
enemy_death = False
chest_fight = False
spawn = True
Loc = 0
attack_style = 0
once_attack = 0
tm = 5
hp_resiste = time.monotonic()
hp_resister = 0
# гра
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if time.monotonic() - time_for_Attack_player >= 1:
                    main_character.attack(enemy)
                    time_for_Attack_player = time.monotonic()

    #фон локацій
    if Location == 0:
        window.blit(background1,(0,0))
        window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(20,10))
    if Location == 1:
        window.blit(background2,(0,0))
        window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(20,10))
        if spawn == True:
            if main_character.damage < 5:
                chest.rect.x = 200

    if Location >= 2:
        window.blit(background3,(0,0))
        window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(20,10))
        
    # ворог на локації
    if Location == 0:
        enemy = enemy_golem
        window.blit(mfont.render(str(enemy.hp),True,(0,0,0)),(enemy.rect.x,enemy.rect.y))
    if Location == 1:
        #під нові локації
        enemy = chest
    if Location >= 2:
        #під нові локації
        enemy = enemy_golem
        window.blit(mfont.render(str(enemy.hp),True,(0,0,0)),(enemy.rect.x,enemy.rect.y))
        if spawn == True:
            enemy.rect.x = 500
            enemy.hp = 80
            enemy.w = 70
            enemy.h = 80
            enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))

    # виведення
    main_character.reset()
    if Location == 0:
        enemy_golem.reset()
        
    if Location == 1:
        #під нові локації
        chest.reset()
    if Location >= 2:
        #під нові локації
        enemy_golem.reset()

    # функції
    if Location == Loc:
        spawn = False
    else:
        spawn = True

    if chest_fight == True:
        if enemy.hp <= 0:
            enemy.rect.x = 1000
            main_character.damage += 2
            enemy_death = True
            Loc = Location
            chest_fight = False
    
    if Fight == True:
        #відображення атаки
        block_atack.reset()
        block_atack1.reset()
        block_atack2.reset()
        block_atack3.reset()
        block_atack4.reset()
        block_atack5.reset()
        block_atack6.reset()
        block_atack7.reset()
        #????
        Loc = Location
        enemy.rect.x = 350
        enemy.rect.y = 250
        enemy.w = 150
        enemy.h = 200
        if time.monotonic() - time_for_style >= tm:
            attack_style = random.randint(0,1)
            once_attack = 1
            if attack_style == 0:
                tm = 5
                time_for_style = time.monotonic()
            if attack_style == 1:
                tm = 10
                time_for_style = time.monotonic()


        if attack_style == 0:
            if time.monotonic() - time_for_Attack >= 6:
                enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
                time_for_Attack = time.monotonic()
            if time.monotonic() - time_for_Attack >= 4:
                enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[2]),(enemy.w,enemy.h))
                if main_character.rect.x - enemy.rect.x < 180 and main_character.rect.x - enemy.rect.x > -40:
                    if main_character.rect.y - enemy.rect.y < 170 and main_character.rect.y - enemy.rect.y > - 30:
                        main_character.hp -= enemy.damage
                time_for_Attack = time.monotonic()
        if attack_style == 1:

                
            if once_attack == 1:
                block_atack.rect.x = enemy.rect.x+60
                block_atack.rect.y = enemy.rect.y-80

                block_atack1.rect.x = enemy.rect.x+60
                block_atack1.rect.y = enemy.rect.y+220

                block_atack2.rect.x = enemy.rect.x-80
                block_atack2.rect.y = enemy.rect.y+80

                block_atack3.rect.x = enemy.rect.x+160
                block_atack3.rect.y = enemy.rect.y+80

                once_attack = 0
                time_for_Attack = time.monotonic()
            if time.monotonic() - time_for_Attack >= 1: 
                block_atack.rect.x = 1000
                block_atack1.rect.x = 1000
                block_atack2.rect.x = 1000
                block_atack3.rect.x = 1000
                block_atack4.rect.x = 1000
                block_atack5.rect.x = 1000
                block_atack6.rect.x = 1000
                block_atack7.rect.x = 1000
                
            if time.monotonic() - time_for_Attack >= 2: 
                block_atack.rect.x = enemy.rect.x+60
                block_atack1.rect.x = enemy.rect.x+60
                block_atack2.rect.x = enemy.rect.x-80
                block_atack3.rect.x = enemy.rect.x+160
                time_for_Attack = time.monotonic()+5
            if time.monotonic() - time_for_style >= 3: 
                block_atack2.rect.x -= 5
                block_atack3.rect.x += 5
                block_atack.rect.y -= 5
                block_atack1.rect.y += 5
                if pygame.sprite.collide_rect(main_character,block_atack) or pygame.sprite.collide_rect(main_character,block_atack1) or pygame.sprite.collide_rect(main_character,block_atack2) or pygame.sprite.collide_rect(main_character,block_atack3):
                    hp_resister = 1
                if hp_resister == 1:
                    if time.monotonic() - hp_resiste >= 2:
                        main_character.hp -= 1
                        hp_resiste = time.monotonic()
            
            if time.monotonic() - time_for_style >= 6:
                block_atack.rect.x = 1000
                block_atack1.rect.x = 1000
                block_atack2.rect.x = 1000
                block_atack3.rect.x = 1000
                block_atack4.rect.x = 1000
                block_atack5.rect.x = 1000
                block_atack6.rect.x = 1000
                block_atack7.rect.x = 1000
                time_for_Attack = time.monotonic()
        if dmgp == 1:
            if time.monotonic() - time_for_Attack >= 1:
                    enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
                    time_for_Attack = time.monotonic()
                    dmgp = 0

        if enemy.hp <= 0:
            enemy.w = 70
            enemy.h = 80
            enemy.rect.x = 1000
            enemy_death = True
            Fight = False
            main_character.hp = 3
        


    main_character.move()
    pygame.display.update()
