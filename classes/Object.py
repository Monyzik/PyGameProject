import pygame
from pygame.sprite import Sprite

from classes import States
from classes.AnimatedObject import AnimatedObject
from classes.Consts import *


class Object(Sprite, AnimatedObject):
    def __init__(self, camera, margins_l_t_r_b: tuple[int, int, int, int], x, y, animation_or_image):
        super().__init__(all_sprites)
        AnimatedObject.__init__(self, state=States.States.idle, animation_idle=animation_or_image)
        self.x = x
        self.y = y
        self.margin_left, self.margin_top, self.margin_right, self.margin_bottom = margins_l_t_r_b
        self.camera = camera
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy
        self.hitbox_sprite = Sprite()
        self.hitbox_sprite.parent = self
        self.hitbox_sprite.rect = pygame.Rect(self.x + self.margin_left, self.y + self.margin_top,
                                              self.rect.width - self.margin_left - self.margin_right,
                                              self.rect.height - self.margin_bottom - self.margin_top)
        self.hitbox = self.hitbox_sprite.rect
        self.objects = None

    def update(self):
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy
        self.hitbox.x = self.x + self.margin_left - self.camera.dx
        self.hitbox.y = self.y + self.margin_top - self.camera.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def add_collision_with_player(self):
        objects.add(self.hitbox_sprite)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
