from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SONS_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 500 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 30 # Frames por segundo

# Define tamanhos
BANANA_WIDTH = 30
BANANA_HEIGHT = 38
MACACO_WIDTH = 90
MACACO_HEIGHT = 72
PEDRA_WIDTH = 30
PEDRA_HEIGHT = 38

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
TERMINOU = 0 
JOGANDO = 1
INIT = 2
CHOOSE = 3
DEAD = 4
QUIT = 5