from pygame import *
import sys
import os
import pyganim
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

width = 800  # Ширина создаваемого окна
height = 640  # Высота
display = (width, height)  # Группируем ширину и высоту в одну переменную
pygame.init()  # Инициация PyGame, обязательная строчка
screen = pygame.display.set_mode(display)
pygame.display.set_caption('Goose-adventurer')

background_1 = load_image('simple_blue_fon.jpg')
background_2 = load_image('forest_with_deers.jpg')
background_3 = load_image('desert_broun.jpg')

goose_animation = [pygame.image.load("data/goose_go_left_1.png"), pygame.image.load("data/goose_go_left4.png"),
                   pygame.image.load("data/goose_left_3.png"), pygame.image.load("data/goose_jump.png"),
                   pygame.image.load("data/goose_jumps_left.png")]
coin_animation = [pygame.image.load('data/coin1.png'), pygame.image.load('data/coin2.png'),
                  pygame.image.load('data/coin3.png'), pygame.image.load('data/coin4.png'), pygame.image.load('data/coin5.png')]
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
# texts for change_level
text_lev_1 = smallfont.render('level №1', True, color)
text_lev_2 = smallfont.render('level №2', True, color)
text_lev_3 = smallfont.render('level №3', True, color)
restart_text = smallfont.render('try again', True, color)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def instruction():
    fon = pygame.transform.scale(load_image('instruction.jpg'), (width, height))
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
                    return

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


def start_screen():
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
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
        # updates the frames of the game
        pygame.display.update()


def game_over():
    fon = pygame.transform.scale(load_image('game_over.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
                    return start_screen()
        mouse = pygame.mouse.get_pos()
        if width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.1 <= mouse[1] <= height / 1.1 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.1, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.5, height / 1.1, 140, 40])
        screen.blit(restart_text, (width / 2.5 + 10, height / 1.1))
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
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
WIDTH = 20
HEIGHT = 30
COLOR = "#888888"
COINCOUNT = 0
levelcounter = 0
depth_counter = 0
lifes_left = 3
EXTRA_SPEED = 2.5
EXTRA_JUMP_POWER = 5

def sprite_goose():
    value = 0
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        clock.tick(3)

        if value >= len(goose_animation):
            value = 0
        image = goose_animation[value]
        x = 150
        if value == 0:
            y = 200
        else:
            y = 265

        screen.blit(image, (x, y))
        pygame.display.update()
        screen.blit(background_1, (0, 0))
        value += 1


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x_speed = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х
        self.y_speed = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        # self.image = sprite_goose()
        self.image = load_image('gose.png')
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))

    def update(self, left, right, up, platforms, is_extra_run):
        if left:
            self.x_speed = -MOVE_SPEED  # Лево = x - n
            if is_extra_run:  #ускорение
                self.x_speed -= EXTRA_SPEED # ходьба-ускорение работает

        if right:
            self.x_speed = MOVE_SPEED  # Право = x + n
            if is_extra_run:  #ускорение
                self.x_speed += EXTRA_SPEED # ходьба-ускорение работает

        if up:
            if self.onGround:
                self.y_speed -= JUMP_POWER
                if is_extra_run and (left or right):  # есть ускорение и движение
                    self.y_speed -= EXTRA_JUMP_POWER # то прыжок с ускорением

        if not (left or right):  # стоим, когда нет указаний идти
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
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, Danger) or isinstance(p, Monster):  # если пересакаемый блок - Danger или Monster
                    self.depth()
                # elif isinstance(p, Coin):
                # self.get_profit()
                elif isinstance(p, End_portal):
                    self.teleport(self.startX, self.startY)

                else:
                    if x_speed > 0:  # если движется вправо
                        self.rect.right = p.rect.left  # то не движется вправо

                    if x_speed < 0:  # если движется влево
                        self.rect.left = p.rect.right  # то не движется влево

                    if y_speed > 0:  # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        self.y_speed = 0  # и энергия падения пропадает

                    if y_speed < 0:  # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.y_speed = 0

    def depth(self):
        global lifes_left
        time.wait(500)
        self.teleport(self.startX, self.startY)
        lifes_left -= 1


    def teleport(self, moveX, moveY):
        self.rect.x = moveX
        self.rect.y = moveY


