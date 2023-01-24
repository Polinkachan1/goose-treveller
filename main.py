from pygame import *
import sys
import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

width = 800
height = 665
display = (width, height)
pygame.init()
screen = pygame.display.set_mode(display)
pygame.display.set_caption('Goose-adventurer')

background_1 = load_image('simple_blue_fon.jpg')
background_2 = load_image('fon.png')
# background_3 = load_image('desert_broun.jpg')

clock = pygame.time.Clock()
# all for start_screen
color = (255, 255, 255)
color_light = (127, 197, 234)
color_dark = (105, 180, 220)
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
level_counter = 0


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def set_level(level_counter):
    global bg, level, COINCOUNT, lives_left

    monster_group.empty()
    coin_group.empty()
    door_group.empty()
    all_sprites.empty()

    if level_counter == 0:
        bg = background_2
        level = level_1
        COINCOUNT = 0
        lives_left = 3

    elif level_counter == 1:
        bg = background_1
        level = level_2
        COINCOUNT = 0
        lives_left = 3

    create_level_sprites()


def create_level_sprites():
    global player, left, right, up, is_extra_run, platforms
    left = right = up = is_extra_run = False  # по умолчанию — стоим
    x = y = 0  # координаты
    platforms = []
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y, 'block.png')
                all_sprites.add(pf)
                platforms.append(pf)
            elif col == ".":
                pf = Platform(x, y, 'iron_block.png')
                all_sprites.add(pf)
                platforms.append(pf)
            elif col == '$':
                cn = Coin(x, y, 'coin.png')
                all_sprites.add(cn)
                coin_group.add(cn)
            elif col == 'P':
                pl = Platform(x, y, 'wood_block.png')
                all_sprites.add(pl)
                platforms.append(pl)
            elif col == '*':
                dan = Danger(x, y, 'lovushka.png')
                all_sprites.add(dan)
                platforms.append(dan)
            elif col == '!':
                next_l = End_portal(x, y, 'door.png')
                all_sprites.add(next_l)
                door_group.add(next_l)
            elif col == 'M':
                mon = Monster(x, y, 'monster.png')
                all_sprites.add(mon)
                monster_group.add(mon)
            elif col == 'G':
                player = Player(x, y)
                all_sprites.add(player)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля


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
                    print(level_counter)
                    return

                elif width / 2.5 <= mouse[0] <= width / 2.5 + 200 and height / 3.5 <= mouse[1] <= height / 3.5 + 60:
                    level_counter = 0
                    set_level(level_counter)
                    print(level_counter)
                    return

        mouse = pygame.mouse.get_pos()
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
        screen.blit(text_lev_1, (width / 2.5 + 20, height / 3.5 + 10))  # first button
        screen.blit(text_lev_2, (width / 2.5 + 20, height / 2.5 + 10))  # second button
        pygame.display.update()


def start_screen():
    global level_counter
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
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

        mouse = pygame.mouse.get_pos()
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    level_counter = 0
                    set_level(level_counter)
                    main_p.set_volume(0)
                    lose.play()
                    return start_screen()
                    main_p.set_volume(50)

        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        screen.blit(restart_text, (width / 2.5 + 10, height / 1.1))
        draw_text('score: ' + str(COINCOUNT), smallfont, 'white', width / 2.5, height / 1.5)
        pygame.display.update()


def win_level():
    global level_counter
    fon = pygame.transform.scale(load_image('win_screen.png'), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    if level_counter == 0:
                        level_counter += 1
                        set_level(level_counter)
                        return
                    if level_counter == 1:
                        level_counter = 0
                        set_level(level_counter)
                        return start_screen()
        mouse = pygame.mouse.get_pos()
        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        if level_counter == 1:
            screen.blit(all_win_text, (width / 2.5 + 10, height / 1.1))
        else:
            screen.blit(win_restart_text, (width / 2.5 + 10, height / 1.1))
        draw_text('score: ' + str(COINCOUNT), smallfont, 'white', width / 2.5, height / 1.5)
        pygame.display.update()


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)


MOVE_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.35
WIDTH = 20
HEIGHT = 30
COLOR = "#888888"
COINCOUNT = 0
depth_counter = 0
lives_left = 3
EXTRA_SPEED = 2.5
EXTRA_JUMP_POWER = 5


