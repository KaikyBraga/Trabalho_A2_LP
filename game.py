import os
import sys
import math
import random
import pygame
from utils import *
from variaveis_globais import *
from variaveis_sprites import *

pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("JOGO")

class Personagem:
    def __init__(self, nome_personagem = "Aventureiro"):
        self.nome_personagem = nome_personagem
        if self.nome_personagem == "Aventureiro":
            self.frames_corrida = AVENTUREIRO_CORRIDA
            self.frames_pulo = AVENTUREIRO_PULO
            self.frames_deslizamento = AVENTUREIRO_DESLIZAMENTO
            self.frames_morte = AVENTUREIRO_MORTE
            # Posição do Personagem
            self.x = 20
            self.y = 350
            self.textura_num = 0
            # Velocidade do pulo
            self.velocidade_pulo = 8
            self.gravidade = 1.3
            # Altura do pulo (Quanto menor o valormais alto fica o pulo)
            self.parar_pulo = 80
            # Tempo do deslizamento
            self.tempo_inicio_deslizamento = 0
            self.tempo_deslizamento = 3500

        elif self.nome_personagem == "Cavaleiro":
            self.frames_corrida = CAVALEIRO_CORRIDA
            self.frames_pulo = CAVALEIRO_PULO
            self.frames_deslizamento = CAVALEIRO_DESLIZAMENTO
            self.frames_morte = CAVALEIRO_PULO
            # Posição do Personagem
            self.x = -65
            self.y = 212
            self.textura_num = 0
            # Velocidade do pulo
            self.velocidade_pulo = 8
            self.gravidade = 1.3
            # Altura do pulo (Quanto menor o valormais alto fica o pulo)
            self.parar_pulo = -30

        elif self.nome_personagem == "Guerreiro":
            self.frames_corrida = GUERREIRO_CORRIDA
            self.frames_pulo = GUERREIRO_PULO
            self.frames_deslizamento = GUERREIRO_DESLIZAMENTO
            self.frames_morte = GUERREIRO_PULO
            # Posição do Personagem
            self.x = -20
            self.y = 285
            self.textura_num = 0
            # Velocidade do pulo
            self.velocidade_pulo = 8
            self.gravidade = 1.3
            # Altura do pulo (Quanto menor o valormais alto fica o pulo)
            self.parar_pulo = 80
        
        elif self.nome_personagem == "Guerreira":
            self.frames_corrida = GUERREIRA_CORRIDA
            self.frames_pulo = GUERREIRA_PULO
            self.frames_deslizamento = GUERREIRA_DESLIZAMENTO
            self.frames_morte = GUERREIRA_MORTE
            # Posição do Personagem
            self.x = 20
            self.y = 318
            self.textura_num = 0
            # Velocidade do pulo
            self.velocidade_pulo = 8
            self.gravidade = 1.3
            # Altura do pulo (Quanto menor o valormais alto fica o pulo)
            self.parar_pulo = 80
        
        # Tempo do deslizamento
        self.tempo_inicio_deslizamento = 0
        self.tempo_deslizamento = 2800

        self.deslizando = False
        self.no_chao = True
        self.pulando = False
        self.parar_cair = self.y
        self.caindo = False
        self.carregar_imagem()
        self.exibir()

    def atualizar(self, loops):
        # Personagem pulando
        if self.pulando:
            if loops % 20 == 0:
                self.textura_num = (self.textura_num + 1) % len(self.frames_pulo)
                self.carregar_imagem()
           
            self.y -= self.velocidade_pulo
            if self.y <= self.parar_pulo:
                self.cair()

        # Personagem caindo
        elif self.caindo:
            if loops % 20 == 0:
                self.textura_num = (self.textura_num + 1) % len(self.frames_pulo)
                self.carregar_imagem()

            self.y += self.gravidade * self.velocidade_pulo
            if self.y >= self.parar_cair:
                self.parar()

        # Personagem deslizando
        elif self.deslizando:
            tempo_atual = pygame.time.get_ticks()
            if loops % 20 == 0:
                self.textura_num = (self.textura_num + 1) % len(self.frames_deslizamento)  
                self.carregar_imagem()   

            if tempo_atual - self.tempo_inicio_deslizamento >= self.tempo_deslizamento:
                self.terminar_deslizar()
                self.tempo_inicio_deslizamento = tempo_atual

        # Personagem caminhando
        elif loops % 7 == 0:
            self.textura_num = (self.textura_num + 1) % len(self.frames_corrida)
            self.carregar_imagem()

    def exibir(self):
        tela.blit(self.textura, (self.x, self.y))

    def carregar_imagem(self):
        if self.pulando or self.caindo:
            self.textura = self.frames_pulo[self.textura_num]
        
        elif self.deslizando:
            self.textura = self.frames_deslizamento[self.textura_num]

        elif self.no_chao:
            self.textura = self.frames_corrida[self.textura_num]

    def pular(self):
        """
        Define a responsabilidade dos booleanos
        """
        self.pulando = True
        self.no_chao = False

    def cair(self):
        self.pulando = False
        self.caindo = True

    def parar(self):
        self.caindo = False
        self.deslizando = False
        self.no_chao = True

    def deslizar(self):
        self.deslizando = True   
        self.no_chao = True 

    def terminar_deslizar(self):
        self.deslizando = False 
        self.no_chao = True   


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


class Paisagem(ElementoMovivel):
    """
    Classe que representa o carrossel de fundo no jogo.
    """
    def __init__(self, x, velocidade):
        super().__init__(x, "background.png", velocidade)


class Ponte(ElementoMovivel):
    """
    Classe que representa a ponte no jogo.
    """
    def __init__(self, x, velocidade):
        super().__init__(x, "ponte.png", velocidade)

class Jogo:
    def __init__(self):

        self.fundos_paisagem = [Paisagem(x=0, velocidade=2.0), Paisagem(x=LARGURA_TELA, velocidade=2.0)]
        self.fundos_ponte = [Ponte(x=0, velocidade=5.0), Ponte(x=LARGURA_TELA, velocidade=5.0)]
        self.personagem = Personagem("Cavaleiro")
    
    #TODO: Criar uma função/método que muda o self.personagem   


    def loop_principal(self):
        """
        Função inicilizadora do loop principal do jogo.
        """

        # Objetos
        jogo = Jogo()
        personagem = jogo.personagem

        relogio = pygame.time.Clock()

        loops = 0

        while True:

            loops += 1

            # Exibição do carrosel do cenário.
            for fundo in jogo.fundos_paisagem:
                fundo.atualizar(-fundo.velocidade)
                fundo.exibir()

            for fundo in jogo.fundos_ponte:
                fundo.atualizar(-fundo.velocidade)
                fundo.exibir()

            personagem.atualizar(loops)
            personagem.exibir()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    # Retorna ao menu se a tecla ESC for pressionada
                    return True    

                if evento.type == pygame.KEYDOWN: 
                    if evento.key == pygame.K_s:
                        if  personagem.no_chao:
                            personagem.deslizar()
                    if evento.key == pygame.K_w:
                        if personagem.no_chao:
                            personagem.pular()

            # Taxa de quadros padrão do jogo
            relogio.tick(80)

            pygame.display.update()


if __name__ == "__main__":
     jogo = Jogo()
     jogo.loop_principal()