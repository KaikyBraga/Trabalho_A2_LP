import os
import sys
import pygame
from variaveis_globais import *

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("JOGO")

class ElementoMovivel:
    """
    Classe base que representa os elementos móveis do jogo.
    """
    def __init__(self, x, imagem, velocidade):
        self.largura = LARGURA
        self.altura = ALTURA
        self.posicao_x = x
        self.posicao_y = 0
        self.velocidade = velocidade
        self.carregar_imagem(imagem)
        self.exibir()

    def atualizar(self, deslocamento):
        self.posicao_x += deslocamento
        if self.posicao_x <= -LARGURA:
            self.posicao_x = LARGURA

    def exibir(self):
        tela.blit(self.textura, (self.posicao_x, self.posicao_y))

    def carregar_imagem(self, imagem):
        caminho_imagem = os.path.join("sprites/cenario", imagem)
        self.textura = pygame.image.load(caminho_imagem).convert_alpha()
        self.textura = pygame.transform.scale(self.textura, (self.largura, self.altura))


class FundoCarrossel(ElementoMovivel):
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
        super().__init__(x, "ponte_teste.png", velocidade)


class JogoPrincipal:
    """
    Classe principal que representa o jogo.
    """
    def __init__(self):
        # Inicialização do Fundo de Carrossel
        self.fundos_bg = [FundoCarrossel(x=0, velocidade=2.0), FundoCarrossel(x=LARGURA, velocidade=2.0)]
        self.fundos_ponte = [Ponte(x=0, velocidade=5.0), Ponte(x=LARGURA, velocidade=5.0)]


def loop_principal():
    """
    Função inicilizadora do loop principal do jogo.
    """
    jogo = JogoPrincipal()

    relogio = pygame.time.Clock()

    while True:
        # Exibição do carrosel do cenário.
        for fundo in jogo.fundos_bg:
            fundo.atualizar(-fundo.velocidade)
            fundo.exibir()

        for fundo in jogo.fundos_ponte:
            fundo.atualizar(-fundo.velocidade)
            fundo.exibir()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Taxa de quadros do jogo
        relogio.tick(80)

        pygame.display.update()


loop_principal()
