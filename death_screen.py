import pygame
from config import WIDTH, HEIGHT, INIT, BLACK, TERMINOU, BLACK, WHITE, RED, YELLOW, JOGANDO
from assets import load_assets, TEXTO_PONTOSS, TEXTO_PONTOS


def death_screen (window):

    assets = load_assets()
    gameover_fnt = assets[TEXTO_PONTOS]
    result_fnt = assets[TEXTO_PONTOS]
    enter_fnt = assets[TEXTO_PONTOSS]

    window.fill(BLACK)

    gameover_surface = gameover_fnt.render("GAME OVER", True, RED)
    gameover_rect = gameover_surface.get_rect()
    gameover_rect.midtop = (WIDTH/2,  HEIGHT/ 2 - 50)

    enter_surface = enter_fnt.render("APERTE ENTER PARA VOLTAR", True, WHITE)
    enter_rect = enter_surface.get_rect()
    enter_rect.midtop = (WIDTH / 2,  HEIGHT - 110)
    window.blit(enter_surface, enter_rect)         

    window.blit(gameover_surface, gameover_rect)
   
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
                if event.key == pygame.K_RETURN:
                    state = JOGANDO
                    game = False

        pygame.display.flip()

    return state
