import pygame
from objects import *

window = pygame.display.set_mode((800,600))
class Tank():
    def __init__(self,hp,damage,x,y,image,w,h):
        self.image = pygame.transform.scale(pygame.image.load(image),(w,h))
        self.hp = hp
        self.damage = damage
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class MainTank(Tank):
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x +=1
        if key[pygame.K_a]:
            self.rect.x -=1
        if key[pygame.K_s]:
            self.rect.y +=1
        if key[pygame.K_w]:
            self.rect.y -=1
class NpcTank(Tank):
    def __init__(self):
        self.orint = 'right'
    def move(self):
        if self.orint == "left":
            self.rect.x -= 1
        if self.orint == "right":
            self.rect.x += 1
        if self.rect.x <= 0:
            self.orint = "right"
        if self.rect.x >= 500:
            self.orint = "left"
backround = (0,0,0)
clock = pygame.time.Clock()
tanck1 = MainTank(50,10,0,0,"images/tank1.png",45,45)
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    window.fill(backround)
    window.blit(brick1,(45,45))
    tanck1.update()
    tanck1.move()
    pygame.display.update()
    clock.tick(60)