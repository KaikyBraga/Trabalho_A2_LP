"""
Esse módulo representa a loja do jogo.
Módulo responsável por criar a página da loja e suas funcionalidades.
"""

import pandas as pd
import os
import sys
import pygame
from pygame.locals import *
from variaveis_globais import *
from game import *
from helpers.image_loader import load_image
from utils import SpritesJogo

tela = pygame.display.set_mode((WIDTH, HEIGHT))

class Loja:
    """
    Classe que representa a loja do jogo.

    Inicializa a interface gráfica, os botões da loja e processa eventos de clique.

    Attributes:
        mainClock: Relógio utilizado para controlar a taxa de quadros.
        screen: Tela onde o menu é renderizado.
        font: Fonte utilizada para desenhar texto.
        click: Flag indicando se um clique do mouse ocorreu.

    Methods:
        __init__: Inicializa a classe e configura a interface gráfica.
        main_loja: Loop principal da loja, processa eventos e atualiza a tela.
    """
    
    def __init__(self):
        """
        Inicializa a classe Loja.
        """
        pygame.init()
        pygame.mixer.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720), 0, 32)
        pygame.display.set_caption("EMAP's RUNNING")
        self.font = pygame.font.SysFont(None, 20)
        self.click = False

        self.loja_aventureiro = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/loja_aventureiro.png"))
        self.loja_cavaleiro = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/loja_cavaleiro.png"))
        self.loja_guerreiro = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/loja_guerreiro.png"))
        self.loja_guerreira = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/loja_guerreira.png"))
        
        # Carrega a imagem de fundo da loja
        dados_jogo = pd.read_csv("informacoes_jogo.csv")
        personagem_selecionado = str(dados_jogo["Personagem_Selecionado"][0])
        if personagem_selecionado == "Aventureiro":
            self.background_img = self.loja_aventureiro
        elif personagem_selecionado == "Cavaleiro":
            self.background_img = self.loja_cavaleiro
        elif personagem_selecionado == "Guerreira":
            self.background_img = self.loja_guerreira
        elif personagem_selecionado == "Guerreiro":
            self.background_img = self.loja_guerreiro

        

        # Carrega as imagens dos botões de compra/adquirido
        self.botao_adquirido = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/botao_adquirido.png"))
        self.botao_preco_50 = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/botao_preco_50.png"))
        self.botao_preco_100 = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/botao_preco_100.png"))
        self.botao_preco_200 = load_image(os.path.join(os.path.dirname(__file__), "sprites/paginas/loja/botao_preco_200.png"))
        
        # Carrega as imagens dos personagens da loja
        self.aventureiro_img = SpritesJogo("sprites/personagens/aventureiro/corrida/aventureiro_corrida_", 6).carregar_frames(5)
        self.cavaleiro_img = SpritesJogo("sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_", 10).carregar_frames(4)
        self.guerreiro_img = SpritesJogo("sprites/personagens/guerreiro/corrida/guerreiro_corrida_", 8).carregar_frames(2)
        self.guerreira_img = SpritesJogo("sprites/personagens/guerreira/corrida/guerreira_corrida_", 8).carregar_frames(5)

        # Carrega a música
        pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "sons\som_loja.wav"))
        
        # Inicia a reprodução contínua da música
        pygame.mixer.music.play(-1)

    def main_loja(self):
        """
        Loop principal da loja, processa eventos e atualiza a tela.
        """
        loops = 0
        
        while True:
            mx, my = pygame.mouse.get_pos()
            loops += 1

            # Desenha a imagem de fundo da loja
            self.screen.blit(self.background_img, (0, 0))
            
            # Dados do arquivo csv   
            dados_jogo = pd.read_csv("informacoes_jogo.csv")
            quantidade_moedas = dados_jogo["Quantidade_de_Moedas"][0]
            aventureiro_desbloqueado = bool(dados_jogo["Aventureiro_Desbloqueado"].iloc[0])
            cavaleiro_desbloqueado = bool(dados_jogo["Cavaleiro_Desbloqueado"].iloc[0])
            guerreiro_desbloqueado = bool(dados_jogo["Guerreiro_Desbloqueado"].iloc[0])
            guerreira_desbloqueado = bool(dados_jogo["Guerreira_Desbloqueada"].iloc[0])   
        
            # Plota a quantidade de moedas
            texto_moeda = str(dados_jogo["Quantidade_de_Moedas"][0])
            mensagem_moeda = criar_texto(texto_moeda, 40, "Arial", (255, 255, 255), texto_negrito = True)
            self.screen.blit(mensagem_moeda, (1118, 35))

            # Cria os botões
            botao_aventureiro = pygame.Rect(100, 220, 240, 340)
            botao_cavaleiro = pygame.Rect(400, 220, 240, 340)
            botao_guerreiro = pygame.Rect(680, 220, 220, 340)
            botao_guerreira = pygame.Rect(950, 220, 240, 340)

            comprar_cavaleiro = pygame.Rect(370, 570, 250, 60)
            comprar_guerreiro = pygame.Rect(672, 570, 250, 60)
            comprar_guerreira = pygame.Rect(962, 570, 250, 60)
            
            # Coloca os personangens em seus respectivos retângulos de acordo com o loop
            self.screen.blit(self.aventureiro_img[loops % len(self.aventureiro_img)], (60, 280))
            self.screen.blit(self.cavaleiro_img[loops % len(self.cavaleiro_img)], (270, 150))
            self.screen.blit(self.guerreiro_img[loops % len(self.guerreiro_img)], (600, 220))
            self.screen.blit(self.guerreira_img[loops % len(self.guerreira_img)], (950, 250))

            # Plota as imagens dos botões de compra/adquirido
            self.screen.blit(self.botao_adquirido, (87, 570))
            if cavaleiro_desbloqueado == False:
                self.screen.blit(self.botao_preco_200, (375, 570))
            elif cavaleiro_desbloqueado == True:
                self.screen.blit(self.botao_adquirido, (375, 570))
            if guerreiro_desbloqueado == False:
                self.screen.blit(self.botao_preco_50, (672, 570))
            elif guerreiro_desbloqueado == True:
                self.screen.blit(self.botao_adquirido, (672, 570))
            if guerreira_desbloqueado == False:
                self.screen.blit(self.botao_preco_100, (960, 570))
            elif guerreira_desbloqueado == True:
                self.screen.blit(self.botao_adquirido, (960, 570))
            
            # Event Loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.mixer.music.stop()  # Para a música antes de fechar o programa
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # Retorna ao menu se a tecla ESC for pressionada
                    pygame.mixer.music.stop()
                    return True
                
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.click = True

            # Verifica as colisões com o mouse
            if botao_aventureiro.collidepoint((mx, my)) and aventureiro_desbloqueado == True and self.click:
                self.background_img = self.loja_aventureiro
                dados_jogo["Personagem_Selecionado"] = "Aventureiro"
                dados_jogo.to_csv("informacoes_jogo.csv", index=False)
             
            elif botao_cavaleiro.collidepoint((mx, my)) and cavaleiro_desbloqueado == True and self.click:
                self.background_img = self.loja_cavaleiro
                dados_jogo["Personagem_Selecionado"] = "Cavaleiro"
                dados_jogo.to_csv("informacoes_jogo.csv", index=False)
                    
            elif comprar_cavaleiro.collidepoint((mx, my)) and self.click and quantidade_moedas >= 200 and cavaleiro_desbloqueado == False:
                dados_jogo["Cavaleiro_Desbloqueado"] = True
                dados_jogo["Quantidade_de_Moedas"] = quantidade_moedas - 200
                dados_jogo.to_csv("informacoes_jogo.csv", index = False)
            
            elif botao_guerreiro.collidepoint((mx, my)) and guerreiro_desbloqueado == True and self.click:
                self.background_img = self.loja_guerreiro
                dados_jogo["Personagem_Selecionado"] = "Guerreiro"
                dados_jogo.to_csv("informacoes_jogo.csv", index=False)
            
            elif comprar_guerreiro.collidepoint((mx, my)) and self.click and quantidade_moedas >= 50 and guerreiro_desbloqueado == False:
                dados_jogo["Guerreiro_Desbloqueado"] = True
                dados_jogo["Quantidade_de_Moedas"] = quantidade_moedas - 50
                dados_jogo.to_csv("informacoes_jogo.csv", index = False)
                                     
            elif botao_guerreira.collidepoint((mx, my)) and guerreira_desbloqueado == True and self.click:
                self.background_img = self.loja_guerreira
                dados_jogo["Personagem_Selecionado"] = "Guerreira"
                dados_jogo.to_csv("informacoes_jogo.csv", index=False)
    
            elif comprar_guerreira.collidepoint((mx, my)) and self.click and quantidade_moedas >= 100 and guerreira_desbloqueado == False:
                dados_jogo["Guerreira_Desbloqueada"] = True
                dados_jogo["Quantidade_de_Moedas"] = quantidade_moedas - 100
                dados_jogo.to_csv("informacoes_jogo.csv", index = False)

            self.click = False
            
            pygame.display.update()
            self.mainClock.tick(15)

    def voltar():
        return True

                
if __name__ == "__main__":
    loja_instance = Loja()
    loja_instance.main_loja()
