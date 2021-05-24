import pygame 
import random 

pygame.init()

WIDTH = 600
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Macaquinho')

#assets
BANANA_WIDTH = 30
BANANA_HEIGHT = 38
MACACO_WIDTH = 90
MACACO_HEIGHT = 72
PEDRA_WIDTH = 30
PEDRA_HEIGHT = 38
background = pygame.image.load('img/floresta1.png').convert_alpha()
background = pygame.transform.scale(background,(WIDTH, HEIGHT))

banana_img = pygame.image.load('img/banana.png').convert_alpha()
banana_img = pygame.transform.scale(banana_img,(BANANA_WIDTH,BANANA_HEIGHT))

macaco_img = pygame.image.load('img/macaco.png').convert_alpha()
macaco_img = pygame.transform.scale(macaco_img,(MACACO_WIDTH,MACACO_HEIGHT))

pedra_img = pygame.image.load('img/stone-0.png').convert_alpha()
pedra_img = pygame.transform.scale(pedra_img,(PEDRA_WIDTH,PEDRA_HEIGHT))

texto_pontos = pygame.font.Font('font/PressStart2P.ttf',28)

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

game = True
clock = pygame.time.Clock()
FPS = 30

all_pedra = pygame.sprite.Group()
all_banana = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player = Macaco(macaco_img)
all_sprites.add(player)

for element in range(6):
    banana = Banana(banana_img)
    all_sprites.add(banana)
    all_banana.add(banana)

for elemento in range(8):
    pedra = Pedra(pedra_img)
    all_sprites.add(pedra)
    all_pedra.add(pedra)

pontuacao_inicial = 0 

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8

    all_sprites.update()

    colisao = pygame.sprite.spritecollide(player, all_pedra, True)
    pontuacao = pygame.sprite.spritecollide(player, all_banana, True)

    if len(colisao) > 0:
        pedra = Pedra(pedra_img)
        all_sprites.add(pedra)
        all_pedra.add(pedra)

    for bananas in pontuacao:
        pontuacao_inicial += 1
        banana = Banana(banana_img)
        all_sprites.add(banana)
        all_banana.add(banana)

    window.fill((0,0,0))
    window.blit(background,(0,0))
  
    all_sprites.draw(window)

    texto = texto_pontos.render('{}'.format(pontuacao_inicial),True,(255,255,0))
    texto_rect = texto.get_rect()
    texto_rect.midtop = (WIDTH-40,10)
    window.blit(texto,texto_rect)

    pygame.display.update()

pygame.quit()