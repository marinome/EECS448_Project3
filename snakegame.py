import pygame
import string
import sys
import random
import time

#external files
from Block import Block
from snake import Snake
from Food import Food

pygame.init()

'''
Main file
date: oct 26 2021
by: Morgan Marino, Michael Talaga, AMA
'''

# MADE COLOR FUNC TO STORE ALL COLORS -AMA
#TODO: define colors, fonts
#define display settings
display_width = 425
display_height = 425
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game - Group 3")
clock = pygame.time.Clock()
pace = 30 #Speed of the game
# initial score
score = 0
#define snake attributes
#snakeBlocks = pygame.sprite.Group()


# class SnakeGame:
#     '''
#     Top level game class.  Will call functions as needed to keep the game running
#
#     Example::
#
#         snakegame =  SnakeGame()
#
#     :param some_param:
#     :type some_param: int
#     '''
#     def __init__(self):
#         self.some_param = 0
#
#     def print_board():
#          return 0
#     def snake_moves():
#          return 0
#     def add_tail():
#          return 0

def get_color(color_string):
    # central place to store all color values
    '''
    pass name of color, return RGB value for color

    :param color_string: name of color
    :type color_string: String
    :return _: The RGB value of the passed color
    :rtype: Tuple (red, green, blue)
    #used to be (red,green,blue) -MEM
    @MEM -> the tuple that is returned, the color, is defined by the amount of red, green and blue, hence the RGB
    '''
    # @MEM lets not delete code, just add another case, this is a generic func 
    match color_string:
        case "red":
            return (255,0,0)
        case "black":
            return (0,0,0)
        case "yellow":
            return (255,255,0)
        case "white":
            return (255,255,255)
        case "blue":
            return (0,0,255)
        case "green":
            return (0,255,0)
        # default, some odd color
        case _:
            return (70,70,70)


def show_score(score_2_display, color, font, size):
    '''
    displays score on screen

    :param score_2_display: score that will be displayed
    :type score_2_display: int
    :param color: color of the score font
    :type color: RGB color
    :param font: font style
    :type font: pygame font name
    :param size: font size
    :type size: int
    '''
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    # create the display surface object
    score_surface = score_font.render('Score : ' + str(score_2_display), True, color)
    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()
    # displaying text
    screen.blit(score_surface, score_rect)

def game_over(font_type, font_size, font_color, final_score):
    '''
    display final score over board

    :param font_type: font style
    :type font_type: pygame font type
    :param font_size: font size
    :type font_size: int
    :param font_color: font color
    :type font_color: RGB color
    :param final_score: final score of game to display
    :type final_score: int
    '''
    end_font = pygame.font.SysFont(font_type, font_size)
    # creating a text surface on which text will be drawn
    game_over_surface = end_font.render('Your Score is : ' + str(final_score), True, get_color(font_color))
    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (display_width/2, display_height/4)
    # blit wil draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # after 2 seconds we will quit the program
    time.sleep(3)

def gridScreen(gridSize, color1, color2):
    '''
    this will add grid lines to the screen \n
    Author: Mason Otto
    needs adjusting, this can be fully implemented in project 4 -MXO

    :meta private:
    '''
    count = 0
    for x in range(25, 400, gridSize):
        for y in range(25, 400, gridSize):
            grid = pygame.Rect(x, y, gridSize, gridSize)
            if (count % 2 == 0):
                pygame.draw.rect(screen, color1, grid, 0)
            else:
                pygame.draw.rect(screen, color2, grid, 0)
            count = count + 1


def game():
    '''
    COMMENTS \n
    Author: Michael Talaga

    :param snake: This is the snake object which will be moving around on the screen. The user will be able to move this with arrow keys or wasd.
    :type snake: Snake, made of, Block
    '''
    exit = False
    snake = Snake(200, 200) #Initializes snake with a starting position (divisible by 5)
    #random food placement
    food = Food(random.choice(range(1, display_width-10, 5)), random.choice(range(1, display_height-10, 5)))

    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                # exit = True
                return snake.size
        screen.fill((0,100,0))
        #should we make border so it's easier to know when you're about to lose? -MEM 
        # border added -MXO
        #need to fix food spawn so they are within the border -MXO
        #following will add grid to screen, can implement in project 4 when it looks prettier -MXO
        gridScreen(15, (0,255,0), (0,200,0))
        snake.render(screen)
        food.render(screen, get_color("red"))
        borderCollide = snake.wall_collision(25,390,25,390)
        snake.update((display_width, display_height), food)
        #borderCollide = snake.update((display_width, display_height), food) #commented this out to make changes for the collision to happen at border not window -MXO
        if (borderCollide == True): #Border collision check
            # exit = True
            return snake.size
        # display score #MT Made snake size for now
        show_score(snake.size, get_color("yellow"), 'times new roman', 20)
        pygame.display.update()
        clock.tick(pace)

def main():
    '''
    Main file to run the game and exit the system when it is finished. \n
    Author: Michael Talaga, AMA

    '''
    game_over('times new roman', 50, "red", game())
    pygame.quit()
    sys.exit()

req_version = (3,10)
curr_version = sys.version_info
if curr_version >= req_version:
    if __name__ == '__main__':
        main()
else:
    # prompt user to update python
    print("Please update your python version to 3.10 or greater")
