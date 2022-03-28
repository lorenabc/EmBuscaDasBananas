import pygame
from config import BLACK, FPS, WIDTH, YELLOW, RED, DEAD
from assets import BANANA_IMG, MACACO_IMG, PEDRA_IMG, load_assets, SOM_BANANA, SOM_PEDRA, BACKGROUND, TEXTO_PONTOS, SOM_VIDA
from sprites import Macaco, Banana, Pedra

# APS DESAGIL 
velx = 8

# game_screen
def game_screen(window):

    assets = load_assets()
    clock = pygame.time.Clock()
    vidas = 1

    # Som de fundo jogo
    pygame.mixer.music.play(loops=-1)

    all_pedra = pygame.sprite.Group()
    all_banana = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    player = Macaco(assets[MACACO_IMG])
    all_sprites.add(player)

    for element in range(4):
        banana = Banana(assets[BANANA_IMG])
        all_sprites.add(banana)
        all_banana.add(banana)

    for elemento in range(4):
        pedra = Pedra(assets[PEDRA_IMG])
        all_sprites.add(pedra)
        all_pedra.add(pedra)

    pontuacao_inicial = 0 

    TERMINOU = 0 
    JOGANDO = 1

    state = JOGANDO

    while state != TERMINOU:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = TERMINOU

            if state == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.speedx -= velx
                    if event.key == pygame.K_RIGHT:
                        player.speedx += velx
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.speedx += velx
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= velx

        all_sprites.update()

        colisao = pygame.sprite.spritecollide(player, all_pedra, True)
        pontuacao = pygame.sprite.spritecollide(player, all_banana, True)

        if state == JOGANDO:
            if len(colisao) > 0:
                pedra = Pedra(assets[PEDRA_IMG])
                all_sprites.add(pedra)
                all_pedra.add(pedra)
                assets[SOM_PEDRA].play()
                vidas -= 1

            for bananas in pontuacao:
                pontuacao_inicial += 1
                banana = Banana(assets[BANANA_IMG])
                all_sprites.add(banana)
                all_banana.add(banana)
                assets[SOM_BANANA].play()
                if pontuacao_inicial % 10 == 0:
                    vidas += 1
                    assets[SOM_VIDA].play()

            if vidas == 0:
                state = DEAD
                return state
                
        window.fill(BLACK)
        window.blit(assets[BACKGROUND],(0,0))
    
        all_sprites.draw(window)

        # Desenhando a pontuação
        texto = assets[TEXTO_PONTOS].render('{}'.format(pontuacao_inicial),True,(YELLOW))
        texto_rect = texto.get_rect()
        texto_rect.midtop = (WIDTH-40,10)
        window.blit(texto,texto_rect)

        # Desenhando as vidas
        texto_coracao = assets[TEXTO_PONTOS].render('{}'.format(chr(9829) * vidas),True,(RED))
        texto_rect_coracao = texto_coracao.get_rect()
        texto_rect_coracao.topleft = (0, 10)
        window.blit(texto_coracao,texto_rect_coracao)

        pygame.display.update()