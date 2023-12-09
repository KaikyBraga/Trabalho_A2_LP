import os, sys, pygame, random

WIDTH = 623
HEIGHT = 150   

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino")

class Dino(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.width = 44
        self.height = 44

        self.x= 30
        self.y= 80

        self.jumping = False
        self.dy = 0
        self.ddy = 0.75

        self.texture_num = 0
        self.texture = [None, None, None]
        self.mask = None
        self.rect = None
        self.set_texture()
    
    def update(self):
        if self.jumping:
            self.y -= self.dy
            self.dy -= self.ddy

            if self.y >=80:
                self.jumping = False
                self.y=80
        else:
            self.texture_num  = (self.texture_num + 0.25)%3

    def show(self): 
        screen.blit(self.texture[int(self.texture_num)], (self.x, self.y))

    def set_texture(self):
        for i in range(3):  
            path = os.path.join(f'assets/images/dino{i}.png')
            self.texture[i] = pygame.image.load(path)
            self.texture[i] = pygame.transform.scale(self.texture[i], (self.width, self.height))

        self.mask = pygame.mask.from_surface(self.texture[0])
        self.rect = self.texture[0].get_rect()

    def jump(self):
        if self.jumping==False:
            self.dy=10
            self.jumping = True
            self.texture_num=0

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.width = 34
        self.height = 44

        self.x= x
        self.y= 80

        self.texture_num = 0
        self.texture = None
        self.mask = None
        self.rect = None

        self.set_texture()
    
    def update(self, dx):
       self.x += dx

       if self.x<=-34:
           self.x=WIDTH

    def show(self): 
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join(f'assets/images/cactus.png')
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

        self.mask = pygame.mask.from_surface(self.texture)
        self.rect = self.texture.get_rect()
class BG:
    def __init__(self, x=0) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        
        self.texture = None
        self.set_texture()
    
    def update(self, dx):
        self.x += dx
        if self.x <= -self.width:
            self.x = self.width

    def show(self):
        screen.blit(self.texture, (self.x, self.y))
 
    def set_texture(self):
        path = os.path.join('assets/images/bg.png')
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Game():
    def __init__(self) -> None:
        self.speed = 5
        self.running = True

        self.bg = [BG(0), BG(WIDTH)]
        
        self.dino = Dino()

        self.obstacule = []
        self.start_obstacle()

    def start_game(self):
        if self.running==False:
            self.speed = 5
            self.running = True

            self.bg = [BG(0), BG(WIDTH)]
            
            self.dino = Dino()

            self.obstacule = []
            self.start_obstacle()

    def check_colision(self):
        group_obstacule = pygame.sprite.Group()
        
        for obstacule in self.obstacule:
            obstacule.rect.x = obstacule.x
            obstacule.rect.y = obstacule.y

            group_obstacule.add(obstacule)

        self.dino.rect.x = self.dino.x
        self.dino.rect.y = self.dino.y

        collision = pygame.sprite.spritecollide(self.dino, group_obstacule, False, pygame.sprite.collide_mask)

        return collision
    
    def start_obstacle(self):
        self.obstacule.append(Cactus(WIDTH))
        for i in range(2):
            self.obstacule.append(
                Cactus(random.randint(self.obstacule[-1].x+4*self.dino.width, self.obstacule[-1].x+WIDTH//1.5)))

    def spawn_cactus(self):
        if self.obstacule[0].x <= -self.obstacule[0].width:
            self.obstacule.remove(0)

            x_max_obstaculo = self.obstacule[-1].x

            x_new_cactus = random.randint(x_max_obstaculo+self.dino*3, x_max_obstaculo+WIDTH//1.5)
            self.obstacule.append( Cactus(x_new_cactus) )
        
def main():

    game = Game()

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
            
            game.dino.update()
            game.dino.show()

            game.spawn_cactus()

            for obstacule in game.obstacule:
                obstacule.update(-game.speed)
                obstacule.show()
            
            #print(game.check_colision())
            if game.check_colision():
                print("Colisao")
                game.running = False

        clock.tick(30)
        pygame.display.update()

main()