from sprites import *
from configer import *
from pygame import *
from player import Player


def set_level(level_counter) -> Player:
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

    return create_level_sprites()


def create_level_sprites() -> Player:
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

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0
    return player


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__(all_sprites)
        self.image = load_image(image)
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


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
           "-G                  -             $$                            $ $ -",
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
           ".G       .      $                       $.....      ....      .......",
           "....................................................................."]
