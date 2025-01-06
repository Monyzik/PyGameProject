import math

import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, all_sprites, path, center, hp=100, speed=10, damage=10):
        super().__init__(all_sprites)
        self.speed = speed
        self.image = pygame.image.load(path)
        self.root_image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.move_ip(*center)
        self.center = center
        self.x = center[0]
        self.y = center[1]
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.damage = damage


    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) + 180
        if 90 < angle < 270:
            self.image = pygame.transform.rotate(self.root_image, 360 - int(angle))
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.image = pygame.transform.rotate(self.root_image, int(angle))
        self.rect = self.image.get_rect(center=self.center)


    def heal(self, health):
        self.hp = min(self.hp + health, self.max_hp)


    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)


    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def update(self):
        self.rotate()