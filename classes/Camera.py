import pygame
from pygame import camera


class Camera:
    def __init__(self, width, height, objects):
        self.rect = pygame.Rect(0, 0, width, height)
        self.objects = objects
        self.dx = 0
        self.dy = 0

    def move(self, vector, obj):
        self.dx += vector[0] * obj.speed
        self.dy += vector[1] * obj.speed

    def update(self, target):
        sprite = pygame.sprite.spritecollideany(target, self.objects)
        if sprite:
            f_1 = sprite.rect.right - target.rect.left
            f_2 = sprite.rect.bottom - target.rect.top
            f_3 = target.rect.right - sprite.rect.left
            f_4 = target.rect.bottom - sprite.rect.top
            mini = min(f_1, f_2, f_3, f_4)
            if target.rect.left <= sprite.rect.right and target.rect.center[0] >= sprite.rect.center[0] and f_1 == mini:
                self.dx += sprite.rect.right - target.rect.left
            if target.rect.top <= sprite.rect.bottom and target.rect.center[1] >= sprite.rect.center[1] and f_2 == mini:
                self.dy += sprite.rect.bottom - target.rect.top
            if target.rect.right >= sprite.rect.left and target.rect.center[0] <= sprite.rect.center[0] and f_3 == mini:
                self.dx -= target.rect.right - sprite.rect.left
            if target.rect.bottom >= sprite.rect.top and target.rect.center[1] <= sprite.rect.center[1] and f_4 == mini:
                self.dy -= target.rect.bottom - sprite.rect.top
