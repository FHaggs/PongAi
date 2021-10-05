import pygame
import random
import neat

WIN_WIDTH = 490
WIN_HEIGHT = 370

class Paddle:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.heigth = WIN_HEIGHT/10

        self.vel = 0
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_up(self):
    
        self.vel -5
    
    def move_down(self):

        self.vel = 5

    def move_stop(self):

        self.vel = 0

    def move(self):
        # Check if is hiting the top or bottom of the screen
        if self.rectangle.top => WIN_HEIGHT and self.vel > 0:
            self.vel = 0
        elif self.rectangle.top => 0 and self.vel > 0:
            self.vel = 0

        self.rectangle = self.rectangle.move([0, self.vel])
    
    def draw(self, screen):

        pygame.draw.rect(screen, (255,255,255), self.rectangle)
        
    
        
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vel = [random_1()*3, random_1()*3] # [x, y]
        self.width = 8
        
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.width)

    def change_y(self):
        self.vel[1] = - self.vel[1] 
        
    def change_x(self):
        self.vel[0] = - self.vel[0] 
    

    def move(self):
        if self.rectangle.top => 0 or self.rectangle.bottom => WIN_HEIGHT:
            self.change_y()
        self.rectangle = self.rectangle.move([self.vel[0], self.vel[1]])

    def draw(screen):
        pygame.draw.rect(screen, (255,255,255), self.rectangle)


def random_1():
    i = randint(0,1)

    if i == 0:
        return -1
    else: 
        return 1



def draw_screen(screen, balls, paddles, paddles_r): # rigth paddles = paddles_r
    screen.fill((0,0,0)) # Fill the screen black

    for paddle in paddles:
        paddle.draw(screen)

    for paddle in paddles_r:
        paddle.draw(screen)

    for ball in balls:
        ball.draw(screen)

    pygame.display.update()



def eval_genomes(genomes, config):
    nets = []
    ge = []
    paddles = []
    paddles_r = []
    balls = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)

        paddles.append(Paddle(0, 160))
        paddles.append(Paddle(WIN_WIDTH - 5, 160))
        balls.append(randint(240, 260), randint(180, 200))



        g.fitness = 0
        ge.append(g)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        for x, paddle in enumerate(paddles):
            paddle.move()
            ge[x].fitness += 0.05

            output = nets[x].activate((pad))


        for x, paddle_r in enumerate(paddles_r):
            paddle_r.move()
            ge[x].fitness += 0.05

            output = nets[x].activate((pad))


def run(config_file):
    conf = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config)

    p = neat.Population(conf)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)

if __name__ = "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)


