import math
from math import hypot
from random import randint

import pygame

from classes.AnimatedObject import AnimatedObject
from classes.Consts import *
from classes.HpBar import HpBar
from classes.States import States


class Enemy(AnimatedObject):
    def __init__(self, camera, player, margins_l_t_r_b: tuple[int, int, int, int], x=0, y=0, multiplier=1):
        super().__init__(camera, margins_l_t_r_b, x, y, States.idle, animation_idle=ENEMY_RUN_ANIMATION,
                         animation_run=ENEMY_RUN_ANIMATION, animation_get_damage=ENEMY_HURT_ANIMATION,
                         animation_destroy=ENEMY_DEATH_ANIMATION, animation_attack=ENEMY_ATTACK_ANIMATION)
        self.camera = camera
        self.player = player
        self.damage = int(ENEMY_DAMAGE + randint(-5, 5) * multiplier)
        self.speed = int(ENEMY_SPEED + randint(-50, 50) * multiplier)
        self.hp = int(ENEMY_HEALTH + randint(-50, 50) * multiplier)
        w, h = 130, 10
        self.hp_bar = HpBar(self.camera, self.hitbox.centerx - w / 2, self.hitbox.top - 50, self.hp, w, h)
        self.add_collision_with_player()
        enemies_hiboxes.add(self.hitbox_sprite)

    def move_towards_player(self, player):
        if self.state in [States.get_damage, States.destroy, States.attack]:
            return
        dx, dy = player.hitbox.centerx - self.hitbox.centerx, player.hitbox.centery - self.hitbox.centery
        dist = math.hypot(dx, dy)

        dx, dy = dx * self.speed / dist / FPS, dy * self.speed / dist / FPS
        self.move(dx, dy)
        self.hp_bar.move(dx, dy)

        # sprites = pygame.sprite.spritecollide(player.hitbox_sprite, enemies_hiboxes, False)
        if hypot(self.hitbox.centerx - player.hitbox.centerx, self.hitbox.centery - player.hitbox.centery) < 65:
        # if self.hitbox_sprite in sprites:
            self.change_state(States.attack)
            player.take_damage(self.damage)
            return



        self.check_rotate(dx) # TODO make normal mirror
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
        self.hp_bar.take_damage(damage)
        self.hp -= damage

    def update(self):
        super().update()
        self.hp_bar.update()
        self.move_towards_player(self.player)
        if self.hp <= 0:
            try:
                super().change_state(States.destroy)
                enemies_arr.remove(self)
                enemies_hiboxes.remove(self.hitbox_sprite)
                all_sprites.remove(self)
                all_sprites.remove(self.hp_bar)
                self.hp_bar.kill()
                self.kill()
            except Exception as e:
                print(e)
        # self.move()
