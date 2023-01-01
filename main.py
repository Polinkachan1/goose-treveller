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

guess = None

step = 10
FPS = 60
width = 1000
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
# texts for start_screen()
text_1 = smallfont.render('Start', True, color)
text_2 = smallfont.render('Instruction', True, color)
text_3 = smallfont.render('Choose level', True, color)

back_button = smallfont.render('--back->', True, color)
# texts for change_level
text_lev_1 = smallfont.render('level №1', True, color)
text_lev_2 = smallfont.render('level №2', True, color)
text_lev_3 = smallfont.render('level №3', True, color)


def instruction():
    fon = pygame.transform.scale(load_image('instruction.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 1.2 <= mouse[0] <= width / 1.2 + 140 and height / 24 <= mouse[1] <= height / 24 + 40:
                    start_screen()

        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 1.2 <= mouse[0] <= width / 1.2 + 140 and height / 24 <= mouse[1] <= height / 24 + 40:
            pygame.draw.rect(screen, color_light, [width / 1.2, height / 24, 150, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 1.2, height / 24, 150, 40])
        screen.blit(back_button, (width / 1.2 + 5, height / 24))

        pygame.display.update()


def wrong_message():
    fon = pygame.transform.scale(load_image('wrong_message.png'), (width, height))
    screen.blit(fon, (0, 0))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        pygame.display.update()


def change_level():
    fon = pygame.transform.scale(load_image('picker_level.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 2 <= mouse[1] <= height / 2 + 60:
                    # need to add first level
                    return wrong_message()
                elif width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 3.5 <= mouse[1] <= height / 3.5 + 60:
                    #  need to add second level
                    return wrong_message()
                elif width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 2.5 <= mouse[1] <= height / 2.5 + 60:
                    #  need to add third level
                    return wrong_message()

        mouse = pygame.mouse.get_pos()
        if width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 2 <= mouse[1] <= height / 2 + 60:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 2, 200, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 2, 200, 60])

        # second_button Instruction
        if width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 3.5 <= mouse[1] <= height / 3.5 + 60:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 3.5, 200, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 3.5, 200, 60])

        # third-button Choose level
        if width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 2.5 <= mouse[1] <= height / 2.5 + 60:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 2.5, 200, 60])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 2.5, 200, 60])
        # superimposing the text onto our button
        screen.blit(text_lev_3, (width / 2.5 + 20, height / 2 + 10))  # third button
        screen.blit(text_lev_1, (width / 2.5 + 20, height / 3.5 + 10))  # first button
        screen.blit(text_lev_2, (width / 2.5 + 20, height / 2.5 + 10))  # second button
        pygame.display.update()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None


class Guess(Sprite):
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
                    return change_level()
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
            guess.rect.top += step
        if pressed_keys[pygame.K_UP]:
            guess.rect.top -= step
        if pressed_keys[pygame.K_RIGHT]:
            guess.rect.left += step
        if pressed_keys[pygame.K_LEFT]:
            guess.rect.left -= step

    background_color = pygame.Color('white')
    screen.fill(background_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
