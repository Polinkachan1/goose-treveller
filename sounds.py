import pygame


def load_music():
    coin = pygame.mixer.Sound('music/catch_coin.mp3')
    lose = pygame.mixer.Sound('music/lose.mp3')
    winner = pygame.mixer.Sound('music/winner.mp3')
    pygame.mixer.music.load('music/game_music.mp3')
    pygame.mixer.music.play(-1)
    return coin, lose, winner
