import pygame
from pygame.sprite import Sprite

from classes.Consts import *


class Object(Sprite):
    def __init__(self, path: str, camera, dw_dh, x, y):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.dw, self.dh = dw_dh
        self.camera = camera
        self.image = pygame.image.load(path)
        self.root_image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.hitbox_sprite = Sprite()
        self.hitbox_sprite.parent = self
        self.hitbox_sprite.rect = pygame.Rect(self.x + dw_dh[0], self.y + dw_dh[1], self.rect.width - 2 * dw_dh[0],
                                       self.rect.height - 2 * dw_dh[1])
        self.hitbox = self.hitbox_sprite.rect
        self.objects = None
        self.clock = pygame.time.Clock()

    def update(self):
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy
        self.hitbox.x = self.x + self.dw - self.camera.dx
        self.hitbox.y = self.y + self.dh - self.camera.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def add_collision_with_player(self):
        objects.add(self.hitbox_sprite)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
