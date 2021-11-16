import pygame
#import pygame_menu
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
by: Morgan Marino, Michael Talaga, AMA, Divya Shakamuri
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
        case "darkGreen":
            return (0,200,0)
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

def chooseDifficulty(snake):
    '''
    Option after starting to select difficulty, changes things like game speed/speed over time
    Author: Michael Talaga
    '''

    difficultyText = "Choose Difficulty"
    font = pygame.font.SysFont('times new roman', 25)
    smallFont = pygame.font.SysFont('times new roman', 20)
    difficulty = ""
    while(1):
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False
            if pressed[pygame.K_RETURN]:
                match difficulty:
                    case "REGULAR":
                        return "REGULAR"
                    case "HARD":
                        return "HARD"
                    case _:
                        continue
            if pressed[pygame.K_LEFT]:
                difficulty = "REGULAR"
            elif pressed[pygame.K_RIGHT]:
                difficulty = "HARD"

        screen.fill(get_color("white"))
        pygame.draw.rect(screen, get_color("darkGreen"), pygame.Rect(30, 30, (display_height - 60), display_width - 60))
        difficultyRender = font.render(difficultyText, False, get_color("yellow"))
        screen.blit(difficultyRender, ((display_width / 4), (display_height / 5)))
        match difficulty:
            case "REGULAR":
                hardRender = smallFont.render("HARD", False, get_color("white"))
                regRender = font.render("REGULAR", False, get_color("yellow"))
            case "HARD":
                hardRender = font.render("HARD", False, get_color("yellow"))
                regRender = smallFont.render("REGULAR", False, get_color("white"))
            case _:
                regRender = smallFont.render("REGULAR", False, get_color("white"))
                hardRender = smallFont.render("HARD", False, get_color("white"))

        screen.blit(hardRender, ((display_width / 1.5), (display_height / 3)))
        screen.blit(regRender, ((display_width / 4.5), (display_height / 3)))
        pygame.display.update()
        clock.tick(pace)

def menu():
    '''
    Menu to start the game or quit
    Author: Michael Talaga
    :return: returns true if the game will start or false to quit.
    '''
    title = "Snake Game by Group 3"
    instruction = "Please use arrow keys to select"
    font = pygame.font.SysFont('times new roman', 30)
    selectedFont = pygame.font.SysFont('times new roman', 25)
    smallFont = pygame.font.SysFont('times new roman', 20)
    choice = ""
    while(1):
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False
            if pressed[pygame.K_RETURN]:
                match choice:
                    case "QUIT":
                        return False
                    case "START":
                        return True
                    case _:
                        continue
            if pressed[pygame.K_DOWN]:
                choice = "QUIT"
            elif pressed[pygame.K_UP]:
                choice = "START"
        screen.fill(get_color("white"))
        pygame.draw.rect(screen, get_color("darkGreen"), pygame.Rect(30, 30, (display_height - 60), display_width - 60))

        #Create and blit title to screen
        titleRender = font.render(title, False, get_color("yellow"))
        screen.blit(titleRender, ((display_width / 6), (display_height / 5)))
        instructionRender = smallFont.render(instruction, False, get_color("white"))
        screen.blit(instructionRender, ((display_width / 4.5), (display_height / 3)))
        match choice:
            case "QUIT":
                startRender = smallFont.render("START", False, get_color("white"))
                quitRender = selectedFont.render("QUIT", False, get_color("yellow"))
            case "START":
                startRender = selectedFont.render("START", False, get_color("yellow"))
                quitRender = smallFont.render("QUIT", False, get_color("white"))
            case _:
                quitRender = smallFont.render("QUIT", False, get_color("white"))
                startRender = smallFont.render("START", False, get_color("white"))

        screen.blit(startRender, ((display_width / 2.5), (display_height / 2)))
        screen.blit(quitRender, ((display_width / 2.5), (display_height / 1.5)))
        pygame.display.update()
        clock.tick(pace)


def game(snake, difficulty):
    '''
    Main game loop to play snake game
    Author: Michael Talaga

    :param snake: This is the snake object which will be moving around on the screen. The user will be able to move this with arrow keys or wasd.
    :type snake: Snake, made of, Block
    '''
    exit = False

    #random food placement
    bonus = 0
    score = 0
    xys = []
    foods = []
    for i in range(2):
        x = random.choice(range(25, display_width-25, 25))
        y = random.choice(range(25, display_width-25, 25))
        while (x, y) in xys:
            x = random.choice(range(25, display_width-25, 25))
            y = random.choice(range(25, display_width-25, 25))
        if i == 1:
            foods.append(Food(x, y, True))
        else:
            foods.append(Food(x, y, False))
        xys.append((x, y))

    while not exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                # exit = True
                return snake.size
        screen.fill((0, 100, 0))
        #should we make border so it's easier to know when you're about to lose? -MEM
        # border added -MXO
        #need to fix food spawn so they are within the border -MXO
        if difficulty == "REGULAR":
            gridScreen(25, get_color("green"), get_color("darkGreen"))
        elif (difficulty == "HARD"):
            gridScreen(25, get_color("green"), get_color("green"))
        snake.render(screen)
        for food in foods[:1+bonus]:
            food.render(screen, get_color("red"), Block, snake)
        borderCollide = snake.wall_collision(20,380,20,380)
        #snake.update((display_width, display_height), food)
        bodyCollide, bonus, add = snake.update((display_width, display_height), foods, bonus)
        score += add
        if (borderCollide == True or bodyCollide == True): #Border collision check
            # exit = True
            return score
        # display score #MT Made snake size for now
        show_score(score, get_color("yellow"), 'times new roman', 20)
        pygame.display.update()
        clock.tick(pace)

def main():
    '''
    Main file to run the game and exit the system when it is finished. \n
    Author: Michael Talaga, AMA


    '''


    finished = False
    while not finished:
        snake = Snake(200, 200) #Initializes snake with a starting position (divisible by 5)
        if (not menu()):
            finished = True
            break
        #Choose game difficulty
        difficulty = chooseDifficulty(snake)
        #Run game
        game_over('times new roman', 50, "red", game(snake, difficulty))
    pygame.quit()
    exit()
    #sys.exit()

req_version = (3,10)
curr_version = sys.version_info
if curr_version >= req_version:
    if __name__ == '__main__':
        main()
else:
    # prompt user to update python
    print("Please update your python version to 3.10 or greater")
