import math

import pygame
from classes.Object import Object


class Enemy(Object):
    def __init__(self, all_sprites, path, camera, x=0, y=0, damage=10, speed=5, hp=50):
        super().__init__(all_sprites, path, x, y)
        self.camera = camera
        self.damage = damage
        self.speed = speed
        self.x = x
        self.y = y
        self.hp = hp

    def move_towards_player(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist < self.speed:  # TODO make normal condition to stop enemy, when he touch player
            return
        dx, dy = dx / dist, dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy

    def move(self):
        rel_x = self.camera.dx - self.x + self.camera.rect.centerx
        rel_y = self.camera.dy - self.y + self.camera.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) + 180
        if 90 < angle < 270:
            self.image = pygame.transform.rotate(self.root_image, 360 - int(angle))
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.image = pygame.transform.rotate(self.root_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.move()
