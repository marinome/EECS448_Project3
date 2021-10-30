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

    :param head: The head of the snake
    :type head: Block
    :param testBlock: a block that acts as the 2nd block of the snake
    :type testBlock: Block
    :param tail: tail of the snake
    :type tail: Block
    :param blocks: A collection of blocks for each block of the snake
    :type blocks: sprite group from pygame's library which
    :param direction: The direction the snake is currently moving - defaulted to still but can be up,down,left, or right
    :type direction: String
    '''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.head = Block(200, 200)
        self.testBlock = Block(200, 205) #test
        self.testBlock2 = Block(200, 210) #test
        self.testBlock3 = Block(200, 210) #test
        self.tail = self.testBlock2
        self.blocks = pygame.sprite.Group() #create group of blocks
        self.blocks.add(self.head)
        self.blocks.add(self.testBlock)
        self.blocks.add(self.testBlock2)
        self.blocks.add(self.testBlock3)
        self.direction = "NULL" #setting direction snke will move in


    def update(self, screenDimensions):
        '''
        Update movement of snake object via keyboard pressing. \n
        Autor: Michael Talaga

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
                return 0
		#return 0
        self.did_eat_block((100,100))

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
            pygame.draw.rect(screen, white, (block.x, block.y, block.width, block.height))

    def wall_check(self, max_size):
        '''
        checks if snake has hit wall
        Authors: Michael Talaga, ...
        :param max_size: max x & y size of game board
        :type max_size: Tuple of (x, y)
        '''
        if ((self.head.x + self.head.width) > (max_size[0])) or ((self.head.y + self.head.height) > (max_size[1])):
            return True



        return True

    def add_tail(self, to_add):
        '''
        when called it will add to tail and add block to block group \n
        Authors: AMA, ...

        :param to_add: integer to increment the size of the snake body
        :type to_add: int
        '''
        #get current self.tail position
        #increment self.tail by to_add

        for i in range (0, to_add):
            newBlock = Block(self.tail.x, self.tail.y)
            self.blocks.add(newBlock)
            
        self.blocks.add(Block(coords[0], coords[1]))


    def did_eat_block(self, coords_2_eat):
        '''
        checks if snake has encountered a block

        :param coords_2_eat: x y of the current, Food
        :type coords_2_eat: x,y
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

















#
