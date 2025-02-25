from classes.Consts import *
from classes.Object import Object
from classes.States import States


class AnimatedObject(Object):  # Класс объектов с анимацией
    def __init__(self, camera, margins_l_t_r_b: tuple[int, int, int, int], x,
                 y, state: States, animation_idle: Animation, animation_run: Animation = None,
                 animation_get_damage: Animation = None, animation_destroy: Animation = None,
                 animation_attack: Animation = None, group=None):
        super().__init__(camera, margins_l_t_r_b, x, y, group=group)
        self.state = state
        self.need_rotate = False

        self.animation_idle = animation_idle
        self.animation_run = animation_run
        self.animation_get_damage = animation_get_damage
        self.animation_destroy = animation_destroy
        self.animation_attack = animation_attack

        self.sheet = self.animation_idle.get_surface()
        columns, rows = self.animation_idle.get_size()
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // columns,
                                self.sheet.get_height() // rows)

        self.last_update = pygame.time.get_ticks()
        self.cur_frame = 0
        self.frames = []
        self.frame_rate = 100
        self.update_animation()
        self.image = self.frames[self.cur_frame]
        self.update_hitbox()

    def update_animation(self):
        match self.state:
            case States.run:
                self.cut_sheet(self.animation_run.get_surface(), *self.animation_run.get_size())
            case States.idle:
                self.cut_sheet(self.animation_idle.get_surface(), *self.animation_idle.get_size())
            case States.get_damage:
                self.cur_frame = 0
                self.cut_sheet(self.animation_get_damage.get_surface(), *self.animation_get_damage.get_size())
            case States.destroy:
                self.cur_frame = 0
                self.cut_sheet(self.animation_destroy.get_surface(), *self.animation_destroy.get_size())
            case States.attack:
                self.cur_frame = 0
                self.cut_sheet(self.animation_attack.get_surface(), *self.animation_attack.get_size())

    def update(self):
        super().update()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.play_next_frame()
            self.last_update = now

    def play_next_frame(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.state in [States.get_damage, States.attack] and self.cur_frame == 0:
            self.change_state(States.idle)
        if self.state == States.destroy and self.cur_frame == 0:
            self.kill()
            self.hitbox_sprite.kill()
        self.image = self.frames[self.cur_frame]
        self.mirror()

    def cut_sheet(self, sheet: pygame.Surface, columns: int, rows: int):
        if not sheet:
            return
        self.frames.clear()

        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def change_state(self, new_state: States):
        self.state = new_state
        self.update_animation()

    def check_rotate(self, dx):
        if dx < 0:
            self.need_rotate = True
        else:
            self.need_rotate = False

    def mirror(self):
        if self.image and self.need_rotate:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], True, False)
