import pygame
import string
import sys
import random
import time

pygame.init()

'''
snake.py
by: Morgan Marino, Michael Talaga, AMA
'''


class Snake(pygame.sprite.Sprite):
    '''
    CLASS COMMENTS HERE

    Example::

        snake =  Snake(100, 200)
        snake.game()

    :param head:
    :type head:
    :param testBlock:
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


    def update(self):
        '''
        COMMENTS \n
        Autor: \n

        :param :
        :type :
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

        if self.direction == "UP":
            y_change -= self.head.speed
        elif self.direction == "DOWN":
            y_change += self.head.speed
        elif self.direction == "LEFT":
            x_change -= self.head.speed
        elif self.direction == "RIGHT":
            x_change += self.head.speed
        else:
            change = False
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
		#return 0

    def render(self, screen):
        '''
        COMMENTS \n
        Autor: \n

        :param :
        :type :
        '''
		#for each in blocks
		#snakeBlocks.draw(screen)
		#pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))
        for block in self.blocks:
            pygame.draw.rect(screen, white, (block.x, block.y, block.width, block.height))


def game():
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

# main()
