# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, JOGANDO, CHOOSE, TERMINOU, DEAD
from game_screen import game_screen
from death_screen import death_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Em Busca das Bananas')

state = JOGANDO
while state != TERMINOU:
    # if state == INIT:
    #     state = init_screen(janela, record)

    # if state == CHOOSE:
    #     #Recebe o estado do jogo e o sprite escolhido pelo jogador
    #     returns = choose_screen(janela)
    #     state = returns[0]
    #     sprite_jogo = returns[1]

    if state == JOGANDO:
        #Recebe o estado do jogo, o score e o record
        state = game_screen(window)
        print(state)
        # state = state[0]
        
    elif state == DEAD:
        state = death_screen(window)

    else:
        state = DEAD



# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados