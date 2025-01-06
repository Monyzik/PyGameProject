import sys

import pygame

from classes.Camera import Camera
from classes.Enemy import Enemy
from classes.Object import Object
from classes.Player import Player

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

FPS = 50


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
    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    objects = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    path = "images/myGrass.png"
    camera = Camera(width, height, objects)
    grass = Object(all_sprites, path, camera, -(width // 2), -(height // 2))
    grass.image = pygame.transform.scale(grass.image, (width * 2, height * 2))
    path = "images/cat.png"
    player = Player(all_sprites, path, (width // 2, height // 2))
    enemy = Enemy(all_sprites, path, camera, width // 3, height // 3)
    enemies.add(enemy)

    while True:
        screen.fill((255, 255, 255))
        camera.update(player)
        pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        vector = [0, 0]

        key = pygame.key.get_pressed()
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

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
