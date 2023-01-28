import pygame
from configer import color


def show_texts():
    smallfont = pygame.font.SysFont('Corbel', 35)
    # texts for start_screen()
    text_1 = smallfont.render('Start', True, color)
    text_2 = smallfont.render('Instruction', True, color)
    text_3 = smallfont.render('Choose level', True, color)
    back_button = smallfont.render('--back->', True, color)
    text_lev_1 = smallfont.render('level №1', True, color)
    text_lev_2 = smallfont.render('level №2', True, color)
    restart_text = smallfont.render('try again', True, color)
    win_restart_text = smallfont.render('next level', True, color)
    all_win_text = smallfont.render('menu', True, color)
    return text_1, text_2, text_3, text_lev_2, text_lev_1, restart_text, win_restart_text,\
           all_win_text, back_button, smallfont
