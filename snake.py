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
by: Morgan Marino, Michael Talaga, AMA
'''


class Snake(pygame.sprite.Sprite):
    '''
    Creates a snake class which will move around on the board and be controled
    by the user. It will avoid collisions with itself and the boundaries.

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
        self.size = 1
        self.head = Block(200, 200)
        self.tail = Block(200, 205) #reassigned later
        self.blocks = pygame.sprite.Group() #create group of blocks
        self.blocks.add(self.head, self.tail)
        self.direction = "NULL" #setting direction snke will move in


    def update(self, screenDimensions, food):
        '''
        Update movement of snake object via keyboard pressing. \n
        Autor: Michael Talaga

        :param screenDimensions: screen dimensions (width,height)
        :type screenDimensions: tuple
        :param food: Food object to check for collision
        :type food: food sprite
        :param pressed: The pygame method for receiving a signal from the keyboard
        :type pressed: Pygame function
        :param change: Dictating if the snake will change its direction. Blocks will readjust location based on this.
        :type change: boolean
        :param y_change: The amount the snake moves in the vertical direction per turn (can be positive or negative)
        :type y_change: int
        :param x_change: The amount the snake moves in the horizontal direction per turn (can be positive or negative)
        :type x_change: int
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

        # if self.direction == "UP":
        #     y_change -= self.head.speed
        # elif self.direction == "DOWN":
        #     y_change += self.head.speed
        # elif self.direction == "LEFT":
        #     x_change -= self.head.speed
        # elif self.direction == "RIGHT":
        #     x_change += self.head.speed
        # else:
        #     change = False

		#Function to update each block's location and adhere to snake movement rules
        if change and len(self.blocks) > 1:
            iter = 0
            for block in self.blocks:
                if iter == 0:
                    prevx = block.x
                    prevy = block.y
                elif iter != 0:
                    currentx = block.x
                    currenty = block.y
                    block.x = prevx
                    block.y = prevy
                    prevx = currentx
                    prevy = currenty

                iter+=1
			#Make change to head
            self.head.x += x_change
            self.head.y += y_change
            #if self.head.y < 50: #tail add test
                #self.add_tail(1)
            #check for collision
            if (self.wall_check(screenDimensions)):
                return True
		#return 0
        if (self.did_eat_block((food.x,food.y), food.width) == True):
            food.changePosition(screenDimensions)
            self.add_tail(1)


    def render(self, screen):
        '''
        Draw objects from snakes block group onto the screen as rectangles. \n
        Autor: Michael Talaga

        :param screen: The screen for the game
        :type screen: pygame display
        '''
		#for each in blocks
		#snakeBlocks.draw(screen)
		#pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))
        for block in self.blocks:
            if block == self.head:
                pygame.draw.rect(screen, blue, (block.x, block.y, block.width, block.height))
            else:
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



        return True

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
            newBlock = Block(self.tail.x, self.tail.y)
            self.blocks.add(newBlock)
            self.tail = newBlock
            self.size += to_add

        #self.blocks.add(Block(coords[0], coords[1]))


    def did_eat_block(self, coords_2_eat, sideLength):
        '''
        checks if snake has encountered a block

        :param coords_2_eat: x y of the current, Food
        :type coords_2_eat: x,y
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
        # if copy_body[0].x == coords_2_eat[0] and copy_body[0].y == coords_2_eat[1]:
        #     # self.blocks.add()
        #     self.add_tail(coords_2_eat)
        mid = int(sideLength * 0.8)
        if (self.head.x in range ((coords_2_eat[0] - mid), (coords_2_eat[0] + sideLength))  and self.head.y in range ((coords_2_eat[1] - mid), (coords_2_eat[1] + mid))):
            return True

















#
