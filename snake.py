import pygame
import string
import sys
import random
import time
from Block import Block
from Food import Food

pygame.init()

#define white for snake
white = (255, 255, 255)
blue = (0,0,255)
'''
snake.py
date: oct 26 2021
by: Morgan Marino, Michael Talaga, AMA
'''


class Snake(pygame.sprite.Sprite):
    '''
    Creates a snake class which will move around on the board and be controled
    by the user. If it encounters food it will grow the snake.  If the snake touches
    the edge of the board, the game will end.

    Example::

        snake =  Snake(100, 200)
        snake._(_)

    :param size: Size of snake
    :type size: int
    :param head: The head of the snake
    :type head: Block
    :param tail: tail of the snake
    :type tail: Block
    :param blocks: A collection of blocks for each block of the snake
    :type blocks: sprite group from pygame's library which
    :param direction: The direction the snake is currently moving - defaulted to still but can be up,down,left, or right
    :type direction: String
    '''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = 2
        self.head = Block(1, 200, 200)
        self.tail = Block(2, 200, 210) #reassigned later
        self.blocks = pygame.sprite.Group() #create group of blocks
        self.blocks.add(self.tail)
        self.direction = "NULL" #setting direction snke will move in


    def update(self, screenDimensions, food):
        '''
        Update movement of snake object via keyboard pressing. \n
        Author: Michael Talaga

        :param screenDimensions: screen dimensions (width,height)
        :type screenDimensions: Tuple
        :param food: Food object to check for collision
        :type food: Food
        :param pressed: The pygame method for receiving a signal from the keyboard
        :type pressed: Pygame function
        :param change: Dictating if the snake will change its direction. Blocks will readjust location based on this.
        :type change: boolean
        :param y_change: The amount the snake moves in the vertical direction per turn (can be positive or negative)
        :type y_change: int
        :param x_change: The amount the snake moves in the horizontal direction per turn (can be positive or negative)
        :type x_change: int
        :return: return if there was an unacceptable collision
        :return type: boolean
        '''
        pressed = pygame.key.get_pressed()
        change = True
        y_change = 0
        x_change = 0
        if pressed[pygame.K_UP] and self.direction != "DOWN":
            self.direction = "UP"
        elif pressed[pygame.K_DOWN] and self.direction != "UP":
            self.direction = "DOWN"
        if pressed[pygame.K_LEFT] and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif pressed[pygame.K_RIGHT] and self.direction != "LEFT":
            self.direction = "RIGHT"
        # changed to pattern matching -AMA
        match self.direction:
            case "UP":
                y_change -= self.head.speed
            case "DOWN":
                y_change += self.head.speed
            case "LEFT":
                x_change -= self.head.speed
            case "RIGHT":
                x_change += self.head.speed
            # default
            case _:
                change = False

		#Function to update each block's location and adhere to snake movement rules
        if change and len(self.blocks) > 0:
            prevx = self.head.x
            prevy = self.head.y
            for block in self.blocks:
                currentx = block.x
                currenty = block.y
                block.x = prevx
                block.y = prevy
                prevx = currentx
                prevy = currenty

			#Make change to head
            self.head.x += x_change
            self.head.y += y_change
            #if self.head.y < 50: #tail add test
                #self.add_tail(1)
            #check for collision
            if (self.wall_check(screenDimensions)):
                return True
		#check for snake body collision
        for block in self.blocks:
            if(block.id not in range (2, 8)):
                if (self.did_eat_block((block.x,block.y), block.width) == True):
                    return True
        #collision check with food 
        if (self.did_eat_block((food.x,food.y), food.width) == True):
            food.changePosition(screenDimensions)
            self.add_tail(1)
        



    def render(self, screen):
        '''
        Draw objects from snakes block group onto the screen as rectangles. \n
        Author: Michael Talaga

        :param screen: The screen for the game
        :type screen: pygame display
        :param head: Head of snake
        :type head: block
        '''
		#for each in blocks
		#snakeBlocks.draw(screen)
		#pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))
        head = self.head
        pygame.draw.rect(screen, blue, (head.x, head.y, head.width, head.height))
        for block in self.blocks:
            pygame.draw.rect(screen, white, (block.x, block.y, block.width, block.height))

    def wall_check(self, max_size):
        '''
        checks if snake has hit wall \n
        Authors: Michael Talaga, ...

        :param max_size: max x & y size of game board
        :type max_size: Tuple of (x, y)
        '''
        if ((self.head.x + self.head.width) > (max_size[0])) or ((self.head.y + self.head.height) > (max_size[1])):
            return True
        if (self.head.x < 0 or self.head.y < 0):
            return True
        else:
            return False

    def add_tail(self, to_add):
        '''
        when called it will add to tail and add block to block group \n
        Authors: AMA, Michael Talaga

        :param to_add: integer to increment the size of the snake body
        :type to_add: int
        '''
        #get current self.tail position
        #increment self.tail by to_add

        for i in range (0, to_add):
            self.size += to_add
            newBlock = Block(self.size, self.tail.x, self.tail.y)
            self.blocks.add(newBlock)
            self.tail = newBlock
            

        #self.blocks.add(Block(coords[0], coords[1]))


    def did_eat_block(self, coords_2_eat, sideLength):
        '''
        checks if snake has encountered a block \n
        Authors: AMA, Michael Talaga

        :param coords_2_eat: x y of the current, Food
        :type coords_2_eat: [x,y] or (x,y)
        :param sideLength: length of comparison object
        :type sideLength: int
        :param mid: middle of side length
        :type mid: int
        '''
        #get current head of snake
        copy_body = self.blocks.sprites()
        # troubleshooting
        print(copy_body[0].x, copy_body[0].y)
        #get position of any blocks on board - this is coords param
        
        #check for overlap of head and tail
        mid = int(sideLength * 0.8)
        if (self.head.x in range (((coords_2_eat[0]) - mid), (coords_2_eat[0] + sideLength)) and (self.head.y in range ((coords_2_eat[1] - mid), (coords_2_eat[1] + sideLength)))):
            return True



















#
