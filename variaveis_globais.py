import pygame

LARGURA = 1280
ALTURA = 720

# SPRITES

# CENÁRIO
PONTE = pygame.image.load("sprites/cenario/ponte.png")
BACKGROUND = pygame.image.load("sprites/cenario/background.png")


# MOEDA
MOEDA_01 = pygame.image.load("sprites/moeda/moeda_01.png")
MOEDA_02 = pygame.image.load("sprites/moeda/moeda_02.png")
MOEDA_03 = pygame.image.load("sprites/moeda/moeda_03.png")
MOEDA_04 = pygame.image.load("sprites/moeda/moeda_04.png")
MOEDA_05 = pygame.image.load("sprites/moeda/moeda_05.png")
MOEDA_06 = pygame.image.load("sprites/moeda/moeda_06.png")
MOEDA = [MOEDA_01, MOEDA_02, MOEDA_03, MOEDA_04, MOEDA_05, MOEDA_06]


# OBSTÁCULOS
# Bomba
BOMBA = pygame.image.load("sprites/bomba/bomba.png")
EXPLOSAO_BOMBA_01 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_01.png")
EXPLOSAO_BOMBA_02 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_02.png")
EXPLOSAO_BOMBA_03 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_03.png")
EXPLOSAO_BOMBA_04 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_04.png")
EXPLOSAO_BOMBA_05 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_05.png")
EXPLOSAO_BOMBA_06 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_06.png")
EXPLOSAO_BOMBA_07 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_07.png")
EXPLOSAO_BOMBA_08 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_08.png")
EXPLOSAO_BOMBA_09 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_09.png")
EXPLOSAO_BOMBA_10 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_10.png")
EXPLOSAO_BOMBA_11 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_11.png")
EXPLOSAO_BOMBA_12 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_12.png")
EXPLOSAO_BOMBA_13 = pygame.image.load("sprites/obstaculos/bomba/explosao/explosao_13.png")
EXPLOSAO_BOMBA = [EXPLOSAO_BOMBA_01, EXPLOSAO_BOMBA_02, EXPLOSAO_BOMBA_03, EXPLOSAO_BOMBA_04, EXPLOSAO_BOMBA_05, 
                  EXPLOSAO_BOMBA_06, EXPLOSAO_BOMBA_07, EXPLOSAO_BOMBA_08, EXPLOSAO_BOMBA_09, EXPLOSAO_BOMBA_10, 
                  EXPLOSAO_BOMBA_11, EXPLOSAO_BOMBA_12, EXPLOSAO_BOMBA_13]

# Fogo
FOGO_01 = pygame.image.load("sprites/obstaculos/fogo/fogo_01.png")
FOGO_02 = pygame.image.load("sprites/obstaculos/fogo/fogo_02.png")
FOGO_03 = pygame.image.load("sprites/obstaculos/fogo/fogo_03.png")
FOGO_04 = pygame.image.load("sprites/obstaculos/fogo/fogo_04.png")
FOGO_05 = pygame.image.load("sprites/obstaculos/fogo/fogo_05.png")
FOGO_06 = pygame.image.load("sprites/obstaculos/fogo/fogo_06.png")
FOGO = [FOGO_01, FOGO_02, FOGO_03, FOGO_04, FOGO_05, FOGO_06]

# Morcego
MORCEGO_01 = pygame.image.load("sprites/obstaculos/morcego_01")
MORCEGO_02 = pygame.image.load("sprites/obstaculos/morcego_01")
MORCEGO_03 = pygame.image.load("sprites/obstaculos/morcego_01")
MORCEGO_04 = pygame.image.load("sprites/obstaculos/morcego_01")
MORCEGO = [MORCEGO_01, MORCEGO_02, MORCEGO_03, MORCEGO_04]


# PÁGINAS
MENU = pygame.image.load("sprites/paginas/menu.png")
LOJA = pygame.image.load("sprites/paginas/loja.png")


# PERSONAGENS

# Aventureiro
AVENTUREIRO_CORRIDA_01 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_corrida_01.png")
AVENTUREIRO_CORRIDA_02 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_corrida_02.png")
AVENTUREIRO_CORRIDA_03 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_corrida_03.png")
AVENTUREIRO_CORRIDA_04 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_corrida_04.png")
AVENTUREIRO_CORRIDA_05 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_corrida_05.png")
AVENTUREIRO_CORRIDA_06 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_corrida_06.png")
AVENTUREIRO_CORRIDA = [AVENTUREIRO_CORRIDA_01, AVENTUREIRO_CORRIDA_02, AVENTUREIRO_CORRIDA_03,
                       AVENTUREIRO_CORRIDA_04, AVENTUREIRO_CORRIDA_05, AVENTUREIRO_CORRIDA_06]

AVENTUREIRO_PULO_01 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_pulo_01.png")
AVENTUREIRO_PULO_02 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_pulo_02.png")
AVENTUREIRO_PULO_03 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_pulo_03.png")
AVENTUREIRO_PULO_04 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_pulo_04.png")
AVENTUREIRO_PULO = [AVENTUREIRO_PULO_01, AVENTUREIRO_PULO_02, AVENTUREIRO_PULO_03, AVENTUREIRO_PULO_04]

