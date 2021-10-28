import pygame
import string
import sys
import random
import time

pygame.init()

'''
Blcok.py
by: Morgan Marino, Michael Talaga, AMA
'''



class Block(pygame.sprite.Sprite):
    '''
    CLASS COMMENTS HERE

    Example::

        block =  Block(100, 200)

    :param x:
    :type x: int
    :param y:
    :type y: int
    :param speed: snake speed
    :type speed: int
    :param width: snake width
    :type width: int
    :param height: snake height
    :type height: int
    '''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = 1 #block number
        self.x = x
        self.y = y
        self.speed = 5
        self.width = 5
        self.height = 5
