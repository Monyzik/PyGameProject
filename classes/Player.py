from pygame.sprite import Sprite

from classes.AnimatedObject import AnimatedObject
from classes.Bullet import *
from classes.Consts import *
from classes.States import States


class Player(Sprite, AnimatedObject):
    def __init__(self, center, dw_dh):
        Sprite.__init__(self, all_sprites)
        AnimatedObject.__init__(self, state=States.idle, animation_idle=PLAYER_IDLE_ANIMATION,
                                animation_run=PLAYER_RUN_ANIMATION)
        self.all_sprites = all_sprites
        AnimatedObject.update(self)

        self.x = center[0] - self.rect.width // 2
        self.y = center[1] - self.rect.height // 2
        self.hitbox_sprite = Sprite()
        self.hitbox_sprite.parent = self
        self.hitbox_sprite.rect = pygame.Rect(self.x + dw_dh[0], self.y + dw_dh[1], self.rect.width - 2 * dw_dh[0],
                                              self.rect.height - 2 * dw_dh[1])

        self.hitbox = self.hitbox_sprite.rect
        self.clock = pygame.time.Clock()
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
        AnimatedObject.update(self)
        screen.blit(self.image, self.rect)

    def move_animation(self):
        if self.time_animation >= TIME_PER_FRAME * 10:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.time_animation = 0
        self.image = self.frames[self.cur_frame]

    def update(self):
        t = self.clock.tick()
        self.time_per_shoot += t
        self.time_per_damage += t
        self.time_animation += t
        pass

    def shoot(self, camera):
        if self.time_per_shoot >= TIME_PER_SHOOT:
            x = self.rect.center[0] + camera.dx
            y = self.rect.center[1] + camera.dy
            Bullet("images/bullet.png", camera, (5, 5), x, y, self)
            self.time_per_shoot = 0
