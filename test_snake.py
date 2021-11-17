import unittest
import pygame


'''
unit test class
date: nov 8 2021
'''

curr_game_size = (425, 425)
rect_verticies = [(25,25),(400,25),(400,400),(25,400)]
border_color = "yellow"
play_area_color = "green"
brdr_pt_left = (10, 213)
brdr_pt_right = (410, 213)
brdr_pt_top = (213, 10)
brdr_pt_bot = (213, 410)
gameplay_pt = (213, 212)
'''
:meta private:
'''

def get_color(color_string):
    # central place to store all color values
    '''
    pass name of color, return RGB value for color

    :param color_string: name of color
    :type color_string: String
    :return _: The RGB value of the passed color
    :rtype: Tuple (red, green, blue)
    '''
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

def create_key_mock(pressed_key):
    '''
    create mock key press for testing
    '''
    def helper():
        tmp = [0] * 300
        tmp[pressed_key] = 1
        return tmp
    return helper


class TestSnake(unittest.TestCase):
    '''
    Test suite for Snake class

    Example::

        python3 test_snake.py

    '''
    def test_border(self):
        '''
        tests the border is drawn and is the correct color
        '''
        # draw a surface
        test_surface = pygame.Surface(curr_game_size)
        # fill surface with border color
        test_surface.fill(get_color(border_color))
        # draw play area on surface
        pygame.draw.polygon(test_surface, get_color(play_area_color), rect_verticies)
        # test left, right, top, bottom is equal to some color
        self.assertEqual(test_surface.get_at(brdr_pt_left), get_color(border_color))
        self.assertEqual(test_surface.get_at(brdr_pt_right), get_color(border_color))
        self.assertEqual(test_surface.get_at(brdr_pt_top), get_color(border_color))
        self.assertEqual(test_surface.get_at(brdr_pt_bot), get_color(border_color))
        # save file for ref
        pygame.image.save(test_surface, "./test_output/test_border_image.png")

    def test_game_area(self):
        '''
        tests the border is drawn and is the correct color
        '''
        # draw a surface
        test_surface = pygame.Surface(curr_game_size)
        # fill surface with border color
        test_surface.fill(get_color(border_color))
        # draw play area on surface
        pygame.draw.polygon(test_surface, get_color(play_area_color), rect_verticies)
        # test left, right, top, bottom is equal to some color
        self.assertEqual(test_surface.get_at(gameplay_pt), get_color(play_area_color))
        # save file for ref
        pygame.image.save(test_surface, "./test_output/test_game_area_image.png")

    def test_food(self):
        '''
        tests food is renderded at some coord
        '''
        # draw the board and food
        test_surface = pygame.Surface(curr_game_size)
        test_surface.fill(get_color(border_color))
        pygame.draw.polygon(test_surface, get_color(play_area_color), rect_verticies)
        # TODO: finish test
        # test that the food is in the correct coords
        # self.assertEqual(<the object in the square drawn>, <what should be drawn>)
        # save file for ref
        pygame.image.save(test_surface, "./test_output/test_food_image.png")

    def test_keyboard(self):
        '''
        test input from the keyboard, if no keys pressed, pass
        '''
        # need video init for test
        pygame.init()
        key_state = pygame.key.get_pressed()
        self.assertEqual(key_state[pygame.K_RIGHT], 0)
        self.assertEqual(key_state[pygame.K_LEFT], 0)
        self.assertEqual(key_state[pygame.K_UP], 0)
        self.assertEqual(key_state[pygame.K_DOWN], 0)

    def test_example(self):
        '''
        example test, link to citation in README.html
        :meta private:
        '''
        surf = pygame.Surface((320, 200))
        surf.fill(get_color("black"))

        # The area the ellipse is contained in, is held by rect.
        #
        # 10 pixels from the left,
        # 11 pixels from the top.
        # 225 pixels wide.
        # 95 pixels high.
        rect = (10, 11, 225, 95)
        pygame.draw.ellipse(surf, get_color("red"), rect)

        # To see what is drawn you can save the image.
        # pygame.image.save(surf, "test_draw2_image.png")

        # The ellipse should not draw over the black in the top left spot.
        self.assertEqual(surf.get_at((0, 0)), get_color("black"))

        # It should be red in the middle of the ellipse.
        middle_of_ellipse = (125, 55)
        self.assertEqual(surf.get_at(middle_of_ellipse), get_color("red"))








































if __name__ == '__main__':
    unittest.main()
