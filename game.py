import os
import sys
import math
import random
import pygame
from variaveis_globais import *
from utils import *

pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("JOGO")

class Personagem:
    def __init__(self):
        self.frames_corrida = AVENTUREIRO_CORRIDA
        self.largura = 44
        self.altura = 44
        # Posição do personagem
        self.x = 100
        self.y = 500
        self.textura_num = 0
        self.carregar_imagem()
        self.exibir()

    def atualizar(self):
        self.textura_num = (self.textura_num + 1) % len(self.frames_corrida)
        self.carregar_imagem()

    def exibir(self):
        tela.blit(self.textura, (self.x, self.y))

    def carregar_imagem(self):
        self.textura = self.frames_corrida[self.textura_num]

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
    def __init__(self) -> None:

        self.fundos_paisagem = [Paisagem(x=0, velocidade=2.0), Paisagem(x=LARGURA_TELA, velocidade=2.0)]
        self.fundos_ponte = [Ponte(x=0, velocidade=5.0), Ponte(x=LARGURA_TELA, velocidade=5.0)]
        self.personagem = Personagem()


def loop_principal():
    """
    Função inicilizadora do loop principal do jogo.
    """

    # Objetos
    jogo = Jogo()
    personagem = jogo.personagem

    relogio = pygame.time.Clock()

    while True:
        # Exibição do carrosel do cenário.
        for fundo in jogo.fundos_paisagem:
            fundo.atualizar(-fundo.velocidade)
            fundo.exibir()

        for fundo in jogo.fundos_ponte:
            fundo.atualizar(-fundo.velocidade)
            fundo.exibir()

        personagem.atualizar()
        personagem.exibir()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Taxa de quadros do jogo
        relogio.tick(80)

        pygame.display.update()


loop_principal()