AVENTUREIRO_DESLIZAMENTO_01 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_deslizamento_01.png")
AVENTUREIRO_DESLIZAMENTO_02 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_deslizamento_02.png")
AVENTUREIRO_DESLIZAMENTO = [AVENTUREIRO_DESLIZAMENTO_01, AVENTUREIRO_DESLIZAMENTO_02]

AVENTUREIRO_MORTE_01 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_01.png")
AVENTUREIRO_MORTE_02 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_02.png")
AVENTUREIRO_MORTE_03 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_03.png")
AVENTUREIRO_MORTE_04 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_04.png")
AVENTUREIRO_MORTE_05 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_05.png")
AVENTUREIRO_MORTE_06 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_06.png")
AVENTUREIRO_MORTE_07 = pygame.image.load("sprites/personagens/aventureiro/aventureiro_morte_07.png")
AVENTUREIRO_MORTE_07 = [AVENTUREIRO_MORTE_01, AVENTUREIRO_MORTE_02, AVENTUREIRO_MORTE_03, AVENTUREIRO_MORTE_04,
                        AVENTUREIRO_MORTE_05, AVENTUREIRO_MORTE_06, AVENTUREIRO_MORTE_07]

# Cavaleiro
CAVALEIRO_CORRIDA_01 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_01.png")
CAVALEIRO_CORRIDA_02 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_02.png")
CAVALEIRO_CORRIDA_03 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_03.png")
CAVALEIRO_CORRIDA_04 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_04.png")
CAVALEIRO_CORRIDA_05 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_05.png")
CAVALEIRO_CORRIDA_06 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_06.png")
CAVALEIRO_CORRIDA_07 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_07.png")
CAVALEIRO_CORRIDA_08 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_08.png")
CAVALEIRO_CORRIDA_09 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_09.png")
CAVALEIRO_CORRIDA_10 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_corrida_10.png")
CAVALEIRO_CORRIDA = [CAVALEIRO_CORRIDA_01, CAVALEIRO_CORRIDA_02, CAVALEIRO_CORRIDA_03, CAVALEIRO_CORRIDA_04, CAVALEIRO_CORRIDA_05,
                     CAVALEIRO_CORRIDA_06, CAVALEIRO_CORRIDA_07, CAVALEIRO_CORRIDA_08, CAVALEIRO_CORRIDA_09, CAVALEIRO_CORRIDA_10]

CAVALEIRO_PULO_01 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_pulo_01.png")
CAVALEIRO_PULO_02 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_pulo_02.png")
CAVALEIRO_PULO_03 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_pulo_03.png")
CAVALEIRO_PULO = [CAVALEIRO_PULO_01, CAVALEIRO_PULO_02, CAVALEIRO_PULO_03]

CAVALEIRO_DESLIZAMENTO_01 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_deslizamento_01.png")
CAVALEIRO_DESLIZAMENTO_02 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_deslizamento_02.png")
CAVALEIRO_DESLIZAMENTO = [AVENTUREIRO_DESLIZAMENTO_01, AVENTUREIRO_DESLIZAMENTO_02]

CAVALEIRO_MORTE_01 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_01.png")
CAVALEIRO_MORTE_02 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_02.png")
CAVALEIRO_MORTE_03 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_03.png")
CAVALEIRO_MORTE_04 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_04.png")
CAVALEIRO_MORTE_05 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_05.png")
CAVALEIRO_MORTE_06 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_06.png")
CAVALEIRO_MORTE_07 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_07.png")
CAVALEIRO_MORTE_08 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_08.png")
CAVALEIRO_MORTE_09 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_09.png")
CAVALEIRO_MORTE_10 = pygame.image.load("sprites/personagens/cavaleiro/cavaleiro_morte_10.png")
CAVALEIRO_MORTE = [CAVALEIRO_MORTE_01, CAVALEIRO_MORTE_02, CAVALEIRO_MORTE_03, CAVALEIRO_MORTE_04, CAVALEIRO_MORTE_05,
                   CAVALEIRO_MORTE_06, CAVALEIRO_MORTE_07, CAVALEIRO_MORTE_08, CAVALEIRO_MORTE_09, CAVALEIRO_MORTE_10]

# Guerreiro
GUERREIRO_CORRIDA_01 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_01.png")
GUERREIRO_CORRIDA_02 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_02.png")
GUERREIRO_CORRIDA_03 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_03.png")
GUERREIRO_CORRIDA_04 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_04.png")
GUERREIRO_CORRIDA_05 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_05.png")
GUERREIRO_CORRIDA_06 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_06.png")
GUERREIRO_CORRIDA_07 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_07.png")
GUERREIRO_CORRIDA_08 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_corrida_08.png")
GUERREIRO_CORRIDA = [GUERREIRO_CORRIDA_01, GUERREIRO_CORRIDA_02, GUERREIRO_CORRIDA_03, GUERREIRO_CORRIDA_04,
                     GUERREIRO_CORRIDA_05, GUERREIRO_CORRIDA_06, GUERREIRO_CORRIDA_07, GUERREIRO_CORRIDA_08]

