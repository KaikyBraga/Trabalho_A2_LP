import pygame
from utils import *

LARGURA_TELA = 1280
ALTURA_TELA = 720

# SPRITES

# CENÁRIO
PONTE = SpritesJogo("sprites/cenario/ponte.png", 1)
PONTE = PONTE.carregar_frames()
BACKGROUND = SpritesJogo("sprites/cenario/background.png", 1)
BACKGROUND = BACKGROUND.carregar_frames()


# MOEDA
MOEDA = SpritesJogo("sprites/moeda/moeda_", 6)
MOEDA = MOEDA.carregar_frames()

# OBSTÁCULOS
# Bomba
BOMBA = SpritesJogo("sprites/obstaculos/bomba/bomba.png", 1)
BOMBA = BOMBA.carregar_frames()
EXPLOSAO_BOMBA = SpritesJogo("sprites/obstaculos/bomba/explosao/explosao_", 13)
EXPLOSAO_BOMBA = EXPLOSAO_BOMBA.carregar_frames()

# Fogo
FOGO = SpritesJogo("sprites/obstaculos/fogo/fogo_", 6)
FOGO = FOGO.carregar_frames()

# Morcego
MORCEGO = SpritesJogo("sprites/obstaculos/morcego/morcego_", 4)
MORCEGO = MORCEGO.carregar_frames()

# PÁGINASss/menu.png", 1)
MENU_JOGAR = SpritesJogo("sprites/paginas/menu_jogar.png", 1)
MENU_JOGAR = MENU_JOGAR.carregar_frames()
MENU_LOJA = SpritesJogo("sprites/paginas/menu_loja.png", 1)
MENU_LOJA = MENU_LOJA.carregar_frames()
MENU_SAIR = SpritesJogo("sprites/paginas/menu_sair.png", 1)
MENU_SAIR = MENU_SAIR.carregar_frames()
LOJA_AVENTUREIRO = SpritesJogo("sprites/paginas/loja_aventureiro.png", 1)
LOJA_AVENTUREIRO = LOJA_AVENTUREIRO.carregar_frames()
LOJA_CAVALEIRO = SpritesJogo("sprites/paginas/loja_cavaleiro.png", 1)
LOJA_CAVALEIRO = LOJA_CAVALEIRO.carregar_frames()
LOJA_GUERREIRO = SpritesJogo("sprites/paginas/loja_guerreiro.png", 1)
LOJA_GUERREIRO = LOJA_GUERREIRO.carregar_frames()
LOJA_GUERREIRA = SpritesJogo("sprites/paginas/loja_guerreira.png", 1)
LOJA_GUERREIRA = LOJA_GUERREIRA.carregar_frames()

# PERSONAGENS
# Aventureiro
AVENTUREIRO_CORRIDA = SpritesJogo("sprites/personagens/aventureiro/corrida/aventureiro_corrida_", 6)
AVENTUREIRO_CORRIDA = AVENTUREIRO_CORRIDA.carregar_frames()
AVENTUREIRO_PULO = SpritesJogo("sprites/personagens/aventureiro/pulo/aventureiro_pulo_", 4)
AVENTUREIRO_PULO = AVENTUREIRO_PULO.carregar_frames()
AVENTUREIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/aventureiro/deslizamento/aventureiro_deslizamento_", 2)
AVENTUREIRO_DESLIZAMENTO = AVENTUREIRO_DESLIZAMENTO.carregar_frames()
AVENTUREIRO_MORTE = SpritesJogo("sprites/personagens/aventureiro/morte/aventureiro_morte_", 7)
AVENTUREIRO_MORTE = AVENTUREIRO_MORTE.carregar_frames()

# Cavaleiro
CAVALEIRO_CORRIDA = SpritesJogo("sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_", 10)
CAVALEIRO_CORRIDA = CAVALEIRO_CORRIDA.carregar_frames()
CAVALEIRO_PULO = SpritesJogo("sprites/personagens/cavaleiro/pulo/cavaleiro_pulo_", 3)
CAVALEIRO_PULO = CAVALEIRO_PULO.carregar_frames()
CAVALEIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/cavaleiro/deslizamento/cavaleiro_deslizamento_", 2)
CAVALEIRO_DESLIZAMENTO = CAVALEIRO_DESLIZAMENTO.carregar_frames()
CAVALEIRO_MORTE = SpritesJogo("sprites/personagens/cavaleiro/morte/cavaleiro_morte_", 10)
CAVALEIRO_MORTE = CAVALEIRO_MORTE.carregar_frames()

# Guerreiro
GUERREIRO_CORRIDA = SpritesJogo("sprites/personagens/guerreiro/corrida/guerreiro_corrida_", 8)
GUERREIRO_CORRIDA = GUERREIRO_CORRIDA.carregar_frames()
GUERREIRO_PULO = SpritesJogo("sprites/personagens/guerreiro/pulo/guerreiro_pulo_", 2)
GUERREIRO_PULO = GUERREIRO_PULO.carregar_frames()
GUERREIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/guerreiro/deslizamento/guerreiro_deslizamento_", 2)
GUERREIRO_DESLIZAMENTO = GUERREIRO_DESLIZAMENTO.carregar_frames()
GUERREIRO_MORTE = SpritesJogo("sprites/personagens/guerreiro/morte/guerreiro_morte_", 9)
GUERREIRO_MORTE = GUERREIRO_MORTE.carregar_frames()

# Guerreira
GUERREIRA_CORRIDA = SpritesJogo("sprites/personagens/guerreira/corrida/guerreira_corrida_", 8)
GUERREIRA_CORRIDA = GUERREIRA_CORRIDA.carregar_frames()
GUERREIRA_PULO = SpritesJogo("sprites/personagens/guerreira/pulo/guerreira_pulo_", 3)
GUERREIRA_PULO = GUERREIRA_PULO.carregar_frames()
GUERREIRA_DESLIZAMENTO = SpritesJogo("sprites/personagens/guerreira/deslizamento/guerreira_deslizamento_", 5)
GUERREIRA_DESLIZAMENTO = GUERREIRA_DESLIZAMENTO.carregar_frames()
GUERREIRA_MORTE = SpritesJogo("sprites/personagens/guerreira/morte/guerreira_morte_", 11)
GUERREIRA_MORTE = GUERREIRA_MORTE.carregar_frames()

