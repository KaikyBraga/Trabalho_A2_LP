from utils import *


# CENÁRIO
PONTE = SpritesJogo("sprites/cenario/ponte.png", 1)
PONTE = PONTE.carregar_frames(1)
BACKGROUND = SpritesJogo("sprites/cenario/background.png", 1)
BACKGROUND = BACKGROUND.carregar_frames(1)


# MOEDA
MOEDA = SpritesJogo("sprites/moeda/moeda_", 6)
MOEDA = MOEDA.carregar_frames(1)


# OBSTÁCULOS
# Bomba
BOMBA = SpritesJogo("sprites/obstaculos/bomba/bomba.png", 1)
BOMBA = BOMBA.carregar_frames(1)
EXPLOSAO_BOMBA = SpritesJogo("sprites/obstaculos/bomba/explosao/explosao_", 13)
EXPLOSAO_BOMBA = EXPLOSAO_BOMBA.carregar_frames(1)


# Fogo
FOGO = SpritesJogo("sprites/obstaculos/fogo/fogo_", 6)
FOGO = FOGO.carregar_frames(1)


# Morcego
MORCEGO = SpritesJogo("sprites/obstaculos/morcego/morcego_", 4)
MORCEGO = MORCEGO.carregar_frames(1)


# PÁGINAS
MENU = SpritesJogo("sprites/paginas/menu/menu.png", 1)
MENU = MENU.carregar_frames(1)
MENU_JOGAR = SpritesJogo("sprites/paginas/menu/menu_jogar.png", 1)
MENU_JOGAR = MENU_JOGAR.carregar_frames(1)
MENU_LOJA = SpritesJogo("sprites/paginas/menu/menu_loja.png", 1)
MENU_LOJA = MENU_LOJA.carregar_frames(1)
MENU_SAIR = SpritesJogo("sprites/paginas/menu/menu_sair.png", 1)
MENU_SAIR = MENU_SAIR.carregar_frames(1)
LOJA_AVENTUREIRO = SpritesJogo("sprites/paginas/loja/loja_aventureiro.png", 1)
LOJA_AVENTUREIRO = LOJA_AVENTUREIRO.carregar_frames(1)
LOJA_CAVALEIRO = SpritesJogo("sprites/paginas/loja/loja_cavaleiro.png", 1)
LOJA_CAVALEIRO = LOJA_CAVALEIRO.carregar_frames(1)
LOJA_GUERREIRO = SpritesJogo("sprites/paginas/loja/loja_guerreiro.png", 1)
LOJA_GUERREIRO = LOJA_GUERREIRO.carregar_frames(1)
LOJA_GUERREIRA = SpritesJogo("sprites/paginas/loja/loja_guerreira.png", 1)
LOJA_GUERREIRA = LOJA_GUERREIRA.carregar_frames(1)


# Botões da Loja
BOTAO_ADQUIRIDO = SpritesJogo("sprites/paginas/loja/botao_preco_100.png", 1)
BOTAO_ADQUIRIDO = BOTAO_ADQUIRIDO.carregar_frames(1)
BOTAO_50 = SpritesJogo("sprites/paginas/loja/botao_preco_100.png", 1)
BOTAO_50 = BOTAO_50.carregar_frames(1)
BOTAO_100 = SpritesJogo("sprites/paginas/loja/botao_preco_100.png", 1)
BOTAO_100 = BOTAO_100.carregar_frames(1)
BOTAO_200 = SpritesJogo("sprites/paginas/loja/botao_preco_100.png", 1)
BOTAO_200 = BOTAO_200.carregar_frames(1)


# PERSONAGENS
# Aventureiro
AVENTUREIRO_CORRIDA = SpritesJogo("sprites/personagens/aventureiro/corrida/aventureiro_corrida_", 6)
AVENTUREIRO_CORRIDA = AVENTUREIRO_CORRIDA.carregar_frames(5)
AVENTUREIRO_PULO = SpritesJogo("sprites/personagens/aventureiro/pulo/aventureiro_pulo_", 4)
AVENTUREIRO_PULO = AVENTUREIRO_PULO.carregar_frames(5)
AVENTUREIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/aventureiro/deslizamento/aventureiro_deslizamento_", 2)
AVENTUREIRO_DESLIZAMENTO = AVENTUREIRO_DESLIZAMENTO.carregar_frames(5)
AVENTUREIRO_MORTE = SpritesJogo("sprites/personagens/aventureiro/morte/aventureiro_morte_", 7)
AVENTUREIRO_MORTE = AVENTUREIRO_MORTE.carregar_frames(5)


# Cavaleiro
CAVALEIRO_CORRIDA = SpritesJogo("sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_", 10)
CAVALEIRO_CORRIDA = CAVALEIRO_CORRIDA.carregar_frames(4)
CAVALEIRO_PULO = SpritesJogo("sprites/personagens/cavaleiro/pulo/cavaleiro_pulo_", 3)
CAVALEIRO_PULO = CAVALEIRO_PULO.carregar_frames(4)
CAVALEIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/cavaleiro/deslizamento/cavaleiro_deslizamento_", 2)
CAVALEIRO_DESLIZAMENTO = CAVALEIRO_DESLIZAMENTO.carregar_frames(4)
CAVALEIRO_MORTE = SpritesJogo("sprites/personagens/cavaleiro/morte/cavaleiro_morte_", 10)
CAVALEIRO_MORTE = CAVALEIRO_MORTE.carregar_frames(4)


# Guerreiro
GUERREIRO_CORRIDA = SpritesJogo("sprites/personagens/guerreiro/corrida/guerreiro_corrida_", 8)
GUERREIRO_CORRIDA = GUERREIRO_CORRIDA.carregar_frames(2)
GUERREIRO_PULO = SpritesJogo("sprites/personagens/guerreiro/pulo/guerreiro_pulo_", 2)
GUERREIRO_PULO = GUERREIRO_PULO.carregar_frames(2)
GUERREIRO_DESLIZAMENTO = SpritesJogo("sprites/personagens/guerreiro/deslizamento/guerreiro_deslizamento_", 2)
GUERREIRO_DESLIZAMENTO = GUERREIRO_DESLIZAMENTO.carregar_frames(2)
GUERREIRO_MORTE = SpritesJogo("sprites/personagens/guerreiro/morte/guerreiro_morte_", 9)
GUERREIRO_MORTE = GUERREIRO_MORTE.carregar_frames(2)


# Guerreira
GUERREIRA_CORRIDA = SpritesJogo("sprites/personagens/guerreira/corrida/guerreira_corrida_", 8)
GUERREIRA_CORRIDA = GUERREIRA_CORRIDA.carregar_frames(5)
GUERREIRA_PULO = SpritesJogo("sprites/personagens/guerreira/pulo/guerreira_pulo_", 3)
GUERREIRA_PULO = GUERREIRA_PULO.carregar_frames(5)
GUERREIRA_DESLIZAMENTO = SpritesJogo("sprites/personagens/guerreira/deslizamento/guerreira_deslizamento_", 5)
GUERREIRA_DESLIZAMENTO = GUERREIRA_DESLIZAMENTO.carregar_frames(5)
GUERREIRA_MORTE = SpritesJogo("sprites/personagens/guerreira/morte/guerreira_morte_", 11)
GUERREIRA_MORTE = GUERREIRA_MORTE.carregar_frames(5)

