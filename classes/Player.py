from pygame.sprite import Sprite

from classes.AnimatedObject import AnimatedObject
from classes.Bullet import *
from classes.Consts import *
from classes.States import States


class Player(Sprite, AnimatedObject):
    def __init__(self, center, margins_l_t_r_b: tuple[int, int, int, int]):
        Sprite.__init__(self, all_sprites)
        AnimatedObject.__init__(self, state=States.idle, animation_idle=PLAYER_IDLE_ANIMATION, animation_run=PLAYER_RUN_ANIMATION)
        self.all_sprites = all_sprites
        self.margin_left, self.margin_top, self.margin_right, self.margin_bottom = margins_l_t_r_b
        self.frames = []
        self.cut_sheet(pygame.image.load(PLAYER_IMAGE), 1, 6)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()

        self.x = center[0] - self.rect.width // 2
        self.y = center[1] - self.rect.height // 2
        self.hitbox_sprite = Sprite()
        self.hitbox_sprite.parent = self
        self.hitbox_sprite.rect = pygame.Rect(self.x + self.margin_left, self.y + self.margin_top,
                                              self.rect.width - self.margin_left - self.margin_right,
                                              self.rect.height - self.margin_bottom - self.margin_top)


        self.hitbox = self.hitbox_sprite.rect
        self.time_per_shoot = 0
        self.time_per_damage = 0
        self.time_animation = 0

        self.rect.x = self.x
        self.rect.y = self.y
        self.hp = PLAYER_HP
        self.max_hp = PLAYER_HP
        self.speed = PLAYER_SPEED
        self.damage = PLAYER_DAMAGE

    def heal(self, health):
        self.hp = min(self.hp + health, self.max_hp)

    def take_damage(self, damage):
        if self.time_per_damage > TIME_INVULNERABILITY:
            self.hp = max(self.hp - damage, 0)

            self.time_per_damage = 0


    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def update(self):
        super().update()
        AnimatedObject.update(self)
        self.time_per_shoot += self.t
        self.time_per_damage += self.t
        self.time_animation += self.t

    def shoot(self, camera):
        if self.time_per_shoot >= TIME_PER_SHOOT:
            x = self.rect.center[0] + camera.dx
            y = self.rect.center[1] + camera.dy
            Bullet(camera, x, y, self, (0, 0, 0, 0), OBJECT_BULLET)
            self.time_per_shoot = 0
