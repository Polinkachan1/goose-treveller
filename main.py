import pygame
import os
import sys

pygame.init()

player = None
step = 10
FPS = 60
width = 1000
height = 800
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

class Button:
    pass

def start_screen():
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
             event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


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
