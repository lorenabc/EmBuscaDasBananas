# ===== Inicialização =====
# ----- Importa e inicia pacotes
from init_screen import init_screen
import pygame
import random
from config import WIDTH, HEIGHT, INIT, JOGANDO, TERMINOU, DEAD
from game_screen import game_screen
from death_screen import death_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Em Busca das Bananas')

state = INIT
while state != TERMINOU:
    if state == INIT:
        state = init_screen(window)

    elif state == JOGANDO:
        state = game_screen(window)
        print(state)
        
    elif state == DEAD:
        state = death_screen(window)

    else:
        state = TERMINOU

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados