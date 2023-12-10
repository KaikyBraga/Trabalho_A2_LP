import os, sys, pygame, random

from variaveis_globais import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption("Dino")

class Personagem():
    def __init__(self, name, qnt_run, qnt_jump, qnt_die, qnt_deslizamento, width, height, y_floor) -> None:
        self.name = name
        self.qnt_run = qnt_run
        self.qnt_jump = qnt_jump
        self.qnt_die = qnt_die
        self.qnt_deslizamento = qnt_deslizamento

        self.width = width
        self.height = height

        self.x = 200 - self.width//2
        self.y_floor = y_floor
        self.y = self.y_floor

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

            if self.y >= self.y_floor:
                self.jumping = False
                self.y = self.y_floor
            
            self.texture_num  = (min(self.texture_num + 0.25, len(self.texture_jump)-1))%len(self.texture_jump)
        elif self.deslizamento:
            self.deslizamento_time -= self.deslizamento_tick*self.alpha/2
            
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
        for i in range(1, self.qnt_run+1):
            run_path = f'sprites/personagens/{self.name}/corrida/{self.name}_corrida_{i}.png'  
            path = os.path.join(run_path)

            img = pygame.image.load(path)

            self.texture_run.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_run.append(pygame.mask.from_surface(self.texture_run[-1]))

        #carrega sprites de pulo
        for i in range(1, self.qnt_jump+1):
            jump_path = f'sprites/personagens/{self.name}/pulo/{self.name}_pulo_{i}.png'  
            path = os.path.join(jump_path)

            img = pygame.image.load(path)

            self.texture_jump.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask_jump.append(pygame.mask.from_surface(self.texture_jump[-1]))
        
        #carrega sprites de morte
        for i in range(1, self.qnt_die+1):
            dead_path = f'sprites/personagens/{self.name}/morte/{self.name}_morte_{i}.png'  
            path = os.path.join(dead_path)

            img = pygame.image.load(path)

            self.texture_dead.append(pygame.transform.scale(img, (self.width, self.height)))
        
        #carrega sprites de deslizamento
        for i in range(1, self.qnt_deslizamento+1):
            deslizamento_path = f'sprites/personagens/{self.name}/deslizamento/{self.name}_deslizamento_{i}.png'  
            path = os.path.join(deslizamento_path)

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
            self.deslizamento_time = 30
            self.deslizamento_tick = 1
            self.texture_num=0

    def current_mask(self):
        if self.jumping:
            return self.mask_jump[int(self.texture_num)]
        elif self.deslizamento:
            return self.mask_deslizamento[int(self.texture_num)]
        else:
            return self.mask_run[int(self.texture_num)]

class Bomb():
    def __init__(self, x) -> None:
        self.width = 100*0.85
        self.height = 100*0.85

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
            self.texture_explosion.append(pygame.transform.scale(img, (3*self.width, 3*self.height))) 
    
    def get_mask(self):
        return self.mask
    
    def explodir(self):
        self.exploded = True
        self.y -= self.height
        self.x -= 30

class Bat():
    def __init__(self, x) -> None:
        self.width = 93
        self.height = 63

        self.x = x
        self.y = Y_FLOOR_BAT

        self.texture_num = 0
        self.texture = []
        self.mask = []

        self.set_texture()
    
    def update(self, dx=0):
        self.x += dx
        self.texture_num  = (self.texture_num + 0.25)%len(self.texture)
    
    def show(self):
        screen.blit(self.texture[int(self.texture_num)], (self.x, self.y))

    def set_texture(self):
        for i in range(1, 5):
            bat_path = f'sprites/obstaculos/morcego/morcego_{i}.png'
            path = os.path.join(bat_path)

            img = (pygame.image.load(path))
            
            self.texture.append(pygame.transform.scale(img, (self.width, self.height)))
            self.mask.append(pygame.mask.from_surface(self.texture[-1]))

    def get_mask(self):
        return self.mask[int(self.texture_num)]
    
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
        self.speed  = min(20, 8 + 2*(self.score//100))
        self.char.alpha = self.speed/5

    def start_game(self):
        if self.running==False:
            self.score = 0
            self.speed = 8
            self.running = True

            self.bg = [BG(WOODS_PATH, 0, 0.25), BG(WOODS_PATH, WIDTH, 0.25),
                        BG(BRIDGE_PATH, 0), BG(BRIDGE_PATH, WIDTH)]
            
            self.char = Personagem('aventureiro', 6, 4, 7, 2, WIDTH_AVENTUREIRO, HEIGHT_AVENTUREIRO, Y_FLOOR_AVENTUREIRO)
            #self.char = Personagem('cavaleiro', 10, 3, 10, 2, WIDTH_CAVALEIRO, HEIGHT_CAVALEIRO, Y_FLOOR_CAVALEIRO)
            #self.char = Personagem('guerreira', 8, 3, 11, 3, WIDTH_GUERREIRA, HEIGHT_GUERREIRA, Y_FLOOR_GUERREIRA)
            #self.char = Personagem('guerreiro', 8, 2, 9, 2, WIDTH_GUERREIRO, HEIGHT_GUERREIRO, Y_FLOOR_GUERREIRO)
            
            self.obstacle = []
            self.start_obstacles()

    def check_colision(self):
        for obstacle in self.obstacle:
            pos = (obstacle.x-self.char.x, obstacle.y-self.char.y)
            if self.char.current_mask().overlap(obstacle.get_mask(), pos)!=None:
                return True
        return False
    
    def start_obstacles(self):
        self.obstacle.append(Bomb(WIDTH))
        for i in range(2):
            x_min = self.obstacle[-1].x+self.obstacle[-1].width + 300
            x_max = self.obstacle[-1].x+self.obstacle[-1].width + 600
            self.obstacle.append(Bomb(random.randint(x_min, x_max)))

    def spawn_obstacles(self):
        if self.obstacle[0].x <= -self.obstacle[0].width:
            self.obstacle.pop(0)

            x_min = self.obstacle[-1].x+self.obstacle[-1].width + 200
            x_max = self.obstacle[-1].x+self.obstacle[-1].width + 800

            x_new_obstacle = random.randint(x_min, x_max)

            rand_type = random.randint(1, 100)
            if rand_type <= 50:
                self.obstacle.append( Bomb(x_new_obstacle) )
            else:
                self.obstacle.append( Bat(x_new_obstacle) )
        
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

            game.spawn_obstacles()

            for obstacle in game.obstacle:
                obstacle.update(-game.speed)
                obstacle.show()

            game.char.update()
            game.char.show()

            if game.check_colision():
                print("Colisao")

                game.running = False
                game.char.alive=False

                if isinstance(game.obstacle[0], Bomb):
                    game.obstacle[0].explodir()

            loop = (loop+1)%100
            
            if(loop%5==0):
                game.update()

            print(game.score)
        else:
            for bg in game.bg:
                bg.show()
            for obstacle in game.obstacle:
                obstacle.update()
                obstacle.show()

            game.char.update()
            game.char.show()

        clock.tick(30)
        pygame.display.update()

main()