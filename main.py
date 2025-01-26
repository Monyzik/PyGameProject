import sys
from multiprocessing.managers import State

import pygame

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
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]


if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Недореверси")
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    path = "images/myGrass.png"
    camera = Camera(width, height)
    grass = Object(path, camera, (0, 0), -(width // 2), -(height // 2))
    grass.image = pygame.transform.scale(grass.image, (width * 2, height * 2))
    path = "images/cat.png"
    player = Player((width // 2, height // 2), (20, 20))
    enemy = Enemy(path, camera, (20, 20), 0, height // 2)
    enemy2 = Enemy(path, camera, (20, 20), width, height // 2)
    enemy.add_collision_with_player()
    enemy2.add_collision_with_player()
    while True:
        screen.fill((255, 255, 255))
        clock.tick(FPS)
        camera.update(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
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
            player.change_state(States.run)
        else:
            player.change_state(States.idle)
        wall.update()
        wall.draw(screen)

        arr = sorted(list(all_sprites.sprites()), key=lambda x: x.rect.y)
        enemy.move_towards_player(player)
        enemy2.move_towards_player(player)
        all_sprites.update()
        for sprite in arr:
            sprite.draw(screen)
        # all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()
