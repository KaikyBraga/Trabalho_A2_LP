import os
import sys
import pygame
from pygame.locals import *
from variaveis_globais import *

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

class ElementoMovivel:
    """
    Classe base que representa os elementos móveis do jogo.
    """
    def __init__(self, x, imagem, velocidade):
        self.largura = LARGURA_TELA
        self.altura = ALTURA_TELA
        self.posicao_x = x
        self.posicao_y = 0
        self.velocidade = velocidade
        self.carregar_imagem(imagem)
        self.exibir()

    def atualizar(self, deslocamento):
        self.posicao_x += deslocamento
        if self.posicao_x <= -LARGURA_TELA:
            self.posicao_x = LARGURA_TELA

    def exibir(self):
        tela.blit(self.textura, (self.posicao_x, self.posicao_y))

    def carregar_imagem(self, imagem):
        caminho_imagem = os.path.join("sprites/cenario", imagem)
        self.textura = pygame.image.load(caminho_imagem)
        self.textura = pygame.transform.scale(self.textura, (self.largura, self.altura))

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
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "sons/loja_som.wav"))
        
# Inicia a reprodução contínua da música
        pygame.mixer.music.play(-1)

    def main_loja(self):
    
        relogio = pygame.time.Clock()
        while True:
            mx, my = pygame.mouse.get_pos()

        # Desenha a imagem de fundo da loja
            self.screen.blit(self.background_img, (0, 0))

        #Cria os botões
            botao_aventureiro = pygame.Rect(100, 220, 240, 400)
            botao_cavaleiro = pygame.Rect(400, 220, 240, 400)
            botao_guerreiro = pygame.Rect(680, 220, 220, 400)
            botao_guerreira = pygame.Rect(950, 220, 240, 400)

            for aventureiro in self.aventureiro_img:
                self.screen.blit(aventureiro, (140, 400))
            for cavaleiro in self.cavaleiro_img:
                self.screen.blit(cavaleiro, (440, 400))
            for guerreiro in self.guerreiro_img:
                self.screen.blit(guerreiro, (720, 400))
            for guerreira in self.guerreira_img:
                self.screen.blit(guerreira, (990, 400))
        
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
                self.screen.blit(self.loja_aventureiro, (0,0))
                for aventureiro in self.aventureiro_img:
                    self.screen.blit(aventureiro, (140, 400))
                for cavaleiro in self.cavaleiro_img:
                    self.screen.blit(cavaleiro, (440, 400))
                for guerreiro in self.guerreiro_img:
                    self.screen.blit(guerreiro, (720, 400))
                for guerreira in self.guerreira_img:
                    self.screen.blit(guerreira, (990, 400))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    

            elif botao_cavaleiro.collidepoint((mx, my)):
                self.screen.blit(self.loja_cavaleiro, (0,0))
                for aventureiro in self.aventureiro_img:
                    self.screen.blit(aventureiro, (140, 400))
                for cavaleiro in self.cavaleiro_img:
                    self.screen.blit(cavaleiro, (440, 400))
                for guerreiro in self.guerreiro_img:
                    self.screen.blit(guerreiro, (720, 400))
                for guerreira in self.guerreira_img:
                    self.screen.blit(guerreira, (990, 400))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    

            elif botao_guerreiro.collidepoint((mx, my)):
                self.screen.blit(self.loja_guerreiro, (0,0))
                for aventureiro in self.aventureiro_img:
                    self.screen.blit(aventureiro, (140, 400))
                for cavaleiro in self.cavaleiro_img:
                    self.screen.blit(cavaleiro, (440, 400))
                for guerreiro in self.guerreiro_img:
                    self.screen.blit(guerreiro, (720, 400))
                for guerreira in self.guerreira_img:
                    self.screen.blit(guerreira, (990, 400))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    
                    
            elif botao_guerreira.collidepoint((mx, my)):
                self.screen.blit(self.loja_guerreira, (0,0))
                for aventureiro in self.aventureiro_img:
                    self.screen.blit(aventureiro, (140, 400))
                for cavaleiro in self.cavaleiro_img:
                    self.screen.blit(cavaleiro, (440, 400))
                for guerreiro in self.guerreiro_img:
                    self.screen.blit(guerreiro, (720, 400))
                for guerreira in self.guerreira_img:
                    self.screen.blit(guerreira, (990, 400))
                if self.click:
                    pygame.mixer.music.stop()  # Para a música antes de chamar a função
                    
                
            self.click = False

            pygame.display.update()
            self.mainClock.tick(60)
            
class Moeda:
    def __init__(self):
        self.quantidade_moeda = 1000 #padrao

    
                
if __name__ == "__main__":
    loja_instance = Loja()
    loja_instance.main_loja()
