import pygame
import os
import sys
from pygame import (
    Color,
)


def load_image(name: str):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image


pygame.init()

player = None

step = 10
FPS = 60
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Goose-adventurer")

screen = pygame.display.set_mode((width, height))
all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

player_image = load_image('goose_sprite.jpg')

clock = pygame.time.Clock()

color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)

text_1 = smallfont.render('Start', True, color)
text_2 = smallfont.render('Instruction', True, color)
text_3 = smallfont.render('Choose level', True, color)


def instruction():
    fon = pygame.transform.scale(load_image('instruction.jpg'), (width, height))
    screen.blit(fon, (0, 0))


class Choose_level:
    pass


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None


class Player(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = player_image
        ...


def start_screen():
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    return
                elif width / 11 <= mouse[0] <= width / 11 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    instruction()

                elif width / 1.5 <= mouse[0] <= width / 1.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    Choose_level()

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        # second_button Instruction
        if width / 11 <= mouse[0] <= width / 11 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 11, height / 1.1, 180, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 11, height / 1.1, 180, 40])
        # third-button Choose level
        if width / 1.5 <= mouse[0] <= width / 1.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 1.5, height / 1.1, 180, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 1.5, height / 1.1, 180, 40])
        # superimposing the text onto our button
        screen.blit(text_1, (width / 2.5 + 40, height / 1.1))  # first button
        screen.blit(text_2, (width / 11 + 10, height / 1.1))  # second button
        screen.blit(text_3, (width / 1.5 + 5, height / 1.1))  # third button
        # updates the frames of the game
        pygame.display.update()


start_screen()

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        keys = pygame.key.get_pressed()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            player.rect.top += step
        if pressed_keys[pygame.K_UP]:
            player.rect.top -= step
        if pressed_keys[pygame.K_RIGHT]:
            player.rect.left += step
        if pressed_keys[pygame.K_LEFT]:
            player.rect.left -= step

    background_color = pygame.Color('white')
    screen.fill(background_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
