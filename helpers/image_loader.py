"""
É sempre recomendado carregar as imagens, usar o .convert() e evitar ficar usando o scale em cada tick.
"""

import os
import pygame

def load_image(path: str, scale: tuple[int, int] = None, scale_factor:int|None = None, convert_alpha: bool = False) -> pygame.Surface:
    # Checa se o caminho é relativo ou absoluto, e normaliza para absoluto
    if not os.path.isabs(path):
        # Caminho relativo vem do diretório root do projeto
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
    path = os.path.abspath(path)
    
    image = pygame.image.load(path)
    if scale:
        image = pygame.transform.scale(image, scale)
    if scale_factor:
        image = pygame.transform.scale(image, (image.get_width() * scale_factor, image.get_height() * scale_factor))
    if convert_alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    
    
    return image