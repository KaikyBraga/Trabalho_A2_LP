from typing import Any
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")

LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

# Título da tela
pygame.display.set_caption("Jogo Maneiro")

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens,"dinoSpritesheet.png")).convert_alpha()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Unindo diretório com o arquivo de som
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, "jump_sound.wav"))
        # Volume do som de pulo
        self.som_pulo.set_volume(1)
        self.imagens_dinossauro = []
        # Recortando frames da Sprite Sheet
        for i in range(0,3):
            img = sprite_sheet.subsurface((i*32,0), (32,32))
            # Alteração da escala do personagem (Naturalmente 32x32)
            img = pygame.transform.scale(img,(32*3,32*3))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.pos_y_inicial = ALTURA - 64 - 96/2
        # Posição que fica o personagem
        self.rect.center = [100,ALTURA-64]
        self.pulo = False

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        if self.index_lista > 2:
            self.index_lista = 0
        # Velocidade que aparece os frames 
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32,0), (32,32))
        self.image = pygame.transform.scale(self.image, (32*3,32*3))
        self.rect = self.image.get_rect()
        # Posição da nuvem
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = LARGURA - randrange(30,300,90)
        
    def update(self):
        # Quando o canto superior direito da nuvem ultrapassar a tela, ela muda para o outro lado da tela
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 200, 50)

        # Velocidade com que a nuvem se movimenta
        self.rect.x -= 10

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        # Posição do Frame do Chão
        self.image = sprite_sheet.subsurface((6*32,0), (32,32))
        # Tamanho da imagem
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64
        self.rect.x = pos_x * 64


    # Mudando a posição do chão ao longo do jogo
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -=10

todas_sprites = pygame.sprite.Group()
dino = Dino()
todas_sprites.add(dino)


for i in range(0,4):
    nuvem = Nuvens()
    todas_sprites.add(nuvem)

# Inserindo 10 chãos
for i in range(0,LARGURA*2//64):
    chao = Chao(i)
    todas_sprites.add(chao)

# Relógio controlando a taxa de frames do jogo
relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Se o personagem ainda estiver no ar, não se pode apertar a tecla espaço
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                    dino.pular()

    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()