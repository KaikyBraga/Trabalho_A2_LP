"""
Esse módulo possui as variáveis de som do jogo.
Módulo responsável por carregar os arquivos de som e armazená-los em variáveis.
"""

import os
from pygame.locals import *

som_loja = os.path.join(os.path.dirname(__file__), "sons/som_loja.wav")
som_menu = os.path.join(os.path.dirname(__file__), "sons/som_menu.wav")
som_moeda = os.path.join(os.path.dirname(__file__), "sons/som_moeda.wav")
som_score = os.path.join(os.path.dirname(__file__), "sons/som_score.wav")
som_game_over = os.path.join(os.path.dirname(__file__), "sons/som_game_over.wav")
som_pulo = os.path.join(os.path.dirname(__file__), "sons/som_pulo.wav")
som_deslizamento = os.path.join(os.path.dirname(__file__), "sons/som_deslizamento.wav")
som_jogo = os.path.join(os.path.dirname(__file__), "sons/som_jogo.wav")
