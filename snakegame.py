import pygame
import string
import sys
import random
import time

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
pace = 10 #Speed of the game
#define snake attributes
#snakeBlocks = pygame.sprite.Group()


class SnakeGame:
 def print_board():
     return 0
 def snake_moves():
     return 0
 def add_tail():
     return 0


class Snake(pygame.sprite.Sprite):
    '''
    CLASS COMMENTS HERE

    Example::

        snake =  Snake(100, 200)
        snake.game()

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
        self.x = x
        self.y = y
        self.speed = 10
        self.width = 5
        self.height = 5
        #self.blocks = pygame.sprite.Group()
        #self.blocks.add()


    def update(self):
        '''
        COMMENTS \n
        Author: \n

        :meta private:
        '''
    	#Add wasd
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.y -= self.speed
        if pressed[pygame.K_DOWN]:
            self.y += self.speed
        if pressed[pygame.K_LEFT]:
            self.x -= self.speed
        if pressed[pygame.K_RIGHT]:
            self.x += self.speed
        return 0

    def render(self, screen):
        '''
        COMMENTS \n
        Autor: \n

        :param screen:
        :type screen:
        '''
    	#for each in blocks
    	#snakeBlocks.draw(screen)
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))


    def game(self):
        '''
        COMMENTS \n
        Autor: \n

        :param :
        :type :
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

    def main(self):
        '''
        COMMENTS \n
        Autor: \n

        :param :
        :type :
        '''
        game()
        pygame.quit()
        sys.exit()

main()
