import random
import pygame
from config import WIDTH, HEIGHT, BANANA_WIDTH, BANANA_HEIGHT, MACACO_WIDTH, MACACO_HEIGHT, PEDRA_WIDTH, PEDRA_HEIGHT
from assets import BANANA_IMG, MACACO_IMG, BACKGROUND, TEXTO_PONTOS, SOM_PEDRA, SOM_BANANA


class Macaco(pygame.sprite.Sprite):
    def  __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT 
        self.speedx = 0

    def update(self):
  
        self.rect.x += self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Banana(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, WIDTH-BANANA_WIDTH)
        self.rect.y = random.randint(-100, -BANANA_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
     
        self.rect.x += self.speedx
        self.rect.y += self.speedy
       
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-BANANA_WIDTH)
            self.rect.y = random.randint(-100, -BANANA_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

class Pedra(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, WIDTH-BANANA_WIDTH)
        self.rect.y = random.randint(-100, -BANANA_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
 
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-BANANA_WIDTH)
            self.rect.y = random.randint(-100, -BANANA_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)