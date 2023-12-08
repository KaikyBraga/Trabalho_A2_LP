import os
import sys
import pygame
from pygame.locals import *

class Loja:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720), 0, 32)
        pygame.display.set_caption('game base')
        self.font = pygame.font.SysFont(None, 20)
        self.click = False

 # Carrega a imagem de fundo do menu
        self.background_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/menu_loja.png")).convert()

# Carrega a música
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "sons/loja_som.wav"))
        
# Inicia a reprodução contínua da música
        pygame.mixer.music.play(-1)

        def main_loja(self):
            while True:
                mx, my = pygame.mouse.get_pos()

            # Desenha a imagem de fundo da loja
                self.screen.blit(self.background_img, (0, 0))

                aventureiro = pygame.Rect(260, 180, 240, 95)
                cavaleiro = pygame.Rect(400, 180, 240, 95)
                guerreiro = pygame.Rect(540, 180, 240, 95)
                guerreira = pygame.Rect(680, 180, 240, 95)
                
            
            # Event Loop
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.mixer.music.stop()  # Para a música antes de fechar o programa
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.mixer.music.stop()  # Para a música antes de fechar o programa
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                        self.click = True

            # Verifica as colisões com o mouse
                if aventureiro.collidepoint((mx, my)):
                    self.screen.blit(self.loja_aventureiro_img, (0, 0))
                    if self.click:
                        pygame.mixer.music.stop()  # Para a música antes de chamar a função
                        self.jogar()

                elif cavaleiro.collidepoint((mx, my)):
                    self.screen.blit(self.loja_cavaleiro_img, (0, 0))
                    if self.click:
                        pygame.mixer.music.stop()  # Para a música antes de chamar a função
                        self.loja()

                elif guerreiro.collidepoint((mx, my)):
                    self.screen.blit(self.loja_guerreiro_img, (0, 0))
                    if self.click:
                        pygame.mixer.music.stop()  # Para a música antes de chamar a função
                        self.sair()
                        
                elif guerreira.collidepoint((mx, my)):
                    self.screen.blit(self.loja_guerreira_img, (0, 0))
                    if self.click:
                        pygame.mixer.music.stop()  # Para a música antes de chamar a função
                        self.sair()
                 
                self.click = False

                pygame.display.update()
                self.mainClock.tick(60)
