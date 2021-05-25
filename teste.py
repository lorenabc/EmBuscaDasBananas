import pygame 
import random 

pygame.init()
pygame.mixer.init()

WIDTH = 400
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Macaquinho')

BANANA_WIDTH = 30
BANANA_HEIGHT = 38
MACACO_WIDTH = 90
MACACO_HEIGHT = 72
PEDRA_WIDTH = 30
PEDRA_HEIGHT = 38

#assets
def load_assets ():
    assets = {}


    # Carrega imagens do jogo
    assets['background'] = pygame.image.load('assets/img/floresta1.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'],(WIDTH, HEIGHT))

    assets['banana_img'] = pygame.image.load('assets/img/banana.png').convert_alpha()
    assets['banana_img'] = pygame.transform.scale(assets['banana_img'],(BANANA_WIDTH,BANANA_HEIGHT))

    assets['macaco_img'] = pygame.image.load('assets/img/macaco.png').convert_alpha()
    assets['macaco_img'] = pygame.transform.scale(assets['macaco_img'],(MACACO_WIDTH,MACACO_HEIGHT))

    assets['pedra_img'] = pygame.image.load('assets/img/stone-0.png').convert_alpha()
    assets['pedra_img'] = pygame.transform.scale(assets['pedra_img'],(PEDRA_WIDTH,PEDRA_HEIGHT))

    assets['texto_pontos'] = pygame.font.Font('assets/font/PressStart2P.ttf',28)

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/sons/som_fundo.mp3')
    pygame.mixer.music.set_volume(0.4)
    assets['som_pedra'] = pygame.mixer.Sound('assets/sons/fall.wav')
    assets['som_banana'] = pygame.mixer.Sound('assets/sons/banana.ogg')

    return assets

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
assets = load_assets()
clock = pygame.time.Clock()
FPS = 30
vidas = 1

# Som de fundo jogo
pygame.mixer.music.play(loops=-1)

all_pedra = pygame.sprite.Group()
all_banana = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player = Macaco(assets['macaco_img'])
all_sprites.add(player)

for element in range(4):
    banana = Banana(assets['banana_img'])
    all_sprites.add(banana)
    all_banana.add(banana)

for elemento in range(4):
    pedra = Pedra(assets['pedra_img'])
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
        pedra = Pedra(assets['pedra_img'])
        all_sprites.add(pedra)
        all_pedra.add(pedra)
        assets['som_pedra'].play()
        vidas -= 1

    for bananas in pontuacao:
        pontuacao_inicial += 1
        banana = Banana(assets['banana_img'])
        all_sprites.add(banana)
        all_banana.add(banana)
        assets['som_banana'].play()
        if pontuacao_inicial % 10 == 0:
            vidas += 1

    window.fill((0,0,0))
    window.blit(assets['background'],(0,0))
  
    all_sprites.draw(window)

    texto = assets['texto_pontos'].render('{}'.format(pontuacao_inicial),True,(255,255,0))
    texto_rect = texto.get_rect()
    texto_rect.midtop = (WIDTH-40,10)
    window.blit(texto,texto_rect)

    # Desenhando as vidas
    texto_coracao = assets['texto_pontos'].render('{}'.format(chr(9829) * vidas),True,(255,0,0))
    texto_rect_coracao = texto_coracao.get_rect()
    texto_rect_coracao.topleft = (0, 10)
    window.blit(texto_coracao,texto_rect_coracao)

    pygame.display.update()

pygame.quit()