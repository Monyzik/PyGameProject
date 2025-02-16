import sys
from random import randint

import pygame
from pygame import Color
from pygame.sprite import collide_rect

from classes.Consts import *
from classes.Bullet import Bullet
from classes.Camera import Camera
from classes.Enemy import Enemy
from classes.Object import Object
from classes.Player import Player
from classes.States import States

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

sshoot_clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["The Game", "",
                  "Правила игры:",
                  "Убивайте врагов и побеждайте",
                  "Для начала игры нажмите любую клавишу"]

    fon = pygame.transform.scale(pygame.image.load('images/start_image.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

def main_game():
    screen.fill((255, 255, 255))
    camera = Camera(width, height)
    last_update = pygame.time.get_ticks()


    for x in range(18):
        for y in range(14):
            grass = Object(camera, (0, 0, 0, 0), x * 255 - 765, y * 255 - 765, GRASS_IMAGE.convert_alpha(), group=environment)
    for x in range(12):
        for y in range(8):
            grass = Object(camera, (0, 0, 0, 0), x * 255, y * 255, GRASS_IMAGE.convert_alpha(), group=environment)

    for i in range(8):
        other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 65, -300, OTHER_HORIZONTAL_WALL, group=environment)
        other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
        other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 382 / 2 + 65, -300, OTHER_HORIZONTAL_WALL, group=environment)
        other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
        hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 65, -256, HORIZONTAL_WALL, group=environment)

        other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 65, 1900, OTHER_HORIZONTAL_WALL, group=all_sprites)
        other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
        other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 382 / 2 + 65, 1900, OTHER_HORIZONTAL_WALL,
                                group=all_sprites)
        other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
        hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 65, 1950, HORIZONTAL_WALL, group=all_sprites)

    tower = Object(camera, (0, 0, 0, 0), -145, -300, TOWER, group=environment)
    tower = Object(camera, (0, 0, 0, 0), 2975, -300, TOWER, group=environment)

    for i in range(6):
        vertical_wall = Object(camera, (0, 0, 0, 0), -130, 382 * i - 100, OTHER_VERTICAL_WALL, group=environment)
        vertical_wall = Object(camera, (0, 0, 0, 0), 2990, 382 * i - 100, OTHER_VERTICAL_WALL, group=environment)

    tower = Object(camera, (0, 0, 0, 0), -145, 2292 - 445, TOWER, group=all_sprites)
    tower.hitbox.h += 200
    tower = Object(camera, (0, 0, 0, 0), 2975, 2292 - 445, TOWER, group=all_sprites)
    tower.hitbox.h += 200

    left_corner = Object(camera, (0, 0, 0, 0), 55, -250, size=(100, 2300))
    left_corner.add_collision_with_player()
    top_corner = Object(camera, (0, 0, 0, 0), 55, -100, size=(3000, 100))
    top_corner.add_collision_with_player()
    right_corner = Object(camera, (0, 0, 0, 0), 3070, -250, size=(100, 2300))
    right_corner.add_collision_with_player()
    bottom_corner = Object(camera, (0, 0, 0, 0), 55, 2000, size=(3000, 100))
    bottom_corner.add_collision_with_player()
    player = Player(size, (30, 130, 45, 30), camera)
    # dobject = Object(camera, (0, 0, 0, 0), 100, 100, size=(200, 200))
    # object.add_collision_with_player()
    enemies_arr = []
    # for _ in range(5):
    #     enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), 0, 0))
    # enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), 500, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        if player.hp < 0:
            pygame.quit()
            exit(0)  # TODO make normal start and end screen (need to delete this line!)
        screen.fill((255, 255, 255))
        clock.tick(FPS)

        vector = [0, 0]

        key = pygame.key.get_pressed()
        click = pygame.mouse.get_pressed()

        if click[0]:
            player.shoot(camera)

        if key[pygame.K_w]:
            vector[1] -= 1
        elif key[pygame.K_s]:
            vector[1] += 1
        if key[pygame.K_a]:
            vector[0] -= 1
        elif key[pygame.K_d]:
            vector[0] += 1

        if vector != [0, 0]:
            camera.move(vector, player)
            player.check_rotate(vector[0])
            if player.state not in [States.get_damage, States.destroy]:
                player.change_state(States.run)
        elif player.state not in [States.get_damage, States.destroy]:
            player.change_state(States.idle)

        now = pygame.time.get_ticks()
        if now - last_update > ENEMY_SPAWN_SPEED and len(enemies_arr) < 7:

            x = []
            y = []
            if int(155 - camera.dx) < 0:
                x.append(randint(int(155 - camera.dx), 0))
            if width < int(3700 - camera.dx):
                x.append(randint(width, int(3700 - camera.dx)))
            if int(0 - camera.dy) < 0:
                y.append(randint(int(0 - camera.dy), 0))
            if height < int(2000 - camera.dy):
                y.append(randint(height, int(2000 - camera.dy)))

            x, y = x[randint(0, len(x) - 1)], y[randint(0, len(y) - 1)]

            enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), x, y))

            last_update = now

        environment.update()
        for sprite in environment.sprites():
            if collide_rect(camera, sprite):
                sprite.draw(screen)

        all_sprites.update()
        camera.update(player)
        arr = sorted(list(all_sprites.sprites()), key=lambda sprite: sprite.hitbox.bottom)
        for sprite in arr:
            if collide_rect(camera, sprite):
                sprite.draw(screen)
        player.hp_bar.draw(screen)

        # all_sprites.draw(screen)

        pygame.display.flip()




if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Недоигра")
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    start_screen()
    main_game()


pygame.quit()
