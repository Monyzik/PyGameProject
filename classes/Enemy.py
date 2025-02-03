import math

import pygame

from classes.AnimatedObject import AnimatedObject
from classes.Consts import *
from classes.States import States


class Enemy(AnimatedObject):
    def __init__(self, camera, margins_l_t_r_b: tuple[int, int, int, int], x=0, y=0, damage=10, speed=MIN_ENEMY_SPEED,
                 hp=50):
        super().__init__(camera, margins_l_t_r_b, x, y, States.idle, animation_idle=ENEMY_RUN_ANIMATION,
                         animation_run=ENEMY_RUN_ANIMATION, animation_get_damage=ENEMY_HURT_ANIMATION,
                         animation_destroy=ENEMY_DEATH_ANIMATION)
        self.camera = camera
        self.damage = damage
        self.speed = speed
        self.hp = hp
        enemies.add(self.hitbox_sprite)

    def move_towards_player(self, player):
        if self.state in [States.get_damage, States.destroy]:
            return
        dx, dy = player.hitbox.centerx - self.hitbox.centerx, player.hitbox.centery - self.hitbox.centery
        dist = math.hypot(dx, dy)

        sprites = pygame.sprite.spritecollideany(player, enemies)
        if sprites:  # TODO make normal condition to stop enemy, when he touch player
            player.take_damage(self.damage)
            return
        dx, dy = dx * self.speed / dist / FPS, dy * self.speed / dist / FPS
        self.move(dx, dy)
        AnimatedObject.update(self)

    # def rotate(self):
    #     rel_x = self.camera.dx - self.x + self.camera.rect.centerx
    #     rel_y = self.camera.dy - self.y + self.camera.rect.centery
    #     angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) + 180
    #     if 90 < angle < 270:
    #         self.image = pygame.transform.rotate(self.root_image, 360 - int(angle))
    #         self.image = pygame.transform.flip(self.image, False, True)
    #     else:
    #         self.image = pygame.transform.rotate(self.root_image, int(angle))
    #     self.rect = self.image.get_rect(center=self.rect.center)

    def take_damage(self, damage):
        super().change_state(States.get_damage)
        self.hp -= damage
        if self.hp <= 0:
            super().change_state(States.destroy)

    def update(self):
        super().update()
        # self.move()
