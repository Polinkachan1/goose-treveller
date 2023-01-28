from configer import *
from pygame import *
from creator_of_level import set_level
from texts import show_texts


def instruction():
    fon = pygame.transform.scale(load_image('instruction.png'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 1.2 <= mouse[0] <= width / 1.2 + 140 and height / 24 <= mouse[1] <= height / 24 + 40:
                    return start_screen()
        mouse = pygame.mouse.get_pos()

        if width / 1.2 <= mouse[0] <= width / 1.2 + 140 and height / 24 <= mouse[1] <= height / 24 + 40:
            pygame.draw.rect(screen, color_light, [width / 1.2, height / 24, 150, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 1.2, height / 24, 150, 40])
        text_1, text_2, text_3, text_lev_2, text_lev_1, restart_text, win_restart_text, \
        all_win_text, back_button, smallfont = show_texts()

        screen.blit(back_button, (width / 1.2 + 5, height / 24))
        pygame.display.update()


def wrong_message():
    fon = pygame.transform.scale(load_image('wrong_message.png'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if width / 1.2 <= mouse[0] <= width / 1.2 + 140 and height / 24 <= mouse[1] <= height / 24 + 40:
                return start_screen()

        mouse = pygame.mouse.get_pos()

        if width / 1.2 <= mouse[0] <= width / 1.2 + 140 and height / 24 <= mouse[1] <= height / 24 + 40:
            pygame.draw.rect(screen, color_light, [width / 1.2, height / 24, 150, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 1.2, height / 24, 150, 40])

        back_button, smallfont = show_texts()
        screen.blit(back_button, (width / 1.2 + 5, height / 24))
        pygame.display.update()


def change_level():
    global level_counter
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
                    level_counter = 1
                    set_level(level_counter)
                    return

                elif width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 3.5 <= mouse[1] <= height / 3.5 + 60:
                    level_counter = 0
                    set_level(level_counter)
                    return

        mouse = pygame.mouse.get_pos()
        # second_button Instruction
        if width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 3.5 <= mouse[1] <= height / 3.5 + 60:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 3.5, 200, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 3.5, 200, 60])

        # third-button Choose level
        if width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 2 <= mouse[1] <= height / 2 + 60:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 2, 200, 60])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 2, 200, 60])
        # superimposing the text onto our button
        text_1, text_2, text_3, text_lev_2, text_lev_1, restart_text, win_restart_text, \
        all_win_text, back_button, smallfont = show_texts()
        screen.blit(text_lev_1, (width / 2.5 + 20, height / 3.5 + 10))  # first button
        screen.blit(text_lev_2, (width / 2.5 + 20, height / 2 + 10))  # second button
        pygame.display.update()


def start_screen():
    global level_counter
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    level_counter = 0
                    set_level(level_counter)
                    return
                elif width / 11 <= mouse[0] <= width / 11 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    instruction()

                elif width / 1.5 <= mouse[0] <= width / 1.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    return change_level()

        # if mouse is hovered on a button it changes to lighter shade
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
        text_1, text_2, text_3, text_lev_2, text_lev_1, restart_text, win_restart_text, \
        all_win_text, back_button, smallfont = show_texts()
        screen.blit(text_1, (width / 2.5 + 40, height / 1.1))  # first button
        screen.blit(text_2, (width / 11 + 10, height / 1.1))  # second button
        screen.blit(text_3, (width / 1.5 + 2, height / 1.1))  # third button
        pygame.display.update()


def game_over():
    global level_counter
    fon = pygame.transform.scale(load_image('game_over.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        mouse = pygame.mouse.get_pos()
        pygame.mixer.music.pause()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    level_counter = 0
                    set_level(level_counter)
                    pygame.mixer.music.play()
                    return start_screen()

        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        text_1, text_2, text_3, text_lev_2, text_lev_1, restart_text, win_restart_text, \
            all_win_text, back_button, smallfont = show_texts()
        screen.blit(restart_text, (width / 2.5 + 5, height / 1.1))
        draw_text('score: ' + str(COINCOUNT), smallfont, 'white', width / 2.5, height / 1.5)
        with open("scores.txt", 'w', encoding='utf-8') as f:
            f.write(str(COINCOUNT))
        pygame.display.update()


def win_level():
    global level_counter
    fon = pygame.transform.scale(load_image('win_screen.png'), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        mouse = pygame.mouse.get_pos()
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    pygame.mixer.music.play()
                    if level_counter == 0:
                        level_counter += 1
                        set_level(level_counter)
                        return
                    if level_counter == 1:
                        level_counter = 0
                        set_level(level_counter)
                        return wrong_message()

        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        if level_counter == 1:
            screen.blit(all_win_text, (width / 2.5 + 5, height / 1.1))
        else:
            screen.blit(win_restart_text, (width / 2.5 + 5, height / 1.1))
        draw_text('score: ' + str(COINCOUNT), smallfont, 'white', width / 2.5, height / 1.5)

        pygame.display.update()
