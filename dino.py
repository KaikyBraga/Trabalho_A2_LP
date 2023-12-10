import os, sys, pygame, random

from variaveis_globais import BRIDGE_PATH, WOODS_PATH

WIDTH = 1200
HEIGHT = 720   

Y_FLOOR = 450
Y_FLOOR_AVENTUREIRO = 450

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption("Dino")

class Character():
    def __init__(self) -> None:
        self.width = 50 * 5
        self.height = 37 * 5

        self.x = 30
        self.y = Y_FLOOR_AVENTUREIRO - self.height//2

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

            if self.y >= Y_FLOOR_AVENTUREIRO - self.height//2:
                self.jumping = False
                self.y = Y_FLOOR_AVENTUREIRO - self.height//2
            
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
        self.y = Y_FLOOR

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
        self.dino.alpha = self.speed/5

    def start_game(self):
        if self.running==False:
            self.score = 0
            self.speed = 15
            self.running = True

            self.bg = [BG(WOODS_PATH, 0, 0.25), BG(WOODS_PATH, WIDTH, 0.25),
                        BG(BRIDGE_PATH, 0), BG(BRIDGE_PATH, WIDTH)]
            
            self.dino = Character()

            self.obstacule = []
            self.start_obstacle()

    def check_colision(self):
        for obstacule in self.obstacule:
            pos = (obstacule.x-self.dino.x, obstacule.y-self.dino.y)
            if self.dino.current_mask().overlap(obstacule.mask, pos)!=None:
                return True
        return False
    
    def start_obstacle(self):
        self.obstacule.append(Bomb(WIDTH))
        for i in range(2):
            x_min = self.obstacule[-1].x+1*self.dino.width
            x_max = self.obstacule[-1].x+5*self.dino.width
            self.obstacule.append(Bomb(random.randint(x_min, x_max)))

    def spawn_cactus(self):
        if self.obstacule[0].x <= -self.obstacule[0].width:
            self.obstacule.pop(0)

            x_min = self.obstacule[-1].x+1*self.dino.width
            x_max = self.obstacule[-1].x+5*self.dino.width

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
                if event.key == pygame.K_SPACE:
                    game.dino.jump()
                if event.key == pygame.K_r:
                    game.start_game()

        if game.running:
            for bg in game.bg:
                bg.update(-game.speed)
                bg.show()

            game.spawn_cactus()

            for obstacule in game.obstacule:
                obstacule.update(-game.speed)
                obstacule.show()

            game.dino.update()
            game.dino.show()

            if game.check_colision():
                print("Colisao")

                game.running = False
                game.dino.alive=False
                game.obstacule[0].exploded=True

            loop = (loop+1)%100
            
            if(loop%2==0):
                game.update()

            print(game.score)
        else:
            for bg in game.bg:
                bg.show()
            for obstacule in game.obstacule:
                obstacule.update()
                obstacule.show()

            game.dino.update()
            game.dino.show()

        clock.tick(30)
        pygame.display.update()

main()