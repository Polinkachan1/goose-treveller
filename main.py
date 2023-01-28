from camera import Camera
from creator_of_level import (
    set_level,
    COIN_ANIMATION_EVENT,
)
from menu import (
    start_screen,
    win_level,
    game_over,
)
from player import Player
from configer import *
from pygame import *
from sounds import *
from texts import *
from sprites import *
import sys
import os
import pygame


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))




def main():
    pygame.init()
    load_music()
    show_texts()
    start_screen()
    camera = Camera()
    FPS = 60
    COINCOUNT = 0
    bg = background_1
    frame_delay = 0
    pygame.time.set_timer(COIN_ANIMATION_EVENT, 200)
    flPause = False

    player = set_level(level_counter)
    coin, lose, winner = load_music()
    text_1, text_2, text_3, text_lev_2, text_lev_1, restart_text, win_restart_text, \
    all_win_text, back_button, smallfont = show_texts()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYUP and event.key == K_SPACE:
                is_extra_run = False
            if event.type == KEYDOWN and event.key == K_SPACE:
                is_extra_run = True
            if event.type == COIN_ANIMATION_EVENT:
                coin_group.update(animation_tick=True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        all_sprites.update()
        camera.update(player)
        monster_group.update()
        for sprite in all_sprites:
            camera.apply(sprite)
        # проверка того, была ли собрана монетка
        if pygame.sprite.spritecollide(player, coin_group, True):
            coin.play()
            COINCOUNT += 1
        if pygame.sprite.spritecollide(player, monster_group, True):
            lose.play()
            game_over()

        player.move(left, right, up, platforms, is_extra_run, frame_delay)
        if lives_left == 0:
            lose.play()
            game_over()

            lives_left = 3
        if lives_left != 0 and pygame.sprite.spritecollide(player, door_group, True):
            winner.play()
            with open("scorer.txt", 'w', encoding='utf-8') as f:
                file = f.write(str(COINCOUNT))
                print(COINCOUNT)
            win_level()

        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)
        draw_text('score: ' + str(COINCOUNT), smallfont, 'white', PLATFORM_WIDTH, 20)
        draw_text('lives_left: ' + str(lives_left), smallfont, 'white', PLATFORM_WIDTH, 60)

        pygame.display.update()
        frame_delay = clock.tick(FPS) / 1000
    pygame.quit()

main()