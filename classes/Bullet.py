import math

from classes.AnimatedObject import AnimatedObject
from classes.Enemy import Enemy
from classes.Object import Object
from classes.Consts import *
from classes.States import States


class Bullet(AnimatedObject):
    def __init__(self, camera, x, y, player, margins_l_t_r_b: tuple[int, int, int, int], animation_or_image):
        # Object.__init__(camera, margins_l_t_r_b, x, y, animation_or_image)
        super().__init__(camera, margins_l_t_r_b, x, y, States.idle, FIREBALL_ANIMATION)
        self.x -= self.rect.width / 2
        self.y -= self.rect.height / 2
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player.rect.center[0], mouse_y - player.rect.center[1]
        angle = math.atan2(rel_y, rel_x)
        self.angle = angle
        self.speed = BULLET_SPEED
        self.damage = player.damage

        self.last_update = pygame.time.get_ticks()


    def update(self):
        super().update()
        sprites = pygame.sprite.spritecollide(self.hitbox_sprite, enemies, dokill=False)
        for sprite in sprites:
            sprite.parent.take_damage(self.damage)
            self.kill()

        now = pygame.time.get_ticks()
        if now - self.last_update > TIME_DURATION:
            self.kill()
        dx, dy = math.cos(self.angle) * self.speed / FPS, math.sin(self.angle) * self.speed / FPS
        self.move(dx, dy)










