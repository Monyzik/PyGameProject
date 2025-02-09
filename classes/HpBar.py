import pygame

from classes.Object import Object


class HpBar:
    def __init__(self, camera, x, y, max_hp, width, height, width_rect=3):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_hp_object = Object(camera, (0, 0, 0, 0), x, y, color=(219, 88, 86), size=(width, height))
        self.current_hp_object = Object(camera, (0, 0, 0, 0), x, y, color=(119, 221, 119), size=(width, height))
        self.frame = Object(camera, (0, 0, 0, 0), x - width_rect, y - width_rect, color=(0, 0, 0), size=(width + 2 * width_rect, height + 2 * width_rect), width=width_rect)
        self.text = False


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


    def draw(self, screen):
        self.max_hp_object.draw(screen)
        self.current_hp_object.draw(screen)
        self.frame.draw(screen)
        if self.text:
            font = pygame.font.Font(None, 60)
            string_rendered = font.render("HP", 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.centery = self.max_hp_object.rect.centery
            intro_rect.right = self.max_hp_object.rect.left - 20
            screen.blit(string_rendered, intro_rect)

            font = pygame.font.Font(None, 30)
            string_rendered = font.render(f"{self.current_hp} / {self.max_hp}", 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.centery = self.max_hp_object.rect.centery
            intro_rect.centerx = self.max_hp_object.rect.centerx
            screen.blit(string_rendered, intro_rect)


    def add_text(self):
        self.text = True





