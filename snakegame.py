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
#define display settings
width = 500
height = 400
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Snake Game - Group 3")
clock = pygame.time.Clock() 
pace = 10 #Speed of the game



class SnakeGame:
 def print_board():
     return 0
 def snake_moves():
     return 0
 def add_tail():
     return 0


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


    def update(self):
        #if pressed[pygame.K_UP]:
        return 0


def game():
    exit = False


    while not exit:

        screen.fill(green)





        pygame.display.update()
        clock.tick(pace)

    
def main():
    game()
    pygame.quit()
    quit()

