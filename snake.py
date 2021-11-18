import pygame
import string
import sys
import random
import time
from Block import Block
from Food import Food

pygame.init()


#define colors
black = (0,0,0)
white = (255, 255, 255)
blue = (0,0,255)
'''
:meta private:
'''
'''
snake.py
date: oct 26 2021
by: Morgan Marino, Michael Talaga, AMA, Divya Shakamuri
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
    :param nextDirection: direction to change to
    :type nextDirection: String
    '''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = 2
        self.head = Block(1, 200, 200)
        self.tail = Block(2, 200, 225) #reassigned later
        self.blocks = pygame.sprite.Group() #create group of blocks
        self.blocks.add(self.tail)
        self.direction = "NULL" #setting direction snke will move in
        self.nextDirection = "NULL"

    def update(self, screenDimensions, foods, bonus):
        '''
        Update movement of snake object via keyboard pressing. \n
        Author: Michael Talaga

        :param screenDimensions: screen dimensions (width,height)
        :type screenDimensions: Tuple
        :param food: Food object to check for collision
        :type food: Food
        :param placedOnSnake: Flag to check if randomly placed food is being placed on snake body
        :type placedOnSnake: Boolean
        :param bonus: ?????????????
        :type bonus: ????????????
        :param chomp: Chomping sound when a snake eats an apple
        :type chomp: pygame mixer sound
        :return: return if there was an unacceptable collision
        :return type: Boolean
        '''
        pressed = pygame.key.get_pressed()
        change = True
        y_change = 0
        x_change = 0
        score = 0

        #arrow key movement
        if pressed[pygame.K_UP] and self.direction != "DOWN":
            self.nextDirection = "UP"
        elif pressed[pygame.K_DOWN] and self.direction != "UP":
            self.nextDirection = "DOWN"
        if pressed[pygame.K_LEFT] and self.direction != "RIGHT":
            self.nextDirection = "LEFT"
        elif pressed[pygame.K_RIGHT] and self.direction != "LEFT":
            self.nextDirection = "RIGHT"

        #added "wasd" movement -MXO
        if pressed[pygame.K_w] and self.direction != "DOWN":
            self.nextDirection = "UP"
        elif pressed[pygame.K_s] and self.direction != "UP":
            self.nextDirection = "DOWN"
        if pressed[pygame.K_a] and self.direction != "RIGHT":
            self.nextDirection = "LEFT"
        elif pressed[pygame.K_d] and self.direction != "LEFT":
            self.nextDirection = "RIGHT"

        # changed to pattern matching -AMA
        #this if statement only allows movement change during a multiple of 25 so it alligns with the grid
        if (self.head.x % 25 == 0 and self.head.y % 25 == 0):
            self.direction = self.nextDirection
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
            if(self.head.x % 25 == 0 and self.head.y % 25 == 0):
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
            if (self.wall_check(screenDimensions)): #check for collision
                return True, bonus, score
		#check for snake body collision
        for block in self.blocks:
            if(block.id != 2):
                if (self.did_eat_block((block.x, block.y), float((block.width / 2))) == True):
                    return True, bonus, score
        #collision check with food
        for i in range(1+bonus):
            if (self.did_eat_block((foods[i].x, foods[i].y), foods[i].width / 2) == True):
                placedOnSnake = True
                while placedOnSnake:
                    placedOnSnake = False
                    foods[i].changePosition(screenDimensions, foods)
                    for block in self.blocks:
                        if (foods[i].x in range (((block.x) - block.width), (block.x + block.width)) and
                        (foods[i].y in range ((block.y - block.width), (block.y + block.width)))):
                            placedOnSnake = True
                chomp = pygame.mixer.Sound("sounds/applesound.wav")
                chomp.set_volume(0.5)
                chomp.play(maxtime=800, fade_ms=250)
                self.add_tail(1)
                if i == 0:
                    score = 1
                else:
                    score = 2
                if i == 0 and bonus == 0:
                    bonus = random.randint(0, 3) > 1
                    if bonus == 1:
                        foods[1].incLife()
                elif bonus and i == bonus:
                    bonus = 0
            if i > 0:
                if foods[i].decLife() == 0:
                    bonus = 0

        return False, bonus, score

    def render(self, screen):
        '''
        Draw objects from snakes block group onto the screen as rectangles. \n
        Author: Michael Talaga

        :param screen: The screen for the game
        :type screen: pygame display
        '''
		#for each in blocks
		#snakeBlocks.draw(screen)
		#pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))
        head = self.head
        for block in self.blocks:
            pygame.draw.rect(screen, white, (block.x, block.y, block.width, block.height))
            pygame.draw.rect(screen, black, (block.x, block.y, block.width, block.height),2)

        pygame.draw.rect(screen, blue, (head.x, head.y, head.width, head.height))
        pygame.draw.rect(screen, black, (head.x, head.y, head.width, head.height),2)

    def wall_collision(self, xmin, xmax, ymin, ymax):
        '''
        ******* what does this do? ********* \n
        Author: ??????

        :param xmin: Left wall x coord
        :type xmin: int
        :param xmax: Right wall x coord
        :type xmax: int
        :param ymin: Top wall y coord
        :type ymin: int
        :param ymax: Bottom wall y coord 
        :type ymax: int
        :return: True if has hit wall
        :rtype: Boolean
        '''
        if (self.head.x <= xmin or self.head.x >= xmax or self.head.y <= ymin or self.head.y >= ymax):
            return True
        else:
            return False

    def wall_check(self, max_size):
        '''
        checks if snake has hit wall \n
        Authors: Michael Talaga

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
        for i in range (0, to_add):
            self.size += to_add
            newBlock = Block(self.size, self.tail.x, self.tail.y)
            self.blocks.add(newBlock)
            self.tail = newBlock


    def did_eat_block(self, coords_2_eat, sideLength):
        '''
        checks if snake has encountered a block \n
        Authors: AMA, Michael Talaga

        :param coords_2_eat: x y of the current, Food
        :type coords_2_eat: [x,y] or (x,y)
        :param sideLength: length of comparison object
        :type sideLength: int
        '''
        #get current head of snake
        copy_body = self.blocks.sprites()
        # troubleshooting
        print(copy_body[0].x, copy_body[0].y)
        #check for overlap of head and tail
        mid = int(sideLength)
        if (self.head.x in range (((coords_2_eat[0]) - mid), (coords_2_eat[0] + mid)) and
            (self.head.y in range ((coords_2_eat[1] - mid), (coords_2_eat[1] + mid)))):
            return True
