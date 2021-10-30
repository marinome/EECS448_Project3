import pygame
import string
import sys
import random
import time

#external files
from Block import Block
from snake import Snake

pygame.init()

'''
Main file
by: Morgan Marino, Michael Talaga
'''

#TODO: define colors, fonts
green = (0, 255, 0)
white = (255, 255, 255)
#define display settings
width = 500
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game - Group 3")
clock = pygame.time.Clock()
pace = 30 #Speed of the game
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

def game():
    '''
    COMMENTS \n
    Autor: Michael Talaga

    :param snake: This is the snake object which will be moving around on the screen. The user will be able to move this with keys.
    :type snake: Snake, made of, Block
    '''
    exit = False
    snake = Snake(200, 200) #Initializes snake with a starting position

    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit = True


        screen.fill(green)
        snake.render(screen)
        snake.update()
        pygame.display.update()
        clock.tick(pace)

def main():
    '''
    Main file to run the game and exit the system when it is finished. \n
    Autor: Michael Talaga

    :param :
    :type :N/A
    '''
    game()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
