import math

import pygame
from classes.Object import Object


class Enemy(Object):
    def __init__(self, all_sprites, path, camera, x=0, y=0, damage=10, speed=5, hp=50):
        super().__init__(all_sprites, path, x, y)
        self.camera = camera
        self.damage = damage
        self.speed = speed
        self.hp = hp

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
        super().update()