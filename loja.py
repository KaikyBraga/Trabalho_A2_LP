import os
import sys
import pygame
from pygame.locals import *
from variaveis_globais import *

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

#Carrega as imagens dos personagens da loja
        self.aventureiro_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/personagens/aventureiro/corrida/aventureiro_corrida_6.png")).convert()
        self.cavaleiro_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_10.png")).convert()
        self.guerreiro_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/personagens/guerreiro/corrida/guerreiro_corrida_8.png")).convert()
        self.guerreira_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/personagens/guerreira/corrida/guerreira_corrida_8.png")).convert()

# Carrega a música
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "sons/loja_som.wav"))
        
# Inicia a reprodução contínua da música
        pygame.mixer.music.play(-1)

    def main_loja(self):
        while True:
            mx, my = pygame.mouse.get_pos()

        # Desenha a imagem de fundo da loja
            self.screen.blit(self.background_img, (0, 0))

            botao_aventureiro = pygame.Rect(100, 220, 240, 400)
            botao_cavaleiro = pygame.Rect(400, 220, 240, 400)
            botao_guerreiro = pygame.Rect(680, 220, 220, 400)
            botao_guerreira = pygame.Rect(950, 220, 240, 400)
                
            
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
            if botao_aventureiro.collidepoint((mx, my)):
                self.screen.blit(self.aventureiro_img, (190, 300))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    

            elif botao_cavaleiro.collidepoint((mx, my)):
                self.screen.blit(self.cavaleiro_img, (400, 180))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    

            elif botao_guerreiro.collidepoint((mx, my)):
                self.screen.blit(self.guerreiro_img, (540, 180))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    
                    
            elif botao_guerreira.collidepoint((mx, my)):
                self.screen.blit(self.guerreira_img, (680, 180))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    
                
            self.click = False

            pygame.display.update()
            self.mainClock.tick(60)
                
if __name__ == "__main__":
    loja_instance = Loja()
    loja_instance.main_loja()
