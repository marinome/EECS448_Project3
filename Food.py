import pygame
import string
import sys
import random
import time
from Block import Block

pygame.init()

'''
Food.py
date: oct 29 2021
by: Morgan Marino, Michael Talaga, AMA, Divya Shakamuri
'''



class Food(pygame.sprite.Sprite):
    '''
    Food for the sanke to eat

    Example::

        food =  Food(100, 200)
        food._(_)

    :param x: x position
    :type x: int
    :param y: y postiion
    :type y: int
    :param width: food width
    :type width: int
    :param height: food height
    :type height: int
    '''
    def __init__(self, x, y, gold):
        pygame.sprite.Sprite.__init__(self)
        self.id = 1000 #block number
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        if gold:
            self.apple_img = pygame.image.load('gold.png').convert_alpha()
        else:
            self.apple_img = pygame.image.load('red.png').convert_alpha()

    def getPosition(self):
        return self.x, self.y

    def changePosition(self, screenDimensions, foods):
        '''
        Change the position of food upon collision with snake head, ensure it is at snake head
        Author: Michael Talaga

        :param screenDimensions: dimensions for the screen
        :type screenDimensions: tuple as (x, y) for (width, height)
        '''
        #self.x = random.randrange(5, screenDimensions[0]-10)
        #self.y = random.randrange(5, screenDimensions[1]-10)
        xys = []
        for food in foods:
            x, y = food.getPosition()
            xys.append((x, y))
        x = random.choice(range(25, screenDimensions[0]-25, 25))
        y = random.choice(range(25, screenDimensions[0]-25, 25))
        while (x, y) in xys:
            x = random.choice(range(25, screenDimensions[0]-25, 25))
            y = random.choice(range(25, screenDimensions[0]-25, 25))
        self.x = x
        self.y = y
    #def update(self, screenDimensions):

    def render(self, screen, color, Block,snake):
        '''
         Draw food object onto the screen. \n
         Author: Michael Talaga

        :param screen: The screen for the game
        :type screen: pygame display
        :param color: color of the food
        :type color: String
        '''
        if (self.x > 30 and self.x < 395 and self.y > 30 and self.y < 395 and self.x and self.x != Block and self.y != Block and self.x != snake and self.y != snake):
            screen.blit(self.apple_img, (self.x, self.y, self.width, self.height))
            #pygame.draw.circle(screen, color, (self.x, self.y), 10,0) #Circle for food might look better than square. -MXO
        else:
            self.x = random.choice(range(25, 400, 25))
            self.y = random.choice(range(25, 400, 25))
            #self.x = random.randrange(30, 390) #can change to not hard coded values later, but this allows food to spawn in border -MXO
            #self.y = random.randrange(30, 390) #can change to not hard coded values later, but this allows food to spawn in border -MXO
            self.render(screen,color,Block,snake)
