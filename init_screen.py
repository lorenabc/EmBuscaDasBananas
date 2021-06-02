import pygame
import os
from assets import BACKGROUND, TEXTO_PONTOS, load_assets, SOM_TELA, BANANA_IMG
from config import WIDTH, HEIGHT, JOGANDO, TERMINOU, BLACK, WHITE, YELLOW
from sprites import Banana
# from sprites import load_spritesheet

def init_screen (window):
    
    assets = load_assets()
    welcome_fnt = assets[TEXTO_PONTOS]
    name_fnt = assets[TEXTO_PONTOS]
    middle_fnt = assets[TEXTO_PONTOS]
    bottom_fnt = assets[TEXTO_PONTOS]

    welcome_surface = welcome_fnt.render("BEM VINDO", True,WHITE)
    welcome_rect = welcome_surface.get_rect()
    welcome_rect.midtop = (WIDTH/2, HEIGHT/2 - 50)

    middle_surface = middle_fnt.render('AO',True,WHITE)
    middle_rect = middle_surface.get_rect()
    middle_rect.midtop = (WIDTH/2,  HEIGHT/2)

    name_surface = name_fnt.render("EM BUSCA DAS BANANAS", True, WHITE)
    name_rect = name_surface.get_rect()
    name_rect.midtop = (WIDTH / 2, HEIGHT-300)

    bottom_surface = bottom_fnt.render('APERTE ESPAÇO PARA COMEÇAR',True,YELLOW)
    bottom_rect = bottom_surface.get_rect()
    bottom_rect.midtop = (WIDTH/2, HEIGHT/2 + 200)

    assets[SOM_TELA].play(loops=-1).set_volume(0.2)

    all_banana = pygame.sprite.Group()

    for element in range(1):
        banana = Banana(assets[BANANA_IMG])
        all_banana.add(banana)

    game = True
    while game:
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = TERMINOU
                game = False

            # Verifica se alguma tecla foi apertada:
            if event.type == pygame.KEYUP:
                key = pygame.key.get_pressed()
                # Verifica se return foi apertado
                if event.key == pygame.K_SPACE:
                    state = JOGANDO
                    pygame.mixer.pause()
                    game = False

        window.fill(BLACK)
        window.blit(assets[BACKGROUND],(0,0))
        window.blit(name_surface, name_rect)      
        window.blit(middle_surface, middle_rect)   
        window.blit(welcome_surface, welcome_rect)
        window.blit(bottom_surface, bottom_rect)

        all_banana.update()
        all_banana.draw(window)
        pygame.display.flip()
        pygame.display.update()

    return state