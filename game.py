import pygame

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



def draw_screen():



def eval_genomes():

def run(config_file):

def __main__():

