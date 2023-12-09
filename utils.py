import pygame
from pygame.locals import *



class SpritesJogo:
    """
    Classe para agrupar frames de uma ação de um objeto e criar animações.

    Attributes:
        caminho_principal (str): Caminho principal dos elementos dos sprites.
        num_frames (int): Número de frames da animação.

    Methods:
        carregar_frames(): Carrega os frames da animação.
        transformar_escala(conjunto_sprites, escala_sprites): Transforma a escala de um conjunto de sprites.
    """
    def __init__(self, caminho_principal, num_frames):
        """
        Inicializa a classe com o caminho dos sprites e o número de frames.

        Parameters:
            caminho_principal (str): Caminho principal dos elementos dos sprites.
            num_frames (int): Número de frames da animação.

        Returns:
            None
        """
        self.caminho_principal = caminho_principal
        self.num_frames = num_frames
    def carregar_frames(self, escala):
        """
        Carrega os frames da animação, caso seja um conjunto de imagens unitário, retorna apenas a imagem carregada. Caso contrário,
        retorna o conjunto de imagens carregadas em uma lista.

        Parameters:
            escala (int): Escala em que o conjunto de imagens fica sem perder 

        Returns:
            pygame.Surface or list[pygame.Surface]: Retorna a imagem unitária carregada ou a lista de imagens carregadas.
        """
        self.escala = escala

        if self.num_frames == 1:
            conjunto_imagens = pygame.image.load(self.caminho_principal)
            largura_sprite = conjunto_imagens.get_width()
            altura_sprite = conjunto_imagens.get_height()
            return pygame.transform.scale(conjunto_imagens, (largura_sprite * self.escala, altura_sprite * self.escala))
        else:
            lista_frames = []
            for i in range(1, self.num_frames + 1):
                caminho_frame = f"{self.caminho_principal}{i}.png"
                frame = pygame.image.load(caminho_frame)
                largura_sprite = frame.get_width()
                altura_sprite = frame.get_height()
                frame = pygame.transform.scale(frame, (largura_sprite * self.escala, altura_sprite * self.escala))
                lista_frames.append(frame)
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
