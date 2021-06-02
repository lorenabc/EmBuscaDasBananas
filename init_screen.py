import pygame
import os
from assets import BACKGROUND_INICIAL, TEXTO_PONTOS, load_assets, SOM_TELA
from config import WIDTH, HEIGHT, JOGANDO, TERMINOU, CHOOSE, BLACK, RED, WHITE
# from sprites import load_spritesheet

def init_screen (window):
    
    assets = load_assets()
    welcome_fnt = assets[TEXTO_PONTOS]
    name_fnt = assets[TEXTO_PONTOS]

    window.fill(BLACK)
    window.blit(assets[BACKGROUND_INICIAL],(0,0))

    welcome_surface = welcome_fnt.render("BEM VINDO AO", True, RED)
    welcome_rect = welcome_surface.get_rect()
    welcome_rect.midtop = (WIDTH/2,  HEIGHT/ 2 - 50)

    name_surface = name_fnt.render("EM BUSCA DAS BANANAS", True, WHITE)
    name_rect = name_surface.get_rect()
    name_rect.midtop = (WIDTH / 2, HEIGHT-300)

    window.blit(name_surface, name_rect)         
    window.blit(welcome_surface, welcome_rect)
    
    assets[SOM_TELA].play(loops=-1).set_volume(0.2)
