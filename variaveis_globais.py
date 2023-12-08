import pygame
from utils import *

LARGURA_TELA = 1280
ALTURA_TELA = 720

# SPRITES

# CENÁRIO
PONTE = SpritesJogo("sprites/cenario/ponte.png", 1)
BACKGROUND = SpritesJogo("sprites/cenario/background.png", 1)


# MOEDA
MOEDA = SpritesJogo("sprites/moeda/moeda_", 6)

# OBSTÁCULOS
# Bomba
BOMBA = SpritesJogo("sprites/obstaculos/bomba/bomba.png", 1)
EXPLOSAO_BOMBA = SpritesJogo("sprites/obstaculos/bomba/explosao/explosao_", 13)

# Fogo
FOGO = SpritesJogo("sprites/obstaculos/fogo/fogo_", 6)

# Morcego
MORCEGO = SpritesJogo("sprites/obstaculos/morcego/morcego_", 4)

# PÁGINASss/menu.png", 1)
MENU_JOGAR = SpritesJogo("sprites/paginas/menu_jogar.png", 1)
MENU_LOJA = SpritesJogo("sprites/paginas/menu_loja.png", 1)
MENU_SAIR = SpritesJogo("sprites/paginas/menu_sair.png", 1)
LOJA_AVENTUREIRO = SpritesJogo("sprites/paginas/loja_aventureiro.png", 1)
LOJA_CAVALEIRO = SpritesJogo("sprites/paginas/loja_cavaleiro.png", 1)
LOJA_GUERREIRO = SpritesJogo("sprites/paginas/loja_guerreiro.png", 1)
LOJA_GUERREIRA = SpritesJogo("sprites/paginas/loja_guerreira.png", 1)

# PERSONAGENS
# Aventureiro
AVENTUREIRO_CORRIDA = SpritesJogo("sprites/personagens/aventureiro/corrida/aventureiro_corrida_", 6)
AVENTUREIRO_PULO = SpritesJogo("sprites/personagens/aventureiro/pulo/aventureiro_pulo_", 4)
AVENTUREIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/aventureiro/deslizamento/aventureiro_deslizamento_", 2)
AVENTUREIRO_MORTE = SpritesJogo("sprites/personagens/aventureiro/morte/aventureiro_morte_", 7)

# Cavaleiro
CAVALEIRO_CORRIDA = SpritesJogo("sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_", 10)
CAVALEIRO_PULO = SpritesJogo("sprites/personagens/cavaleiro/pulo/cavaleiro_pulo_", 3)
CAVALEIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/cavaleiro/deslizamento/cavaleiro_deslizamento_", 2)
CAVALEIRO_MORTE = SpritesJogo("sprites/personagens/cavaleiro/morte/cavaleiro_morte_", 10)

# Guerreiro
GUERREIRO_CORRIDA = SpritesJogo("sprites/personagens/guerreiro/corrida/guerreiro_corrida_", 8)
GUERREIRO_PULO = SpritesJogo("sprites/personagens/guerreiro/pulo/guerreiro_pulo_", 2)
GUERREIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/guerreiro/deslizamento/guerreiro_deslizamento_", 2)
GUERREIRO_MORTE = SpritesJogo("sprites/personagens/guerreiro/morte/guerreiro_morte_", 9)

# Guerreira
GUERREIRA_CORRIDA = SpritesJogo("sprites/personagens/guerreira/corrida/guerreira_corrida_", 8)
GUERREIRA_PULO = SpritesJogo("sprites/personagens/guerreira/pulo/guerreira_pulo_", 3)
GUERREIRA_DESLIZAMENTO = SpritesJogo("sprites/personagens/guerreira/deslizamento/guerreira_deslizamento_", 5)
GUERREIRA_MORTE = SpritesJogo("sprites/personagens/guerreira/morte/guerreira_morte_", 11)
