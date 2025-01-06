import pygame
from pygame.sprite import Sprite

from Camera import Camera


class Object(Sprite):
    def __init__(self, all_sprites, path, camera: Camera, x=0, y=0):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.camera = camera
        self.image = pygame.image.load(path)
        self.root_image = pygame.image.load(path)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x - self.camera.dx
        self.rect.y = self.y - self.camera.dy

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)