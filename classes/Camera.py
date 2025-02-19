from classes.Player import *


class Camera:
    def __init__(self, width: int, height: int):
        self.rect = pygame.Rect(0, 0, width, height)
        self.objects = all_sprites
        self.dx = 0
        self.dy = 0
        self.clock = pygame.time.Clock()
        self.rect = pygame.Rect(0, 0, width, height)

    def move(self, vector: list[int], player: Player):
        if vector[0] and vector[1]:
            vector[0] /= 2 ** 0.5
            vector[1] /= 2 ** 0.5
        self.dx += vector[0] * player.speed / FPS
        self.dy += vector[1] * player.speed / FPS
        player.move(vector[0] * player.speed / FPS, vector[1] * player.speed / FPS)

    def update(self, player: Player):
        sprites = pygame.sprite.spritecollide(player, objects, dokill=False)

        # Реализация коллизии
        for sprite in sprites:
            hitbox_player = player.hitbox
            hitbox_sprite = sprite.rect
            f_1 = hitbox_sprite.right - hitbox_player.left
            f_2 = hitbox_sprite.bottom - hitbox_player.top
            f_3 = hitbox_player.right - hitbox_sprite.left
            f_4 = hitbox_player.bottom - hitbox_sprite.top

            mini = min(f_1, f_2, f_3, f_4)
            if hitbox_player.left <= hitbox_sprite.right and hitbox_player.center[0] >= hitbox_sprite.center[
                0] and f_1 == mini:
                self.dx += hitbox_sprite.right - hitbox_player.left - 1
                player.hp_bar.move(hitbox_sprite.right - hitbox_player.left - 1, 0)
            if hitbox_player.top <= hitbox_sprite.bottom and hitbox_player.center[1] >= hitbox_sprite.center[
                1] and f_2 == mini:
                self.dy += hitbox_sprite.bottom - hitbox_player.top - 1
                player.hp_bar.move(0, hitbox_sprite.bottom - hitbox_player.top - 1)
            if hitbox_player.right >= hitbox_sprite.left and hitbox_player.center[0] <= hitbox_sprite.center[
                0] and f_3 == mini:
                self.dx -= hitbox_player.right - hitbox_sprite.left - 1
                player.hp_bar.move(-(hitbox_player.right - hitbox_sprite.left - 1), 0)
            if hitbox_player.bottom >= hitbox_sprite.top and hitbox_player.center[1] <= hitbox_sprite.center[
                1] and f_4 == mini:
                self.dy -= hitbox_player.bottom - hitbox_sprite.top - 1
                player.hp_bar.move(0, -(hitbox_player.bottom - hitbox_sprite.top - 1))
