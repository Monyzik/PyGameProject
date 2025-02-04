from random import randint

import pygame
from pygame.sprite import Sprite

from classes import States
from classes.Consts import *


class Object(Sprite):
    def __init__(self, camera, margins_l_t_r_b: tuple[int, int, int, int], x, y, path: str=DEFAULT_IMAGE, size: tuple[int, int] = None, color: tuple[int, int, int] = (255, 255, 255), group=None, width=0):
        self.image = pygame.image.load(path)
        self.root_image = pygame.image.load(path)
        self.size = size
        self.camera = camera
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        if group is None:
            super().__init__(all_sprites)
        else:
            super().__init__(group)
        if size is None:
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(x, y, size[0], size[1])
        self.margin_left, self.margin_top, self.margin_right, self.margin_bottom = margins_l_t_r_b
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy
        self.update_hitbox()


    def update(self):
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy
        self.hitbox.x = self.x + self.margin_left - self.camera.dx
        self.hitbox.y = self.y + self.margin_top - self.camera.dy


    def update_hitbox(self):
        self.hitbox_sprite = Sprite()
        self.hitbox_sprite.parent = self
        self.hitbox_sprite.rect = pygame.Rect(self.x + self.margin_left, self.y + self.margin_top,
                                              self.rect.width - self.margin_left - self.margin_right,
                                              self.rect.height - self.margin_bottom - self.margin_top)
        self.hitbox = self.hitbox_sprite.rect

    def draw(self, screen):
        if self.size is None:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect, width=self.width)

    def add_collision_with_player(self):
        objects.add(self.hitbox_sprite)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy



