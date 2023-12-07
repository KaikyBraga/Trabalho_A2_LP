import pygame
from pygame.locals import *

def animacao_objetos(caminho_principal, num_frames):
    """
    Essa função tem o objetivo de fazer uma lista dos frames de determinado objeto com a finalidade de geram uma animação.

    Parameters:
        caminho_principal (string): Caminho principal dos elementos dos sprites com frames de uma animação específica.
        num_frames (int): Número de frames de determinada animação.

    Returns:
        lista_frames (list): Lista das Sprites de determinada animação.
    """
    lista_frames = []
    for i in range(1,num_frames+1):
        caminho_frame = caminho_principal + str(i) + ".png"
        lista_frames.append(pygame.image.load(caminho_frame))
    return lista_frames


# Função para criar o texto
def criar_texto(mensagem_texto, tamanho_fonte, nome_fonte, cor_fonte, texto_cerrilhado=False, texto_negrito = False, texto_italico = False):
    """
    Essa função tem o objetivo de criar textos estilizados para serem utilizadas no jogo.
    
    Parameters:
        mensagem_texto (str): Mensagem do texto.
        tamanho_fonte (float): Tamanho da fonte do texto.
        nome_fonte (str): Nome da fonte.
        cor_fonte (tuple): Cor da fonte em canal RGB (quantidade_vermelho, quantidade_verde, quantidade_azul).
        texto_cerrilhado (bool): Define se o texto é cerrilhado ou não.
        texto_negrito (bool): Define se o texto está em negrito ou não.
        texto_italico (bool): Define se o texto está em itálico ou não.
    Returns:
        texto (pygame.surface.Surface): Texto a ser utilizado na construção do jogo.
    """
    pygame.init()

    # Configuração do texto
    fonte = pygame.font.SysFont(nome_fonte, tamanho_fonte, texto_negrito, texto_italico)
    texto = fonte.render(mensagem_texto, texto_cerrilhado, cor_fonte)
    
    return print(texto)
