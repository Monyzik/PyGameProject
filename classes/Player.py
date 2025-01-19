from pygame.sprite import Sprite

from classes.Bullet import *
from classes.Consts import *


class Player(Sprite):
    def __init__(self, center, dw_dh):
        super().__init__(all_sprites)
        self.all_sprites = all_sprites
        # self.image = pygame.image.load(PLAYER_IMAGE)
        # self.root_image = pygame.image.load(PLAYER_IMAGE)
        self.frames = []
        self.cut_sheet(pygame.image.load(PLAYER_IMAGE), 1, 6)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()

        self.x = center[0] - self.rect.width // 2
        self.y = center[1] - self.rect.height // 2
        self.hitbox_sprite = Sprite()
        self.hitbox_sprite.parent = self
        self.hitbox_sprite.rect = pygame.Rect(self.x + dw_dh[0], self.y + dw_dh[1], self.rect.width - 2 * dw_dh[0],
                                       self.rect.height - 2 * dw_dh[1])


        self.hitbox = self.hitbox_sprite.rect
        self.clock = pygame.time.Clock()
        self.time_per_shoot = 0
        self.time_per_damage = 0
        self.time_animation = 0

        self.rect.x = self.x
        self.rect.y = self.y
        self.hp = PLAYER_HP
        self.max_hp = PLAYER_HP
        self.speed = PLAYER_SPEED
        self.damage = PLAYER_DAMAGE


    # def rotate(self):
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #     rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
    #     angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) + 180
    #     if 90 < angle < 270:
    #         self.image = pygame.transform.rotate(self.root_image, 360 - int(angle))
    #         self.image = pygame.transform.flip(self.image, False, True)
    #     else:
    #         self.image = pygame.transform.rotate(self.root_image, int(angle))
    #     self.rect = self.image.get_rect(center=self.center)

    def heal(self, health):
        self.hp = min(self.hp + health, self.max_hp)

    def take_damage(self, damage):
        if self.time_per_damage > TIME_INVULNERABILITY:
            self.hp = max(self.hp - damage, 0)

            self.time_per_damage = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


    def draw(self, screen):
        if self.time_animation >= TIME_PER_FRAME * 10:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.time_animation = 0
        self.image = self.frames[self.cur_frame]
        screen.blit(self.image, self.rect)



    def update(self):
        t = self.clock.tick()
        self.time_per_shoot += t
        self.time_per_damage += t
        self.time_animation += t
        pass
        # self.rotate()

    def shoot(self, camera):
        if self.time_per_shoot >= TIME_PER_SHOOT:
            x = self.rect.center[0] + camera.dx
            y = self.rect.center[1] + camera.dy
            Bullet("images/bullet.png", camera, (5, 5), x, y, self)
            self.time_per_shoot = 0
