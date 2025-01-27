import pygame

from classes.Animation import Animation
from classes.Consts import *
from classes.States import States


class AnimatedObject:
    def __init__(self, state: States, animation_idle: Animation = None, animation_run: Animation = None,
                 animation_get_damage: Animation = None):
        self.state = state

        self.animation_idle = animation_idle
        self.animation_run = animation_run
        self.animation_get_damage = animation_get_damage

        self.last_update = pygame.time.get_ticks()
        self.cur_frame = 0
        self.frames = []
        self.frame_rate = 100
        self.update_animation()
        self.image = self.frames[self.cur_frame]
        self.time_frame = 0
        self.clock = pygame.time.Clock()

    def update_animation(self):
        if self.state == States.run:
            self.cut_sheet(self.animation_run.get_surface(), *self.animation_run.get_size())
        elif self.state == States.idle:
            self.cut_sheet(self.animation_idle.get_surface(), *self.animation_idle.get_size())
        elif self.state == States.get_damage:
            self.cut_sheet(self.animation_get_damage.get_surface(), *self.animation_get_damage.get_size())

    def update(self):
        t = self.clock.tick()
        self.time_frame += t

        if self.time_frame >= TIME_PER_FRAME * 10:
            self.play_next_frame()

        self.image = self.frames[self.cur_frame]

    def play_next_frame(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.time_frame = 0

    def cut_sheet(self, sheet: pygame.Surface, columns: int, rows: int):
        if not sheet:
            return
        self.frames.clear()
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)

        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        self.image = self.frames[self.cur_frame]

    def change_state(self, new_state: States):
        self.state = new_state
        self.update_animation()
