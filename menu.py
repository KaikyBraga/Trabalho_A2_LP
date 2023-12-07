import os
import sys
import pygame
from pygame.locals import *

class Menu:
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720), 0, 32)
        pygame.display.set_caption('game base')
        self.font = pygame.font.SysFont(None, 20)
        self.click = False

        # Carrega a imagem de fundo do menu
        self.background_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/menu.png")).convert()

        # Carrega as imagens dos botões normais
        self.menu_jogar_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/menu_jogar.png")).convert()
        self.menu_loja_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/menu_loja.png")).convert()
        self.menu_sair_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "sprites/paginas/menu_sair.png")).convert()

    def draw_text(self, text, color, x, y, rect):
        # Desenha a imagem de fundo do menu
        self.screen.blit(self.background_img, (0, 0))
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(rect.centerx, rect.centery))
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            mx, my = pygame.mouse.get_pos()

            # Desenha a imagem de fundo do menu
            self.screen.blit(self.background_img, (0, 0))

            botao_jogar = pygame.Rect(520, 250, 240, 95)
            botao_loja = pygame.Rect(520, 400, 240, 95)
            botao_sair = pygame.Rect(520, 550, 240, 95)
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.click = True

            # Verifica as colisões com o mouse
            if botao_jogar.collidepoint((mx, my)):
                self.screen.blit(self.menu_jogar_img, (0, 0))
                if self.click:
                    self.jogar()

            elif botao_loja.collidepoint((mx, my)):
                self.screen.blit(self.menu_loja_img, (0, 0))
                if self.click:
                    self.loja()

            elif botao_sair.collidepoint((mx, my)):
                self.screen.blit(self.menu_sair_img, (0, 0))
                if self.click:
                    self.sair()
                 
            self.click = False

            pygame.display.update()
            self.mainClock.tick(60)

    def jogar(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.draw_text('Game started!', (255, 255, 255), 250, 250, pygame.Rect(100, 100, 100, 100))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)

    def loja(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.draw_text('Options menu!', (255, 255, 255), 250, 250, pygame.Rect(100, 100, 100, 100))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)

    def sair(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    menu_instance = Menu()
    menu_instance.main_menu()