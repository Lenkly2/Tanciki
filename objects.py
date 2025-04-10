import pygame

class Image():
    def __init__(self,x,y,image,w,h):
        self.image = pygame.transform.scale(pygame.image.load(image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

brick1 = Image(45,45,"images/brick1.png",45,250)
brick2 = Image(135,45,"images/brick1.png",45,250)
brick3 = Image(225,45,"images/brick1.png",45,205)
brick4 = Image(315,45,"images/brick1.png",45,205)
brick5 = Image(405,45,"images/brick1.png",45,250)
brick6 = Image(495,45,"images/brick1.png",45,250)