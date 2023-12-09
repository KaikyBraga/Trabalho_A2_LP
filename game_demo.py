import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")

LARGURA = 1280
ALTURA = 720

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

# Título da tela
pygame.display.set_caption("Jogo Maneiro")

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens,"dinoSpritesheet.png")).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, "som_game_over.wav"))
som_colisao.set_volume(1)
colidiu = False

som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, "score_sound.wav"))
som_pontuacao.set_volume(1)

trilha_sonora = pygame.mixer.Sound(os.path.join(diretorio_sons, "trilha_sonora.wav"))
trilha_sonora.set_volume(0.3)
trilha_sonora.play()

escolha_obstaculo = choice([0,1])

pontos = 0

velocidade_jogo = 10

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont("comicsansms", tamanho, True, False)
    mensagem = f"{msg}"
    texto_formato = fonte.render(mensagem, True, cor)
    return texto_formato

def reiniciar_jogo():
    global pontos, velocidade_jogo, colidiu, escolha_obstaculo, trilha_sonora
    pontos = 0
    velocidade_jogo = 10
    colidiu = False
    dino.rect.y = ALTURA - 64 - 96//2
    dino.pulo = False
    dino_voador.rect.x = LARGURA
    cacto.rect.x = LARGURA
    escolha_obstaculo = choice([0, 1])
    trilha_sonora.play()


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Unindo diretório com o arquivo de som
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, "som_pulo.wav"))
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
        self.mask = pygame.mask.from_surface(self.image)
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
        self.rect.x -= velocidade_jogo

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
        self.rect.x -= 10

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32,0), (32,32))
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        # Posição do cacto logo acima do chão
        self.rect.center = (LARGURA, ALTURA - 64)
        self.rect.x = LARGURA

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= velocidade_jogo

class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro_voador = []
        for i in range(3,5):
            img = sprite_sheet.subsurface((i*32,0), (32,32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro_voador.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_dinossauro_voador[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA, 300)
        self.rect.x = LARGURA

    def update(self):
        # Se a escolha aleatória for igual a 0, o cacto aparece na tela
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= velocidade_jogo

            if self.index_lista > 1:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro_voador[int(self.index_lista)]

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

cacto = Cacto()
todas_sprites.add(cacto)

dino_voador = DinoVoador()
todas_sprites.add(dino_voador)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
grupo_obstaculos.add(dino_voador)

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
            if event.key == K_SPACE and colidiu == False:
                # Se o personagem ainda estiver no ar, não se pode apertar a tecla espaço
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                    dino.pular()

            if event.key == K_r and colidiu == True:
                reiniciar_jogo()

    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)

    todas_sprites.draw(tela)

    if cacto.rect.topright[0] <= 0 or dino_voador.rect.topright[0] <= 0:
        escolha_obstaculo = choice([0,1])
        cacto.rect.x = LARGURA
        dino_voador.rect.x = LARGURA
        cacto.escolha = escolha_obstaculo
        dino_voador.escolha = escolha_obstaculo


    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        trilha_sonora.stop()

        if pontos % 100 == 0:
            pontos += 1
        mensagem_game_over = exibe_mensagem("GAME OVER", 40, (255,0,0))
        tela.blit(mensagem_game_over, (LARGURA//2, ALTURA//2))

        mensagem_restart = exibe_mensagem("Pressione R para reiniciar", 20, (255,0,0))
        tela.blit(mensagem_restart, (LARGURA//2, (ALTURA//2) + 60))


    else:
        pontos += 1
        todas_sprites.update()
        texto_pontos = exibe_mensagem(pontos, 40, (0,255,0))

    if pontos % 100 == 0:
        som_pontuacao.play()
        if velocidade_jogo >= 23:
            velocidade_jogo += 0
        else:
            velocidade_jogo += 1

    # Inserindo o texto de pontos em determinada posição
    tela.blit(texto_pontos, (520, 30))


    pygame.display.flip()