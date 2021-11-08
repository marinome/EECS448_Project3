import pygame
import string
import sys
import random
import time

pygame.init()

'''
Block.py
by: Morgan Marino, Michael Talaga, AMA
'''



class Block(pygame.sprite.Sprite):
    '''
    sprites that make up the snake body segments

    Example::

        block =  Block(100, 200)

    :param id: sprite unique id 
    :type id: int
    :param x: x position
    :type x: int
    :param y: y postiion
    :type y: int
    :param speed: block speed
    :type speed: int
    :param width: block width
    :type width: int
    :param height: block height
    :type height: int
    '''
    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = id #block number
        self.x = x
        self.y = y
        self.speed = 5
        self.width = 10
        self.height = 10
