import pygame

from classes.Consts import *
from classes.States import States


class AnimatedObject:
    def __init__(self, state: States, animation_idle=None, animation_run=None, animation_get_damage=None):
        self.state = state
        if animation_idle:
            self.animation_idle = pygame.image.load(animation_idle)
        if animation_run:
            self.animation_run = pygame.image.load(animation_run)
        if animation_get_damage:
            self.animation_get_damage = pygame.image.load(animation_get_damage)

        self.last_update = pygame.time.get_ticks()
        self.cur_frame = 0
        self.frames = []
        self.frame_rate = 100
        self.update_animation()
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()

    def update_animation(self):
        match self.state:
            case States.run:
                self.cut_sheet(self.animation_run, 1, 8)
            case States.idle:
                self.cut_sheet(self.animation_idle, 1, 6)
            case States.get_damage:
               self.cut_sheet(self.animation_get_damage, 1, 8)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.play_next_frame()
            self.last_update = now

    def play_next_frame(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        if not sheet:
            return
        self.frames.clear()
        self.rect = pygame.Rect(WIDTH // 2 - sheet.get_width() // columns // 2,
                                HEIGHT // 2 - sheet.get_height() // rows // 2, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def change_state(self, new_state: States):
        self.state = new_state
        self.update_animation()
