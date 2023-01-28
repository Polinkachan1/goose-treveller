from configer import *
from pygame import *
from creator_of_level import *



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
