import pygame
import string
import sys
import random
import time

pygame.init()

'''
Food.py
date: oct 29 2021
by: Morgan Marino, Michael Talaga, AMA
'''



class Food(pygame.sprite.Sprite):
    '''
    Food for the sanke to eat

    Example::

        food =  Food(100, 200)

    :param x: x position
    :type x: int
    :param y: y postiion
    :type y: int
    :param width: food width
    :type width: int
    :param height: food height
    :type height: int
    '''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = 1000 #block number
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10

    def changePosition(self, screenDimensions):
        '''
        Change the position of food upon collision with snake head, ensure it is at snake head
        Author: Michael Talaga

        :param screenDimensions: dimensions for the screen
        :type screenDimensions: tuple as (x, y) for (width, height)
        '''
        self.x = random.randrange(1, screenDimensions[0]-10)
        self.y = random.randrange(1, screenDimensions[1]-10)

    #def update(self, screenDimensions):

    def render(self, screen, color):
        '''
         Draw food object onto the screen. \n
         Author: Michael Talaga

        :param screen: The screen for the game
        :type screen: pygame display
        :param color: color of the food
        :type color: String
        '''
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
