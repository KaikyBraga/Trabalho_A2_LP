import os, sys, pygame, random

from variaveis_globais import BRIDGE_PATH, WOODS_PATH

WIDTH = 1200
HEIGHT = 720   

Y_FLOOR_BOMB = 435
Y_FLOOR_AVENTUREIRO = 355
Y_FLOOR_CAVALEIRO   = 215

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption("Dino")

class Aventureiro():
    def __init__(self) -> None:
        self.width = 50 * 5
        self.height = 37 * 5

        self.x = 150 - self.width//2
        self.y = Y_FLOOR_AVENTUREIRO

        self.jumping = False
        self.alpha = 1
        self.dy = 0
        self.ddy = 0.75*(self.alpha**2)

        self.deslizamento = False
        self.deslizamento_time = 20
        self.deslizamento_tick = 1

        self.alive = True

        self.texture_num = 0
        self.texture_run = []
        self.texture_jump = []
        self.texture_dead = []
        self.texture_deslizamento = []

        self.mask_run = []
        self.mask_jump = []
        self.mask_deslizamento = []

        self.set_texture()
    
    def update(self):
        if self.jumping:
            self.y -= self.dy
            self.dy -= self.ddy

            if self.y >= Y_FLOOR_AVENTUREIRO:
                self.jumping = False
                self.y = Y_FLOOR_AVENTUREIRO
            
            self.texture_num  = (min(self.texture_num + 0.25, len(self.texture_jump)-1))%len(self.texture_jump)
        elif self.deslizamento:
            self.deslizamento_time -= self.deslizamento_tick
            
            if self.deslizamento_time <= 0:
                self.deslizamento = False

            self.texture_num  = (self.texture_num + 0.25)%len(self.texture_deslizamento)
        elif self.alive:
            self.texture_num  = (self.texture_num + 0.25)%len(self.texture_run)
        else:
            self.texture_num  = min(self.texture_num + 0.125, len(self.texture_dead)-1)

    def show(self):
        if self.jumping: 
            screen.blit(self.texture_jump[int(self.texture_num)], (self.x, self.y))
        elif self.deslizamento:
            screen.blit(self.texture_deslizamento[int(self.texture_num)], (self.x, self.y))
        elif self.alive:
            screen.blit(self.texture_run[int(self.texture_num)], (self.x, self.y))
        else:
            screen.blit(self.texture_dead[int(self.texture_num)], (self.x, self.y))

    def set_texture(self):
        #carrega sprites de corrida
        for i in range(1, 7):
            aventureiro_run_path = f'sprites/personagens/aventureiro/corrida/aventureiro_corrida_{i}.png'  
            path = os.path.join(aventureiro_run_path)

            img = pygame.image.load(path)

            self.texture_run.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_run.append(pygame.mask.from_surface(self.texture_run[-1]))

        #carrega sprites de pulo
        for i in range(1, 5):
            aventureiro_jump_path = f'sprites/personagens/aventureiro/pulo/aventureiro_pulo_{i}.png'  
            path = os.path.join(aventureiro_jump_path)

            img = pygame.image.load(path)

            self.texture_jump.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_jump.append(pygame.mask.from_surface(self.texture_jump[-1]))
        
        #carrega sprites de morte
        for i in range(1, 7):
            aventureiro_dead_path = f'sprites/personagens/aventureiro/morte/aventureiro_morte_{i}.png'  
            path = os.path.join(aventureiro_dead_path)

            img = pygame.image.load(path)

            self.texture_dead.append(pygame.transform.scale(img, (self.width, self.height)))
        
        #carrega sprites de deslizamento
        for i in range(1, 3):
            aventureiro_deslizamento_path = f'sprites/personagens/aventureiro/deslizamento/aventureiro_deslizamento_{i}.png'  
            path = os.path.join(aventureiro_deslizamento_path)

            img = pygame.image.load(path)

            self.texture_deslizamento.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_deslizamento.append(pygame.mask.from_surface(self.texture_deslizamento[-1]))

    def jump(self):
        if self.deslizamento==False and self.jumping==False and self.alive:
            self.dy=17*self.alpha
            self.ddy = 0.75*(self.alpha**2)
            self.jumping = True
            self.texture_num=0
    
    def deslizar(self):
        if self.deslizamento==False and self.jumping==False and self.alive:
            self.deslizamento = True
            self.deslizamento_time = 20
            self.deslizamento_tick = 1
            self.texture_num=0

    def current_mask(self):
        if self.jumping:
            return self.mask_jump[int(self.texture_num)]
        elif self.deslizamento:
            return self.mask_deslizamento[int(self.texture_num)]
        else:
            return self.mask_run[int(self.texture_num)]

