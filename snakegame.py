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
by: Morgan Marino, Michael Talaga
'''

# MADE COLOR FUNC TO STORE ALL COLORS -AMA
#TODO: define colors, fonts
# green = (0, 255, 0)
# white = (255, 255, 255)
#define display settings
display_width = 400
display_height = 400
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game - Group 3")
clock = pygame.time.Clock()
pace = 30 #Speed of the game
# initial score
score = 0
#define snake attributes
#snakeBlocks = pygame.sprite.Group()


class SnakeGame:
    '''
    Top level game class.  Will call functions as needed to keep the game running

    Example::

        snakegame =  SnakeGame()

    :param some_param:
    :type some_param: int
    '''
    def __init__(self):
        self.some_param = 0

    def print_board():
         return 0
    def snake_moves():
         return 0
    def add_tail():
         return 0

def get_color(color_string):
    # central place to store all color values
    '''
    pass name of color, return RGB value for color

    :param color_string: name of color
    :type color_string: str
    :return _: The RGB value of the passed color
    :rtype: tuple (red, green, blue)
    '''
    match color_string:
        case "red":
            return (255,0,0)
        case "green":
            return (0,255,0)
        case "blue":
            return (0,0,255)
        case "white":
            return (255,255,255)
        # return black of no match
        case _:
            return (0,0,0)


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

def game():
    '''
    COMMENTS \n
    Autor: Michael Talaga

    :param snake: This is the snake object which will be moving around on the screen. The user will be able to move this with keys.
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
        screen.fill(get_color("green"))
        snake.render(screen)
        food.render(screen, get_color("red"))
        borderCollide = snake.update((display_width, display_height), food)
        if (borderCollide == True): #Border collision check
            # exit = True
            return snake.size
        # display score #MT Made snake size for now
        show_score(snake.size, get_color("blue"), 'times new roman', 20)
        pygame.display.update()
        clock.tick(pace)

def main():
    '''
    Main file to run the game and exit the system when it is finished. \n
    Autor: Michael Talaga

    '''
    # final_score =
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
