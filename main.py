import sys
from random import randint

import pygame
from pygame import Color
from pygame.sprite import collide_rect

from classes.Consts import *
from classes.Bullet import Bullet
from classes.Camera import Camera
from classes.Enemy import Enemy
from classes.Map import Map
from classes.Object import Object
from classes.Player import Player
from classes.Score import Score
from classes.States import States

score: int = 0


def terminate():
    pygame.quit()
    sys.exit()


def draw_start_end_screens(intro_text, fon):
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


def start_screen():
    intro_text = ["The Game", "",
                  "Правила игры:",
                  "Убивайте врагов и побеждайте",
                  "Для начала игры нажмите любую клавишу"]

    fon = pygame.transform.scale(pygame.image.load('images/start_image.jpg'), (WIDTH, HEIGHT))
    draw_start_end_screens(intro_text, fon)


def end_screen():
    intro_text = ["Death", "",
                  f"Вы набрали {score} очков ",
                  "Нажмите любую клавишу, чтобы начать игру заново", ]

    fon = pygame.transform.scale(pygame.image.load('images/end_image.jpg'), (WIDTH, HEIGHT))
    draw_start_end_screens(intro_text, fon)


def main_game():
    all_sprites.empty()
    environment.empty()
    objects.empty()
    enemies_hiboxes.empty()
    enemies_arr.clear()

    cur_score = Score()

    screen.fill((255, 255, 255))
    camera = Camera(width, height)
    last_update = pygame.time.get_ticks()
    Map(all_sprites, camera)
    player = Player(size, (30, 130, 45, 30), camera)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        if player.hp < 0:
            global score
            score = cur_score.count
            return
        screen.fill((255, 255, 255))
        clock.tick(FPS)

        vector = [0, 0]

        # Стрельба и передвижение персонажа
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

        # Создание врагов
        now = pygame.time.get_ticks()
        if now - last_update > ENEMY_SPAWN_SPEED:
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

            enemies_arr.append(Enemy(camera, player, cur_score, (240, 230, 230, 260), x, y))

            last_update = now

        environment.update()

        # Отрисовка всех спрайтов в пределах экрана
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
        cur_score.show_score(screen)

        pygame.display.flip()


if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Недоигра")
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    start_screen()
    while True:
        main_game()
        end_screen()

pygame.quit()