class Cavaleiro():
    def __init__(self) -> None:
        self.width = 120 * 4
        self.height = 80 * 4

        self.x = 200 - self.width//2
        self.y = Y_FLOOR_CAVALEIRO

        self.jumping = False
        self.alpha = 1
        self.dy = 0
        self.ddy = 0.75*(self.alpha**2)

        self.alive = True

        self.texture_num = 0
        self.texture_run = []
        self.texture_jump = []
        self.texture_dead = []
        self.mask_run = []
        self.mask_jump = []
        self.set_texture()
    
    def update(self):
        if self.jumping:
            self.y -= self.dy
            self.dy -= self.ddy

            if self.y >= Y_FLOOR_CAVALEIRO:
                self.jumping = False
                self.y = Y_FLOOR_CAVALEIRO
            
            self.texture_num  = (min(self.texture_num + 0.25, len(self.texture_jump)-1))%len(self.texture_jump)
        elif self.alive:
            self.texture_num  = (self.texture_num + 0.25)%len(self.texture_run)
        else:
            self.texture_num  = min(self.texture_num + 0.125, len(self.texture_dead)-1)

    def show(self):
        if self.jumping: 
            screen.blit(self.texture_jump[int(self.texture_num)], (self.x, self.y))
        elif self.alive:
            screen.blit(self.texture_run[int(self.texture_num)], (self.x, self.y))
        else:
            screen.blit(self.texture_dead[int(self.texture_num)], (self.x, self.y))

    def set_texture(self):
        #carrega sprites de corrida
        for i in range(1, 11):
            cavaleiro_run_path = f'sprites/personagens/cavaleiro/corrida/cavaleiro_corrida_{i}.png'  
            path = os.path.join(cavaleiro_run_path)

            img = pygame.image.load(path)

            self.texture_run.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_run.append(pygame.mask.from_surface(self.texture_run[-1]))

        #carrega sprites de pulo
        for i in range(1, 4):
            cavaleiro_jump_path = f'sprites/personagens/cavaleiro/pulo/cavaleiro_pulo_{i}.png'  
            path = os.path.join(cavaleiro_jump_path)

            img = pygame.image.load(path)

            self.texture_jump.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_jump.append(pygame.mask.from_surface(self.texture_jump[-1]))
        
        #carrega sprites de morte
        for i in range(1, 11):
            cavaleiro_dead_path = f'sprites/personagens/cavaleiro/morte/cavaleiro_morte_{i}.png'  
            path = os.path.join(cavaleiro_dead_path)

            img = pygame.image.load(path)

            self.texture_dead.append(pygame.transform.scale(img, (self.width, self.height)))

    def jump(self):
        if self.jumping==False and self.alive:
            self.dy=17*self.alpha
            self.ddy = 0.75*(self.alpha**2)
            self.jumping = True
            self.texture_num=0
    
    def current_mask(self):
        if self.jumping:
            return self.mask_jump[int(self.texture_num)]
        else:
            return self.mask_run[int(self.texture_num)]

