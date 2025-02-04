import pygame

from classes.Object import Object


class HpBar:
    def __init__(self, camera, x, y, max_hp, width, height, enemy):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.enemy = enemy
        self.max_hp_object = Object(camera, (0, 0, 0, 0), x, y, color=(255, 0, 0), size=(width, height))
        self.current_hp_object = Object(camera, (0, 0, 0, 0), x, y, color=(0, 255, 0), size=(width, height))
        self.frame = Object(camera, (0, 0, 0, 0), x - 3, y - 3, color=(0, 0, 0), size=(width + 6, height + 6), width=3)


    def update(self):
        self.current_hp_object.rect.width = self.max_hp_object.rect.width * self.current_hp / self.max_hp

    def take_damage(self, damage):
        self.current_hp -= damage

    def kill(self):
        self.current_hp_object.kill()
        self.max_hp_object.kill()
        self.frame.kill()


    def move(self, dx, dy):
        self.current_hp_object.move(dx, dy)
        self.max_hp_object.move(dx, dy)
        self.frame.move(dx, dy)