class Platform(sprite.Sprite):
    def __init__(self, x, y, image):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = load_image(image)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)



class Coin(sprite.Sprite):
    def __init__(self, x, y, image):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = load_image(image)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.image.set_colorkey(Color(COLOR))
        self.x = x
        self.y = y

    def update(self):
        pass


class Danger(sprite.Sprite):
    def __init__(self, x, y, image):
        Platform.__init__(self, x, y, image)
        self.image = load_image(image)
        self.image.set_colorkey(Color(COLOR))

    def player_die(self):
        time.delay(50)
        self.teleport(self.startX, self.startY)

    def teleport(self, moveX, moveY):
        self.rect.x = moveX
        self.rect.y = moveY




class Monster(sprite.Sprite):
    def __init__(self, x, y, image):
        Platform.__init__(self, x, y, image)
        self.image = load_image(image)
        self.image.set_colorkey(Color(COLOR))

    def player_die(self):
        pass


class End_portal(sprite.Sprite):
    def __init__(self, x, y, image):
        Platform.__init__(self, x, y, image)
        self.image = load_image(image)
        self.image.set_colorkey(Color(COLOR))

    def next_level(self):
        global levelcounter
        levelcounter += 1



left = right = up = is_extra_run = False  # по умолчанию — стоим

all_sprites = pygame.sprite.Group()  # Все объекты, кроме монет
coin_group = pygame.sprite.Group()  # монеты
platforms = []  # то, во что мы будем врезаться или опираться

level_1 = ["-                                 ",
           "-            --                   ",
           "-                                 ",
           "-                                 ",
           "-                   ----     ---  ",
           "-                                 ",
           "-                                 ",
           "-            *                    ",
           "-                            ---  ",
           "-                                 ",
           "-                                 ",
           "-     ---        !          *     ",
           "-       $ $     ---               ",
           "-           ----                  ",
           "-   --------                      ",
           "-  -                      -  !    ",
           "-                          ------ ",
           "-           ***                   ",
           "-G        P                      ",
           "----------PP----------------------"]

x = y = 0  # координаты
for row in level_1:  # вся строка
    for col in row:  # каждый символ
        if col == "-":
            pf = Platform(x, y, 'block.png')
            all_sprites.add(pf)
            platforms.append(pf)
        if col == '$':
            cn = Coin(x, y, 'coin0.png')
            all_sprites.add(cn)
            coin_group.add(cn)
        if col == 'P':
            pl = Platform(x, y, 'wood_block.png')
            all_sprites.add(pl)
            platforms.append(pl)
        if col == '*':
            dan = Danger(x, y, 'lovushka.png')
            all_sprites.add(dan)
            platforms.append(dan)
        if col == '!':
            next_l = End_portal(x, y, 'door.png')
            all_sprites.add(next_l)
            platforms.append(next_l)
        if col == 'G':
            player = Player(x, y)
            all_sprites.add(player)

        x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
    y += PLATFORM_HEIGHT  # то же самое и с высотой
    x = 0  # на каждой новой строчке начинаем с нуля

start_screen()
camera = Camera()
FPS = 60
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


    screen.blit(background_1, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    # проверка того, была ли собрана монетка
    if pygame.sprite.spritecollide(player, coin_group, True):
        COINCOUNT += 1

    draw_text('score: ' + str(COINCOUNT), smallfont, 'white', PLATFORM_WIDTH, 20)
    draw_text('lifes_left: ' + str(lifes_left), smallfont, 'white', PLATFORM_WIDTH, 40)

    all_sprites.draw(screen)
    coin_group.draw(screen)
    player.update(left, right, up, platforms, is_extra_run)
    if lifes_left == 0:
        game_over()
    pygame.display.update()  # обновление и вывод всех изменений на экран
    clock.tick(FPS)
pygame.quit()