class Bomb():
    def __init__(self, x) -> None:
        self.width = 100
        self.height = 100

        self.x = x
        self.y = Y_FLOOR_BOMB

        self.exploded = False

        self.texture_num = 0
        self.texture = None
        self.texture_explosion = []
        self.mask = None

        self.set_texture()
    
    def update(self, dx=0):
        if self.exploded==False:
            self.x += dx
        else:
            self.texture_num  = min(self.texture_num + 0.5, len(self.texture_explosion)-1)
    
    def show(self):
        if self.exploded==False:
            screen.blit(self.texture, (self.x, self.y))
        else:
            screen.blit(self.texture_explosion[int(self.texture_num)], (self.x, self.y))

    def set_texture(self):
        bomba_path = f'sprites/obstaculos/bomba/bomba.png'
        path = os.path.join(bomba_path)

        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

        self.mask = pygame.mask.from_surface(self.texture)

        for i in range(1, 14):
            explosao_path = f'sprites/obstaculos/bomba/explosao/explosao_{i}.png'
            path = os.path.join(explosao_path)
            img = (pygame.image.load(path))
            self.texture_explosion.append(pygame.transform.scale(img, (self.width, self.height))) 

class BG:
    def __init__(self, img_path, x=0, mult_speed=1) -> None:
        self.width = WIDTH
        self.height = HEIGHT

        self.x = x  
        self.y = 0
        
        self.mult_speed = mult_speed

        self.img_path = img_path
        self.texture = None
        self.set_texture()
    
    def update(self, dx):
        self.x += int(dx*self.mult_speed)
        if self.x <= -self.width:
            self.x += 2*self.width

    def show(self):
        screen.blit(self.texture, (self.x, self.y))
 
    def set_texture(self):
        path = os.path.join(self.img_path)

        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Game():
    def __init__(self) -> None:
        self.running = False
        self.start_game()

    def update(self):
        self.score += 1
        self.speed  = 8 + 2*(self.score//100) #dando erro
        self.char.alpha = self.speed/5

    def start_game(self):
        if self.running==False:
            self.score = 0
            self.speed = 15
            self.running = True

            self.bg = [BG(WOODS_PATH, 0, 0.25), BG(WOODS_PATH, WIDTH, 0.25),
                        BG(BRIDGE_PATH, 0), BG(BRIDGE_PATH, WIDTH)]
            
            self.char = Aventureiro()

            self.obstacule = []
            self.start_obstacle()

    def check_colision(self):
        for obstacule in self.obstacule:
            pos = (obstacule.x-self.char.x, obstacule.y-self.char.y)
            if self.char.current_mask().overlap(obstacule.mask, pos)!=None:
                return True
        return False
    
    def start_obstacle(self):
        self.obstacule.append(Bomb(WIDTH))
        for i in range(2):
            x_min = self.obstacule[-1].x+self.obstacule[-1].width + 300
            x_max = self.obstacule[-1].x+self.obstacule[-1].width + 600
            self.obstacule.append(Bomb(random.randint(x_min, x_max)))

    def spawn_cactus(self):
        if self.obstacule[0].x <= -self.obstacule[0].width:
            self.obstacule.pop(0)

            x_min = self.obstacule[-1].x+self.obstacule[-1].width + 200
            x_max = self.obstacule[-1].x+self.obstacule[-1].width + 500

            x_new_cactus = random.randint(x_min, x_max)

            self.obstacule.append( Bomb(x_new_cactus) )
        
def main():

    game = Game()

    loop = 0

    clock = pygame.time.Clock()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    game.char.jump()
                if event.key == pygame.K_r:
                    game.start_game()
                if event.key == pygame.K_s:
                    game.char.deslizar()

        if game.running:
            for bg in game.bg:
                bg.update(-game.speed)
                bg.show()

            game.spawn_cactus()

            for obstacule in game.obstacule:
                obstacule.update(-game.speed)
                obstacule.show()

            game.char.update()
            game.char.show()

            if game.check_colision():
                print("Colisao")

                game.running = False
                game.char.alive=False
                game.obstacule[0].exploded=True

            loop = (loop+1)%100
            
            if(loop%5==0):
                game.update()

            print(game.score)
        else:
            for bg in game.bg:
                bg.show()
            for obstacule in game.obstacule:
                obstacule.update()
                obstacule.show()

            game.char.update()
            game.char.show()

        clock.tick(30)
        pygame.display.update()

main()