class Player(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.reset(x, y)

    def move(self, left, right, up, platforms, is_extra_run, frame_delay):
        if left:
            self.image = load_image('gosle.png')
            self.x_speed = -MOVE_SPEED  # Лево = x - n
            if is_extra_run:  # ускорение
                self.x_speed -= EXTRA_SPEED  # ходьба-ускорение

        if right:
            self.image = load_image('gose.png')
            self.x_speed = MOVE_SPEED  # Право = x + n
            if is_extra_run:  # ускорение
                self.x_speed += EXTRA_SPEED  # ходьба-ускорение

        if up:
            if self.onGround:
                self.y_speed -= JUMP_POWER
                if is_extra_run and (left or right):  # ускорение и движение
                    self.y_speed -= EXTRA_JUMP_POWER  # прыжок с ускорением

        if not (left or right) and not is_extra_run:  # стоим
            self.x_speed = 0
        if not self.onGround:
            self.y_speed += GRAVITY

        self.onGround = False
        self.rect.y += self.y_speed  # переносим своё положение на y_speed
        self.collide(0, self.y_speed, platforms)
        self.rect.x += self.x_speed  # переносим свои положение на x_speed
        self.collide(self.x_speed, 0, platforms)

    def collide(self, x_speed, y_speed, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, Danger) or isinstance(p, Monster):  # если пересекаемый блок - Danger или Monster
                    self.death()
                elif isinstance(p, End_portal):
                    self.teleport(self.startX, self.startY)

                else:
                    if x_speed > 0:
                        self.rect.right = p.rect.left
                    elif x_speed < 0:
                        self.rect.left = p.rect.right
                    elif y_speed > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.y_speed = 0
                    elif y_speed < 0:
                        self.rect.top = p.rect.bottom
                        self.y_speed = 0

    def death(self):
        global lives_left
        time.wait(500)
        self.teleport(self.startX, self.startY)
        lives_left -= 1

    def teleport(self, moveX, moveY):
        self.rect.x = moveX
        self.rect.y = moveY

    def reset(self, x, y):
        self.x_speed = 0
        self.startX = x
        self.y_speed = 0
        self.onGround = False
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image = load_image('gose.png')
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))


class Platform(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__(all_sprites)
        self.image = load_image(image)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *groups):
        super().__init__(*groups)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, animation_tick=False):
        if not animation_tick:
            return
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


COIN_ANIMATION_EVENT = pygame.USEREVENT + 1


class Coin(AnimatedSprite):
    def __init__(self, x: int, y: int, image_name):
        image = load_image(image_name)
        super().__init__(image, 6, 1, x, y, all_sprites)


class Danger(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = load_image(image)
        self.image.set_colorkey(Color(COLOR))
        self.rect = self.image.get_rect().move(x, y)
        self.startX = x
        self.startY = y


class Monster(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__(all_sprites)
        self.image = load_image(image)
        self.image.set_colorkey(Color(COLOR))
        self.rect = self.image.get_rect().move(x, y)
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class End_portal(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = load_image(image)
        self.image.set_colorkey(Color(COLOR))
        self.rect = self.image.get_rect().move(x, y)


left = right = up = is_extra_run = False

all_sprites = pygame.sprite.Group()  # Все объекты, кроме монет
coin_group = pygame.sprite.Group()  # монеты
door_group = pygame.sprite.Group()  # портал
monster_group = pygame.sprite.Group()  # монстр
platforms = []

main_p = pygame.mixer.Sound('game_music.mp3')
main_p.play(-1)

level_1 = ["-                                                                   -",
           "-                                                                   -",
           "-                                                                   -",
           "-                                                                   -",
           "-       $$                   $        *                             -",
           "-      ----         --      ---             ---      $$             -",
           "-                             --                   ----             -",
           "-                       *                          M                -",
           "-$                M                      $      ------              -",
           "--       $      -----                  ----                         -",
           "-       $ $   *                           *                         -",
           "-       ---                      --                            $    -",
           "- $                         M                              M  --    -",
           "-                $        ----                 $ $        --- -     -",
           "----                    ----                           -      -     -",
           "-            -------                         --------         -  *  -",
           "-          --                             **                  -  !  -",
           "-        --                             ------                ---P---",
           "-                     *                                          $ $-",
           "-G     !             -             $$                            $ $ -",
           "---------------------------------------------------------------------"]

level_2 = [".                                                                   .",
           ".                                                                   .",
           ".          ...                          M                  $ $      .",
           ".   $$                               ......           *   ....      .",
           ".   $$            *    $ $       *                $   ..            .",
           ".  ...                ....     ...               $ $                .",
           ".                                                ...                .",
           ".$                                                                  .",
           "..          **                 $$                                   .",
           ".                            ......                                 .",
           ".                                                                   .",
           ".      $                              ...                           .",
           ".     ...         M          *                                    **.",
           ".               .....                                               .",
           ".          ...                       M          **             !    .",
           ".   ........                      ........                 ..........",
           ".  .                             ... $ ....                     $ $ .",
           ".                            ....... $ .....                   $ $ $.",
           ".            **                  ...   ......        ..        ......",
           ".G     ! .      $                       $.....      ....      .......",
           "....................................................................."]

start_screen()
camera = Camera()
FPS = 60
bg = background_1
is_running = True
frame_delay = 0
pygame.time.set_timer(COIN_ANIMATION_EVENT, 200)
flPause = False
vol = 0.1
coin = pygame.mixer.Sound('data/catch_coin.mp3')
lose = pygame.mixer.Sound('lose.mp3')
set_level(level_counter)

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
        game_over()


    player.move(left, right, up, platforms, is_extra_run, frame_delay)
    if lives_left == 0:
        game_over()

        lives_left = 3
    if lives_left != 0 and pygame.sprite.spritecollide(player, door_group, True):
        win_level()


    screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
    all_sprites.draw(screen)
    draw_text('score: ' + str(COINCOUNT), smallfont, 'white', PLATFORM_WIDTH, 20)
    draw_text('lives_left: ' + str(lives_left), smallfont, 'white', PLATFORM_WIDTH, 60)

    pygame.display.update()  # обновление и вывод всех изменений на экран
    frame_delay = clock.tick(FPS) / 1000
pygame.quit()