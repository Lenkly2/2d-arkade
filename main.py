import pygame
import random
import time

class Owner():
    def __init__(self,image_player,x,y,w,h,hp,speed,image_list):
        self.image = pygame.transform.scale(pygame.image.load(image_player),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.speed = speed
        self.image_list = image_list
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self):
        Key = pygame.key.get_pressed()
        if Key[pygame.K_w] and self.rect.y > -50:
            self.rect.y = self.rect.y - self.speed
            self.image = pygame.transform.scale(pygame.image.load(self.image_list[0]),(self.w,self.h))
            if self.rect.y < 0 and Fight == False:
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
                enemy_name.hp -= 3
                global dmgp
                dmgp = 1
                global Fight
                Fight = True
                

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
main_character = Owner(main_images[1],50,450,50,70,70,2,main_images)
golem_images = ['golem_left.png','golem_right.png','golem_attack.png','golem_left_dmg.png']
enemy_golem = Owner(golem_images[0],600,50,70,80,50,3,golem_images)
chest_images = ['chest.png']
chest = Owner(chest_images[0],1000,1000,70,60,3,0,chest_images)
#змінні
mfont = pygame.font.Font(None,20)
global Fight
Fight = False
global time_for_Attack
time_for_Attack = time.monotonic()
dmgp = 0
Location = 0
# гра
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            main_character.attack(enemy)

    
    #фон локацій
    if Location == 0:
        window.blit(background1,(0,0))
        window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(20,10))
    if Location == 1:
        window.blit(background2,(0,0))
        window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(20,10))
    if Location >= 2:
        window.blit(background3,(0,0))
        window.blit(mfont.render(str(main_character.hp),True,(0,0,0)),(20,10))
    # виведення
    main_character.reset()
    if Location == 0:
        enemy_golem.reset()
        
    if Location == 1:
        #під нові локації
        enemy_golem.reset()
    if Location >= 2:
        #під нові локації
        enemy_golem.reset()

    # ворог на локації
    if Location == 0:
        enemy = enemy_golem
        window.blit(mfont.render(str(enemy.hp),True,(0,0,0)),(enemy.rect.x,enemy.rect.y))
    if Location >= 2:
        #під нові локації
        enemy = enemy_golem
        
    # функції
    if Fight == True:
        enemy.rect.x = 350
        enemy.rect.y = 250
        enemy.w = 150
        enemy.h = 200
        if time.monotonic() - time_for_Attack >= 12:
            enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
            time_for_Attack = time.monotonic()
        if time.monotonic() - time_for_Attack >= 10:
            enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[2]),(enemy.w,enemy.h))
            if main_character.rect.x - enemy.rect.x < 150 and main_character.rect.x - enemy.rect.x > -30:
                if main_character.rect.y - enemy.rect.y < 155 and main_character.rect.y - enemy.rect.y > - 20:
                    main_character.hp -= 5
            time_for_Attack = time.monotonic()
        if dmgp == 1:
            if time.monotonic() - time_for_Attack >= 1:
                    enemy.image = pygame.transform.scale(pygame.image.load(enemy.image_list[0]),(enemy.w,enemy.h))
                    time_for_Attack = time.monotonic()
                    dmgp = 0

        if enemy.hp <= 0:
            enemy.w = 50
            enemy.h = 60
            enemy.rect.x = 1000
            Fight = False

    main_character.move()
    pygame.display.update()
