import sys

import pygame
from pygame import Color

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
    for x in range(8):
        for y in range(8):
            grass = Object(camera, (0, 0, 0, 0), x * 255, y * 255, GRASS_IMAGE)
            grass.hitbox = pygame.Rect(-2000, -2000, 4000, 1)
    # grass = Object(camera, (0, 0, 0, 0), -(width // 2), -(height // 2), GRASS_IMAGE)
    # grass.image = pygame.transform.scale(grass.image, (width * 2, height * 2))
    # grass.hitbox = pygame.Rect(-2000, -2000, 4000, 1)
    player = Player(size, (30, 130, 45, 30), camera)
    object = Object(camera, (0, 0, 0, 0), 100, 100, size=(200, 200))
    object.add_collision_with_player()
    enemies_arr = []
    enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), 0, 0))
    enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), 500, 0))
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
        # wall.update()
        wall.draw(screen)

        all_sprites.update()
        camera.update(player)
        arr = sorted(list(all_sprites.sprites()), key=lambda sprite: sprite.hitbox.bottom)
        for sprite in arr:
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
