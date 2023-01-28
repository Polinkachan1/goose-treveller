import pygame

from load_image import load_image


width = 800
height = 665
display = (width, height)

screen = pygame.display.set_mode(display)
pygame.display.set_caption('Goose-adventurer')

MOVE_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.35
WIDTH = 20
HEIGHT = 30
COLOR = "#888888"
depth_counter = 0
lives_left = 3
EXTRA_SPEED = 2.5
EXTRA_JUMP_POWER = 5

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

background_1 = load_image('simple_blue_fon.jpg')
background_2 = load_image('fon.png')

clock = pygame.time.Clock()
# all for start_screen
color = (255, 255, 255)
color_light = (127, 197, 234)
color_dark = (105, 180, 220)
level_counter = 0
left = right = up = is_extra_run = False


