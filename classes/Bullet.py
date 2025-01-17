import math


from classes.Enemy import Enemy
from classes.Object import Object
from classes.Consts import *


class Bullet(Object):
    def __init__(self, path: str, camera, dw_dh: tuple[int, int], x, y, player):
        super().__init__(path, camera, dw_dh, x, y)
        self.x -= self.rect.width / 2
        self.y -= self.rect.height / 2
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player.rect.center[0], mouse_y - player.rect.center[1]
        angle = math.atan2(rel_y, rel_x)
        self.angle = angle
        self.speed = BULLET_SPEED
        self.clock = pygame.time.Clock()
        self.time = 0
        self.damage = player.damage

    def update(self):
        super().update()
        sprites = pygame.sprite.spritecollide(self.hitbox_sprite, enemies, dokill=False)
        for sprite in sprites:
            sprite.parent.take_damage(self.damage)
            self.kill()

        self.time += self.clock.tick()
        if self.time >= TIME_DURATION:
            self.kill()
        dx, dy = math.cos(self.angle) * self.speed / FPS, math.sin(self.angle) * self.speed / FPS
        self.move(dx, dy)










