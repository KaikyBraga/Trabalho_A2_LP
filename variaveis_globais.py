import pygame
from utils import *

LARGURA_TELA = 1280
ALTURA_TELA = 720

# SPRITES

# CENÁRIO
PONTE = pygame.image.load("sprites/cenario/ponte.png")
BACKGROUND = pygame.image.load("sprites/cenario/background.png")


# MOEDA
MOEDA = animacao_objetos("sprites/moeda/moeda_", 6)

# OBSTÁCULOS
# Bomba
BOMBA = pygame.image.load("sprites/obstaculos/bomba/bomba.png")
EXPLOSAO_BOMBA = animacao_objetos("sprites/obstaculos/bomba/explosao/explosao_", 13)

# Fogo
FOGO = animacao_objetos("sprites/obstaculos/fogo/fogo_", 6)

# Morcego
MORCEGO = animacao_objetos("sprites/obstaculos/morcego/morcego_", 4)

# PÁGINAS
MENU = pygame.image.load("sprites/paginas/menu.png")
MENU_JOGAR = pygame.image.load("sprites/paginas/menu_jogar.png")
MENU_LOJA = pygame.image.load("sprites/paginas/menu_loja.png")
MENU_SAIR = pygame.image.load("sprites/paginas/menu_sair.png")
LOJA = pygame.image.load("sprites/paginas/loja.png")


# PERSONAGENS
# Aventureiro
AVENTUREIRO_CORRIDA = animacao_objetos("sprites/personagens/aventureiro/corrida/aventureiro_corrida_", 6)
AVENTUREIRO_PULO = animacao_objetos("sprites/personagens/aventureiro/pulo/aventureiro_pulo_", 4)
AVENTUREIRO_DESLIZAMENTO = animacao_objetos("sprites/personagens/aventureiro/deslizamento/aventureiro_deslizamento_", 2)
AVENTUREIRO_MORTE = animacao_objetos("sprites/personagens/aventureiro/morte/aventureiro_morte_", 7)

# Cavaleiro
CAVALEIRO_CORRIDA = animacao_objetos("sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_", 10)
CAVALEIRO_PULO = animacao_objetos("sprites/personagens/cavaleiro/pulo/cavaleiro_pulo_", 3)
CAVALEIRO_DESLIZAMENTO = animacao_objetos("sprites/personagens/cavaleiro/deslizamento/cavaleiro_deslizamento_", 2)
CAVALEIRO_MORTE = animacao_objetos("sprites/personagens/cavaleiro/morte/cavaleiro_morte_", 10)

# Guerreiro
GUERREIRO_CORRIDA = animacao_objetos("sprites/personagens/guerreiro/corrida/guerreiro_corrida_", 8)
GUERREIRO_PULO = animacao_objetos("sprites/personagens/guerreiro/pulo/guerreiro_pulo_", 2)
GUERREIRO_DESLIZAMENTO = animacao_objetos("sprites/personagens/guerreiro/deslizamento/guerreiro_deslizamento_", 2)
GUERREIRO_MORTE = animacao_objetos("sprites/personagens/guerreiro/morte/guerreiro_morte_", 9)

# Guerreira
GUERREIRA_CORRIDA = animacao_objetos("sprites/personagens/guerreira/corrida/guerreira_corrida_", 8)
GUERREIRA_PULO = animacao_objetos("sprites/personagens/guerreira/pulo/guerreira_pulo_", 3)
GUERREIRA_DESLIZAMENTO = animacao_objetos("sprites/personagens/guerreira/deslizamento/guerreira_deslizamento_", 5)
GUERREIRA_MORTE = animacao_objetos("sprites/personagens/guerreira/morte/guerreira_morte_", 11)
