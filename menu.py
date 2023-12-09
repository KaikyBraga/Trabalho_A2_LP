import os
import sys
import pygame
from utils import *
import pandas as pd
from game import Jogo
from pygame.locals import *
from variaveis_sons import *
from variaveis_sprites import *

class Menu:
    def __init__(self):
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
        # Desenha a imagem de fundo do menu
        self.screen.blit(self.background_img, (0, 0))
        
    def main_menu(self):
        while True:
            mx, my = pygame.mouse.get_pos()

            # Desenha a imagem de fundo do menu
            self.screen.blit(self.background_img, (0, 0))

            botao_jogar = pygame.Rect(520, 250, 240, 95)
            botao_loja = pygame.Rect(520, 400, 240, 95)
            botao_sair = pygame.Rect(520, 550, 240, 95)

            dados_jogo = pd.read_csv("informacoes_jogo.csv")
            texto_record = str(dados_jogo["Score_Record"][0])
            mensagem_record = criar_texto(texto_record, 40, "Arial", (255,0,0), texto_negrito=True)
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
        pygame.mixer.music.stop()  
        jogo = Jogo()
        jogo_retornou_ao_menu = jogo.loop_principal()

        if jogo_retornou_ao_menu:
            # Reinicia a música ao retornar ao menu
            pygame.mixer.music.play(-1)

    def loja(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.draw_text('Options menu!', (255, 255, 255), 250, 250, pygame.Rect(100, 100, 100, 100))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)

    def sair(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    menu_instance = Menu()
    menu_instance.main_menu()