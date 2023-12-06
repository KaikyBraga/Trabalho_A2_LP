import pygame
import sys
from pygame.locals import *

class Menu:
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((500, 500), 0, 32)
        pygame.display.set_caption('game base')
        self.font = pygame.font.SysFont(None, 20)
        self.click = False

    def draw_text(self, text, color, x, y, rect):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(rect.centerx, rect.centery))
        self.screen.blit(text_surface, text_rect)

    def main_menu(self):
        while True:
            self.screen.fill((0, 0, 0))

            mx, my = pygame.mouse.get_pos()

            # Mudar as coordenadas do botão
            botao_jogar = pygame.Rect(50, 100, 200, 50)
            botao_loja = pygame.Rect(50, 200, 200, 50)
            botao_sair = pygame.Rect(50, 300, 200, 50)
            
            if botao_jogar.collidepoint((mx, my)):
                if self.click:
                    self.jogar()
            elif botao_loja.collidepoint((mx, my)):
                if self.click:
                    self.loja()
            elif botao_sair.collidepoint((mx, my)):
                if self.click:
                    self.sair()        

            pygame.draw.rect(self.screen, (128, 128, 128), botao_jogar) 
            pygame.draw.rect(self.screen, (128, 128, 128), botao_loja)  
            pygame.draw.rect(self.screen, (128, 128, 128), botao_sair)

            # Essa parte não vai precisar, pq a imagem já tem as palavras
            self.draw_text('JOGAR', (255, 255, 255), 50 + 100, 100 + 25, botao_jogar)
            self.draw_text('LOJA', (255, 255, 255), 50 + 100, 200 + 25, botao_loja)
            self.draw_text('SAIR', (255, 255, 255), 50 + 100, 300 + 25, botao_sair)

            self.click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.click = True

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