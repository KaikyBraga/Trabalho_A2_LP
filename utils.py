import pygame

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

# TODO: CRIAR FUNÇÃO PARA FONTE DE TEXTO 