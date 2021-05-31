import pygame
import os
from config import WIDTH, HEIGHT, BANANA_WIDTH, BANANA_HEIGHT, MACACO_WIDTH, MACACO_HEIGHT, PEDRA_WIDTH, PEDRA_HEIGHT, IMG_DIR, SONS_DIR, FNT_DIR

BACKGROUND = 'background'
BANANA_IMG = 'banana_img'  
MACACO_IMG = 'macaco_img' 
PEDRA_IMG = 'pedra_img' 
TEXTO_PONTOS = 'texto_pontos' 
SOM_PEDRA = 'som_pedra'
SOM_BANANA = 'som_banana'
SOM_VIDA = 'som_vida'
SOM_TELA = 'som_tela'

#assets
def load_assets ():
    assets = {}

    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,'floresta1.png')).convert_alpha()
    assets[BACKGROUND] = pygame.transform.scale(assets['background'],(WIDTH, HEIGHT))

    assets[BANANA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'banana.png')).convert_alpha()
    assets[BANANA_IMG] = pygame.transform.scale(assets['banana_img'],(BANANA_WIDTH,BANANA_HEIGHT))

    assets[MACACO_IMG] = pygame.image.load(os.path.join(IMG_DIR,'macaco.png')).convert_alpha()
    assets[MACACO_IMG] = pygame.transform.scale(assets['macaco_img'],(MACACO_WIDTH,MACACO_HEIGHT))

    assets[PEDRA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'stone-0.png')).convert_alpha()
    assets[PEDRA_IMG] = pygame.transform.scale(assets['pedra_img'],(PEDRA_WIDTH,PEDRA_HEIGHT))

    assets[TEXTO_PONTOS] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SONS_DIR,'som_jogo.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[SOM_PEDRA] = pygame.mixer.Sound(os.path.join(SONS_DIR,'fall.wav'))
    assets[SOM_BANANA] = pygame.mixer.Sound(os.path.join(SONS_DIR,'banana.ogg'))
    assets[SOM_VIDA] = pygame.mixer.Sound(os.path.join(SONS_DIR,'life.ogg'))
    assets[SOM_TELA] = pygame.mixer.Sound(os.path.join(SONS_DIR,'som_fundo.mp3'))

    return assets