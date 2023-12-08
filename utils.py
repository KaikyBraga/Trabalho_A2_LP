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
    def carregar_frames(self):
        """
        Carrega os frames da animação, caso seja um conjunto de imagens unitário, retorna apenas a imagem carregada. Caso contrário,
        retorna o conjunto de imagens carregadas em uma lista.

        Parameters:
            None

        Returns:
            pygame.Surface or list[pygame.Surface]: Retorna a imagem unitária carregada ou a lista de imagens carregadas.
        """
        if self.num_frames == 1:
            return pygame.image.load(self.caminho_principal)
        else:
            lista_frames = []
            for i in range(1, self.num_frames + 1):
                caminho_frame = f"{self.caminho_principal}{i}.png"
                lista_frames.append(pygame.image.load(caminho_frame))
            return lista_frames

    def tranformar_escala(self, conjunto_sprites, escala_sprites):
        """
        Muda a escala de resolução de um conjunto de Sprites.

        Parameters:
            conjunto_sprites (pygame.Surface or list[pygame.Surface]): Conjunto de Sprites que geram uma animação ou uma imagem estática.
            escala_sprites (int): Fator de escala aplicado aos Sprites.
            
        Returns:
            pygame.Surface or list[pygame.Surface]: Retorna uma única imagem escalada ou uma lista de imagens escaladas.
        """
        self.conjunto_sprites = conjunto_sprites
        self.escala_sprites = escala_sprites

        if isinstance(self.conjunto_sprites, list):
            for index, sprite in enumerate(self.conjunto_sprites):
                largura_sprite = self.conjunto_sprites[index].get_width()
                altura_sprite = self.conjunto_sprites[index].get_height()
                self.conjunto_sprites[index] = pygame.transform.scale(sprite, (largura_sprite * escala_sprites, altura_sprite * escala_sprites))
            return self.conjunto_sprites

        else:
            largura_sprite = self.conjunto_sprites.get_width()
            altura_sprite = self.conjunto_sprites.get_height()
            return pygame.transform.scale(self.conjunto_sprites, (largura_sprite * escala_sprites, altura_sprite * escala_sprites))
        

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


PONTE = SpritesJogo("sprites/cenario/ponte.png", 1)