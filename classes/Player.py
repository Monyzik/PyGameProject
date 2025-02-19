from pygame.sprite import Sprite

from classes.Bullet import *
from classes.Consts import *
from classes.HpBar import HpBar
from classes.States import States


class Player(AnimatedObject):
    def __init__(self, size_window, margins_l_t_r_b: tuple[int, int, int, int], camera):

        super().__init__(camera, margins_l_t_r_b, size_window[0] / 2, size_window[1] / 2, States.idle,
                         animation_idle=PLAYER_IDLE_ANIMATION,
                         animation_run=PLAYER_RUN_ANIMATION, animation_destroy=PLAYER_DEATH_ANIMATION,
                         animation_get_damage=PLAYER_TAKE_DAMAGE_ANIMATION)
        self.all_sprites = all_sprites
        self.margin_left, self.margin_top, self.margin_right, self.margin_bottom = margins_l_t_r_b
        self.frames = []
        self.cut_sheet(PLAYER_IMAGE, 1, 6)
        self.cur_frame = 0
        self.rect = self.image.get_rect()

        self.x = size_window[0] / 2 - self.rect.width // 2
        self.y = size_window[1] / 2 - self.rect.height // 2
        self.update_hitbox()
        self.last_shoot = 0
        self.time_per_damage = 0

        self.rect.x = self.x
        self.rect.y = self.y
        self.hp = PLAYER_HP
        self.max_hp = PLAYER_HP
        self.speed = PLAYER_SPEED
        self.damage = PLAYER_DAMAGE
        k = 2.5
        self.hp_bar = HpBar(self.camera, 100, 35, self.max_hp, size_window[0] / k, 25, width_rect=5)
        self.hp_bar.add_text()

    def heal(self, health):
        self.hp = min(self.hp + health, self.max_hp)

    def take_damage(self, damage):
        now = pygame.time.get_ticks()
        if now - self.time_per_damage > TIME_INVULNERABILITY:
            self.hp -= damage
            self.hp_bar.take_damage(damage)
            if self.hp < 0:
                super().change_state(States.destroy)
            else:
                super().change_state(States.get_damage)
            self.time_per_damage = now

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        Sprite.update(self)
        self.hp_bar.update()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.play_next_frame()
            self.last_update = now

    def shoot(self, camera):
        now = pygame.time.get_ticks()
        if now - self.last_shoot >= TIME_PER_SHOOT:
            x = self.rect.center[0] + camera.dx
            y = self.rect.center[1] + camera.dy
            Bullet(camera, x, y, self, (0, 0, 0, 0))
            self.last_shoot = now

    def move(self, dx, dy):
        self.hp_bar.move(dx, dy)
