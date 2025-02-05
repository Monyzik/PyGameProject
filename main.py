import sys

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
    pygame.display.set_caption("Недоигра")
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    screen.fill((255, 255, 255))
    camera = Camera(width, height)
    grass = Object(camera, (0, 0, 0, 0), -(width // 2), -(height // 2), GRASS_IMAGE)
    grass.image = pygame.transform.scale(grass.image, (width * 2, height * 2))
    grass.hitbox = pygame.Rect(-2000, -2000, 4000, 1)
    player = Player((width // 2, height // 2), (30, 130, 0, 30), camera)
    object = Object(camera, (0, 0, 0, 0), 100, 100, size=(200, 200))
    object.add_collision_with_player()
    enemies_arr = []
    enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), 0, 0))
    enemies_arr.append(Enemy(camera, player, enemies_arr, (240, 230, 230, 260), 500, 0))
    while True:
        if player.hp < 0:
            pygame.quit()
            exit(0) #TODO make normal start and end screen (need to delete this line!)
        screen.fill((255, 255, 255))
        clock.tick(FPS)

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



        # all_sprites.draw(screen)

        pygame.display.flip()
pygame.quit()
