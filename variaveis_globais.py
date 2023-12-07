import pygame

LARGURA_TELA = 1280
ALTURA_TELA = 720

# SPRITES

# CENÁRIO
PONTE = pygame.image.load("sprites/cenario/ponte.png")
BACKGROUND = pygame.image.load("sprites/cenario/background.png")


# MOEDA
MOEDA = []
for i in range(1,7):
    caminho_frame = "sprites/moeda/moeda_" + str(i) + ".png"
    MOEDA.append(pygame.image.load(caminho_frame))


# OBSTÁCULOS
# Bomba
BOMBA = pygame.image.load("sprites/obstaculos/bomba/bomba.png")
EXPLOSAO_BOMBA = []
for i in range(1,14):
    caminho_frame = "sprites/obstaculos/bomba/explosao/explosao_" + str(i) + ".png"
    EXPLOSAO_BOMBA.append(pygame.image.load(caminho_frame))

# Fogo
FOGO = []
for i in range(1,7):
    caminho_frame = "sprites/obstaculos/fogo/fogo_" + str(i) + ".png"
    FOGO.append(pygame.image.load(caminho_frame))

# Morcego
MORCEGO = []
for i in range(1,5):
    caminho_frame = "sprites/obstaculos/morcego/morcego_" + str(i) + ".png"
    MORCEGO.append(pygame.image.load(caminho_frame))


# PÁGINAS
MENU = pygame.image.load("sprites/paginas/menu.png")
MENU_JOGAR = pygame.image.load("sprites/paginas/menu_jogar.png")
MENU_LOJA = pygame.image.load("sprites/paginas/menu_loja.png")
MENU_SAIR = pygame.image.load("sprites/paginas/menu_sair.png")
LOJA = pygame.image.load("sprites/paginas/loja.png")


# PERSONAGENS

# Aventureiro
AVENTUREIRO_CORRIDA = []
for i in range(1,7):
    caminho_frame = "sprites/personagens/aventureiro/aventureiro_corrida_" + str(i) + ".png"
    AVENTUREIRO_CORRIDA.append(pygame.image.load(caminho_frame))

AVENTUREIRO_PULO = []
for i in range(1,5):
    caminho_frame = "sprites/personagens/aventureiro/aventureiro_pulo_" + str(i) + ".png"
    AVENTUREIRO_PULO.append(pygame.image.load(caminho_frame))

AVENTUREIRO_DESLIZAMENTO = []
for i in range(1,3):
    caminho_frame = "sprites/personagens/aventureiro/aventureiro_deslizamento_" + str(i) + ".png"
    AVENTUREIRO_DESLIZAMENTO.append(pygame.image.load(caminho_frame))

AVENTUREIRO_MORTE = []
for i in range(1,8):
    caminho_frame = "sprites/personagens/aventureiro/aventureiro_morte_" + str(i) + ".png"
    AVENTUREIRO_DESLIZAMENTO.append(pygame.image.load(caminho_frame))

# Cavaleiro
CAVALEIRO_CORRIDA = []
for i in range(1,11):
    caminho_frame = "sprites/personagens/cavaleiro/cavaleiro_corrida_" + str(i) + ".png"
    CAVALEIRO_CORRIDA.append(pygame.image.load(caminho_frame))

CAVALEIRO_PULO = []
for i in range(1,4):
    caminho_frame = "sprites/personagens/cavaleiro/cavaleiro_pulo_" + str(i) + ".png"
    CAVALEIRO_PULO.append(pygame.image.load(caminho_frame))

CAVALEIRO_DESLIZAMENTO = []
for i in range(1,3):
    caminho_frame = "sprites/personagens/cavaleiro/cavaleiro_deslizamento_" + str(i) + ".png"
    CAVALEIRO_DESLIZAMENTO.append(pygame.image.load(caminho_frame))

CAVALEIRO_MORTE = []
for i in range(1,11):
    caminho_frame = "sprites/personagens/cavaleiro/cavaleiro_morte_" + str(i) + ".png"
    CAVALEIRO_MORTE.append(pygame.image.load(caminho_frame))

# Guerreiro
GUERREIRO_CORRIDA = []
for i in range(1,9):
    caminho_frame = "sprites/personagens/guerreiro/guerreiro_corrida_" + str(i) + ".png"
    GUERREIRO_CORRIDA.append(pygame.image.load(caminho_frame))

GUERREIRO_PULO = []
for i in range(1,3):
    caminho_frame = "sprites/personagens/guerreiro/guerreiro_pulo_" + str(i) + ".png"
    GUERREIRO_PULO.append(pygame.image.load(caminho_frame))

GUERREIRO_DESLIZAMENTO = []
for i in range(1,3):
    caminho_frame = "sprites/personagens/guerreiro/guerreiro_deslizamento_" + str(i) + ".png"
    GUERREIRO_PULO.append(pygame.image.load(caminho_frame))

GUERREIRO_MORTE = []
for i in range(1,10):
    caminho_frame = "sprites/personagens/guerreiro/guerreiro_morte_" + str(i) + ".png"
    GUERREIRO_MORTE.append(pygame.image.load(caminho_frame))

# Guerreira
GUERREIRA_CORRIDA = []
for i in range(1,9):
    caminho_frame = "sprites/personagens/guerreira/guerreira_corrida_" + str(i) + ".png"
    GUERREIRA_CORRIDA.append(pygame.image.load(caminho_frame))

GUERREIRA_PULO = []
for i in range(1,4):
    caminho_frame = "sprites/personagens/guerreira/guerreira_pulo_" + str(i) + ".png"
    GUERREIRA_PULO.append(pygame.image.load(caminho_frame))

GUERREIRA_DESLIZAMENTO = []
for i in range(1,6):
    caminho_frame = "sprites/personagens/guerreira/guerreira_deslizamento_" + str(i) + ".png"
    GUERREIRA_PULO.append(pygame.image.load(caminho_frame))

GUERREIRA_MORTE = []
for i in range(1,12):
    caminho_frame = "sprites/personagens/guerreira/guerreira_morte_" + str(i) + ".png"
    GUERREIRA_MORTE.append(pygame.image.load(caminho_frame))
