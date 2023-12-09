import pandas as pd
import os
import sys
import pygame
from pygame.locals import *
from variaveis_globais import *
from variaveis_sprites import *

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

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
        self.background_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja_aventureiro.png")).convert()
        
        self.loja_aventureiro = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja_aventureiro.png"))
        self.loja_cavaleiro = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja_cavaleiro.png"))
        self.loja_guerreiro = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja_guerreiro.png"))
        self.loja_guerreira = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja_guerreira.png"))

#Carrega as imagens dos personagens da loja
        self.aventureiro_img = AVENTUREIRO_CORRIDA
        self.cavaleiro_img = CAVALEIRO_CORRIDA
        self.guerreiro_img = GUERREIRO_CORRIDA
        self.guerreira_img = GUERREIRA_CORRIDA

# Carrega a música
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "sons\som_loja.wav"))
        
# Inicia a reprodução contínua da música
        pygame.mixer.music.play(-1)

    def main_loja(self):
    
        loops = 0
        
        while True:
            mx, my = pygame.mouse.get_pos()
            loops += 1
        # Desenha a imagem de fundo da loja
            self.screen.blit(self.background_img, (0, 0))
            dados_jogo = pd.read_csv("informacoes_jogo.csv")
            quantidade_moedas = (dados_jogo["Quantidade_de_Moedas"])
            aventureiro_desbloqueado = (dados_jogo["Aventureiro_Desbloqueado"]).bool()
            cavaleiro_desbloqueado = (dados_jogo["Cavaleiro_Desbloqueado"]).bool()
            guerreiro_desbloqueado = (dados_jogo["Guerreiro_Desbloqueado"]).bool()
            guerreira_desbloqueado = (dados_jogo["Guerreira_Desbloqueada"]).bool()


        #Cria os botões
            botao_aventureiro = pygame.Rect(100, 220, 240, 400)
            botao_cavaleiro = pygame.Rect(400, 220, 240, 400)
            botao_guerreiro = pygame.Rect(680, 220, 220, 400)
            botao_guerreira = pygame.Rect(950, 220, 240, 400)

            
            self.screen.blit(self.aventureiro_img[loops % len(self.aventureiro_img)], (60, 280))
            self.screen.blit(self.cavaleiro_img[loops % len(self.cavaleiro_img)], (270, 150))
            self.screen.blit(self.guerreiro_img[loops % len(self.guerreiro_img)], (600, 220))
            self.screen.blit(self.guerreira_img[loops % len(self.guerreira_img)], (950, 250))
        
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
            if botao_aventureiro.collidepoint((mx, my)) and aventureiro_desbloqueado == True and self.click:
                self.background_img = LOJA_AVENTUREIRO
                self.screen.blit(self.aventureiro_img[loops % len(self.aventureiro_img)], (60, 280))
                self.screen.blit(self.cavaleiro_img[loops % len(self.cavaleiro_img)], (270, 150))
                self.screen.blit(self.guerreiro_img[loops % len(self.guerreiro_img)], (600, 220))
                self.screen.blit(self.guerreira_img[loops % len(self.guerreira_img)], (950, 250))
                
            elif botao_cavaleiro.collidepoint((mx, my)) and cavaleiro_desbloqueado == True and self.click:
                self.background_img = LOJA_CAVALEIRO
                self.screen.blit(self.aventureiro_img[loops % len(self.aventureiro_img)], (60, 280))
                self.screen.blit(self.cavaleiro_img[loops % len(self.cavaleiro_img)], (270, 150))
                self.screen.blit(self.guerreiro_img[loops % len(self.guerreiro_img)], (600, 220))
                self.screen.blit(self.guerreira_img[loops % len(self.guerreira_img)], (950, 250))
                    
            elif botao_guerreiro.collidepoint((mx, my)) and guerreiro_desbloqueado == True and self.click:
                self.background_img = LOJA_GUERREIRO 
                self.screen.blit(self.aventureiro_img[loops % len(self.aventureiro_img)], (60, 280))
                self.screen.blit(self.cavaleiro_img[loops % len(self.cavaleiro_img)], (270, 150))
                self.screen.blit(self.guerreiro_img[loops % len(self.guerreiro_img)], (600, 220))
                self.screen.blit(self.guerreira_img[loops % len(self.guerreira_img)], (950, 250))
                           
            elif botao_guerreira.collidepoint((mx, my)) and guerreira_desbloqueado == True and self.click:
                self.background_img = LOJA_GUERREIRA
                self.screen.blit(self.aventureiro_img[loops % len(self.aventureiro_img)], (60, 280))
                self.screen.blit(self.cavaleiro_img[loops % len(self.cavaleiro_img)], (270, 150))
                self.screen.blit(self.guerreiro_img[loops % len(self.guerreiro_img)], (600, 220))
                self.screen.blit(self.guerreira_img[loops % len(self.guerreira_img)], (950, 250))
    
            
            self.click = False

            pygame.display.update()
            self.mainClock.tick(15)
                
if __name__ == "__main__":
    loja_instance = Loja()
    loja_instance.main_loja()
