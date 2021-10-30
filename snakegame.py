import pygame
import string
import sys
import random
import time

#external files
from Block import Block
from snake import Snake
from Food import Food

pygame.init()

'''
Main file
by: Morgan Marino, Michael Talaga
'''

#TODO: define colors, fonts
green = (0, 255, 0)
white = (255, 255, 255)
#define display settings
display_width = 500
display_height = 400
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game - Group 3")
clock = pygame.time.Clock()
pace = 30 #Speed of the game
# initial score
score = 0
#define snake attributes
#snakeBlocks = pygame.sprite.Group()


class SnakeGame:
    '''
    Top level game class.  Will call functions as needed to keep the game running

    Example::

        snakegame =  SnakeGame()

    :param some_param:
    :type some_param: int
    '''
    def __init__(self):
        self.some_param = 0

    def print_board():
         return 0
    def snake_moves():
         return 0
    def add_tail():
         return 0



# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    # create the display surface object
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()
    # displaying text
    screen.blit(score_surface, score_rect)

def game():
    '''
    COMMENTS \n
    Autor: Michael Talaga

    :param snake: This is the snake object which will be moving around on the screen. The user will be able to move this with keys.
    :type snake: Snake, made of, Block
    '''
    exit = False
    snake = Snake(200, 200) #Initializes snake with a starting position
    #random food placement
    food = Food(random.randrange(1, display_width//10) * 10, random.randrange(1, display_height//10) * 10)

    while not exit:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                exit = True


        screen.fill(green)
        snake.render(screen)
        snake.update()
        # display score
        show_score(score, white, 'times new roman', 20)
        pygame.display.update()
        clock.tick(pace)

def main():
    '''
    Main file to run the game and exit the system when it is finished. \n
    Autor: Michael Talaga

    '''
    game()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
