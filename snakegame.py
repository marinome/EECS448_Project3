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
    CLASS COMMENTS HERE

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
