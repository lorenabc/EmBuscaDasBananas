import pygame 

pygame.init()

WIDTH = 1200
HEIGHT = 580
BANANA_WIDTH = 30
BANANA_HEIGTH = 38
MACACO_WIDTH = 50
MACACO_HEIGHT = 38

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Macaquinho')

background = pygame.image.load('img/floresta.jpeg').convert_alpha()
background = pygame.transform.scale(background,(WIDTH, HEIGHT))
banana_img = pygame.image.load('img/banana.png').convert_alpha()
banana_img = pygame.transform.scale(banana_img,(BANANA_WIDTH,BANANA_HEIGTH))
macaco_img = pygame.image.load('img/macaco.png').convert_alpha()
macaco_img = pygame.transform.scale(macaco_img,(MACACO_WIDTH,MACACO_HEIGHT))

game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((0,0,0))
    window.blit(background,(0,0))
    window.blit(banana_img,(0,0))
    window.blit(macaco_img,(0,HEIGHT-50))
    pygame.display.update()

pygame.quit()