import pygame
import os
import sys

pygame.init()



player = None
step = 10
FPS = 60
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Goose-adventurer")
clock = pygame.time.Clock()


def load_image(name: str, color_key: int = None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image


class Instructions:
    pass


class Changing_Fon:
    pass


# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text_1 = smallfont.render('start', True, color)
text_2 = smallfont.render('Instructions', True, color)
text_3 = smallfont.render('Change Fon', True, color)

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
                    Instructions()

                elif width / 1.5 <= mouse[0] <= width / 1.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    Changing_Fon()


        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        # second_button Instructions
        if width / 11 <= mouse[0] <= width / 11 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 11, height / 1.1, 180, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 11, height / 1.1, 180, 40])
        # third-button Change Fon
        if width / 1.5 <= mouse[0] <= width / 1.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 1.5, height / 1.1, 170, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 1.5, height / 1.1, 170, 40])
        # superimposing the text onto our button
        screen.blit(text_1, (width / 2.5 + 40, height / 1.1))  # first button
        screen.blit(text_2, (width / 11 + 10, height / 1.1))  # second button
        screen.blit(text_3, (width / 1.5, height / 1.1))  # third button
        # updates the frames of the game
        pygame.display.update()


start_screen()

is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN]:
            player.rect.top += step
        if pressed_keys[pygame.K_UP]:
            player.rect.top -= step
        if pressed_keys[pygame.K_RIGHT]:
            player.rect.left += step
        if pressed_keys[pygame.K_LEFT]:
            player.rect.left -= step
    background_color = pygame.Color('black')
    screen.fill(background_color)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
