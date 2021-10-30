import pygame
import string
import sys
import random
import time

pygame.init()

'''
Food.py
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
        self.id = 1 #block number
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
