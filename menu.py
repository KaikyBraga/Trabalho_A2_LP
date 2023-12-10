import os
import sys
import pygame
from utils import *
import pandas as pd
from dino import *
from loja import Loja 
from pygame.locals import *
from variaveis_sons import *
from variaveis_globais import *
from variaveis_sprites import *

class Menu:
    """
    Classe que representa o menu principal do jogo.

    Inicializa a interface gráfica, os botões do menu e processa eventos de clique.

    Attributes:
        mainClock: Relógio utilizado para controlar a taxa de quadros.
        screen: Tela onde o menu é renderizado.
        font: Fonte utilizada para desenhar texto.
        click: Flag indicando se um clique do mouse ocorreu.

    Methods:
        __init__: Inicializa a classe e configura a interface gráfica.
        draw_text: Desenha a imagem de fundo do menu.
        main_menu: Loop principal do menu, processa eventos e atualiza a tela.
        jogar: Método chamado quando o botão "Jogar" é clicado.
        loja: Método chamado quando o botão "Loja" é clicado.
        sair: Método chamado quando o botão "Sair" é clicado.
    """
    def __init__(self):
        """
        Inicializa a classe Menu.
        """
        pygame.init()
        pygame.mixer.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720), 0, 32)
        pygame.display.set_caption("Emap's Running")
        self.font = pygame.font.SysFont(None, 20)
        self.click = False

        # Carrega a imagem de fundo do menu
        self.background_img = MENU

        # Carrega a música
        pygame.mixer.music.load(som_menu)

        # Inicia a reprodução contínua da música
        pygame.mixer.music.play(-1)  

        # Carrega as imagens dos botões 
        self.menu_jogar_img = MENU_JOGAR
        self.menu_loja_img = MENU_LOJA
        self.menu_sair_img = MENU_SAIR

    def draw_text(self):
        """
        Desenha a imagem de fundo do menu.
        """
        # Desenha a imagem de fundo do menu
        self.screen.blit(self.background_img, (0, 0))
        
    def main_menu(self):
        """
        Loop principal do menu, processa eventos e atualiza a tela.
        """
        while True:
            mx, my = pygame.mouse.get_pos()

            # Desenha a imagem de fundo do menu
            self.screen.blit(self.background_img, (0, 0))

            # Botões do Menu
            botao_jogar = pygame.Rect(520, 250, 240, 95)
            botao_loja = pygame.Rect(520, 400, 240, 95)
            botao_sair = pygame.Rect(520, 550, 240, 95)

            # Record
            dados_jogo = pd.read_csv("informacoes_jogo.csv")
            texto_record = str(dados_jogo["Score_Record"][0])
            mensagem_record = criar_texto(texto_record, 40, NOME_FONTE, COR_FONTE, texto_negrito=True)
            self.screen.blit(mensagem_record, (100, 80))

            # Event Loop
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.mixer.music.stop()  
                    pygame.quit()
                    sys.exit()
                elif evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    pygame.mixer.music.stop()  
                    pygame.quit()
                    sys.exit()
                elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                    self.click = True

            # Verifica as colisões com o mouse
            if botao_jogar.collidepoint((mx, my)):
                self.screen.blit(self.menu_jogar_img, (0, 0))
                self.screen.blit(mensagem_record, (100, 80))
                if self.click:
                    pygame.mixer.music.stop()  
                    self.jogar()

            elif botao_loja.collidepoint((mx, my)):
                self.screen.blit(self.menu_loja_img, (0, 0))
                self.screen.blit(mensagem_record, (100, 80))
                if self.click:
                    pygame.mixer.music.stop()  
                    self.loja()

            elif botao_sair.collidepoint((mx, my)):
                self.screen.blit(self.menu_sair_img, (0, 0))
                self.screen.blit(mensagem_record, (100, 80))
                if self.click:
                    pygame.mixer.music.stop()  
                    self.sair()
                 
            self.click = False

            pygame.display.update()
            self.mainClock.tick(60)

    def jogar(self):
        """
        Método chamado quando o botão "Jogar" é clicado.
        """
        pygame.mixer.music.stop()  
        main()
        pygame.mixer.music.load(som_menu)
        pygame.mixer.music.play(-1)

    def loja(self):
        """
        Método chamado quando o botão "Loja" é clicado.
        """
        pygame.mixer.music.stop()
        loja= Loja()
        loja_retorna_menu = loja.main_loja()

        if loja_retorna_menu:
            # Reinicia a música ao retornar ao menu
            pygame.mixer.music.load(som_menu)
            pygame.mixer.music.play(-1)
            return None

    def sair(self):
        """
        Método chamado quando o botão "Sair" é clicado.
        """
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    menu_instance = Menu()
    menu_instance.main_menu()