GUERREIRO_PULO_01 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_pulo_01.png")
GUERREIRO_PULO_02 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_pulo_02.png")
GUERREIRO_PULO = [GUERREIRO_PULO_01, GUERREIRO_PULO_02]

GUERREIRO_DESLIZAMENTO_01 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_deslizamento_01.png")
GUERREIRO_DESLIZAMENTO_02 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_deslizamento_02.png")
GUERREIRO_DESLIZAMENTO = [GUERREIRO_DESLIZAMENTO_01, GUERREIRO_DESLIZAMENTO_02]

GUERREIRO_MORTE_01 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_01.png")
GUERREIRO_MORTE_02 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_02.png")
GUERREIRO_MORTE_03 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_03.png")
GUERREIRO_MORTE_04 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_04.png")
GUERREIRO_MORTE_05 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_05.png")
GUERREIRO_MORTE_06 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_06.png")
GUERREIRO_MORTE_07 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_07.png")
GUERREIRO_MORTE_08 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_08.png")
GUERREIRO_MORTE_09 = pygame.image.load("sprites/personagens/guerreiro/guerreiro_morte_09.png")
GUERREIRO_MORTE = [GUERREIRO_MORTE_01, GUERREIRO_MORTE_02, GUERREIRO_MORTE_03, GUERREIRO_MORTE_04, GUERREIRO_MORTE_05,
                   GUERREIRO_MORTE_06, GUERREIRO_MORTE_07, GUERREIRO_MORTE_08, GUERREIRO_MORTE_09]

# Guerreira
GUERREIRA_CORRIDA_01 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_01.png")
GUERREIRA_CORRIDA_02 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_02.png")
GUERREIRA_CORRIDA_03 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_03.png")
GUERREIRA_CORRIDA_04 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_04.png")
GUERREIRA_CORRIDA_05 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_05.png")
GUERREIRA_CORRIDA_06 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_06.png")
GUERREIRA_CORRIDA_07 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_07.png")
GUERREIRA_CORRIDA_08 = pygame.image.load("sprites/personagens/guerreira/guerreira_corrida_08.png")
GUERREIRA_CORRIDA = [GUERREIRA_CORRIDA_01, GUERREIRA_CORRIDA_02, GUERREIRA_CORRIDA_03, GUERREIRA_CORRIDA_04,
                     GUERREIRA_CORRIDA_05, GUERREIRA_CORRIDA_06, GUERREIRA_CORRIDA_07, GUERREIRA_CORRIDA_08]

GUERREIRA_PULO_01 = pygame.image.load("sprites/personagens/guerreira/guerreira_pulo_01.png")
GUERREIRA_PULO_02 = pygame.image.load("sprites/personagens/guerreira/guerreira_pulo_02.png")
GUERREIRA_PULO = [GUERREIRA_PULO_01, GUERREIRA_PULO_02]

GUERREIRA_DESLIZAMENTO_01 = pygame.image.load("sprites/personagens/guerreira/guerreira_deslizamento_01.png")
GUERREIRA_DESLIZAMENTO_02 = pygame.image.load("sprites/personagens/guerreira/guerreira_deslizamento_02.png")
GUERREIRA_DESLIZAMENTO_03 = pygame.image.load("sprites/personagens/guerreira/guerreira_deslizamento_03.png")
GUERREIRA_DESLIZAMENTO_04 = pygame.image.load("sprites/personagens/guerreira/guerreira_deslizamento_04.png")
GUERREIRA_DESLIZAMENTO_05 = pygame.image.load("sprites/personagens/guerreira/guerreira_deslizamento_05.png")
GUERREIRA_DESLIZAMENTO = [GUERREIRA_DESLIZAMENTO_01, GUERREIRA_DESLIZAMENTO_02, GUERREIRA_DESLIZAMENTO_03, 
                          GUERREIRA_DESLIZAMENTO_04, GUERREIRA_DESLIZAMENTO_05]

GUERREIRA_MORTE_01 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_01.png")
GUERREIRA_MORTE_02 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_02.png")
GUERREIRA_MORTE_03 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_03.png")
GUERREIRA_MORTE_04 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_04.png")
GUERREIRA_MORTE_05 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_05.png")
GUERREIRA_MORTE_06 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_06.png")
GUERREIRA_MORTE_07 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_07.png")
GUERREIRA_MORTE_08 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_08.png")
GUERREIRA_MORTE_09 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_09.png")
GUERREIRA_MORTE_10 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_10.png")
GUERREIRA_MORTE_11 = pygame.image.load("sprites/personagens/guerreira/guerreira_morte_11.png")
GUERREIRO_MORTE = [GUERREIRA_MORTE_01, GUERREIRA_MORTE_02, GUERREIRA_MORTE_03, GUERREIRA_MORTE_04, GUERREIRA_MORTE_05, GUERREIRA_MORTE_06, 
                   GUERREIRA_MORTE_07, GUERREIRA_MORTE_08, GUERREIRA_MORTE_09, GUERREIRA_MORTE_10, GUERREIRA_MORTE_11]
