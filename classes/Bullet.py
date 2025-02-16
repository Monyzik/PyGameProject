import math

from classes.AnimatedObject import AnimatedObject
from classes.Consts import *
from classes.States import States


class Bullet(AnimatedObject):
    def __init__(self, camera, x, y, player, margins_l_t_r_b: tuple[int, int, int, int]):
        super().__init__(camera, margins_l_t_r_b, x, y, States.idle, FIREBALL_ANIMATION, animation_destroy=FIREBALL_DESTROY)
        self.x -= self.rect.width / 2
        self.y -= self.rect.height / 2
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player.rect.center[0], mouse_y - player.rect.center[1]
        angle = math.atan2(rel_y, rel_x)
        self.angle = angle
        self.speed = BULLET_SPEED
        self.damage = player.damage

        self.last_update_bullet = pygame.time.get_ticks()


    def update(self):
        super().update()
        if self.state == States.destroy:
            return
        sprites = pygame.sprite.spritecollide(self.hitbox_sprite, enemies_hiboxes, dokill=False)
        for sprite in sprites:
            sprite.parent.take_damage(self.damage)
            self.change_state(States.destroy)

        now = pygame.time.get_ticks()
        if now - self.last_update_bullet > TIME_DURATION:
            self.change_state(States.destroy)
        dx, dy = math.cos(self.angle) * self.speed / FPS, math.sin(self.angle) * self.speed / FPS
        self.move(dx, dy)










