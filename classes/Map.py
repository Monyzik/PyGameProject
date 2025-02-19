import pygame

from classes.Camera import Camera
from classes.Consts import GRASS_IMAGE, TOWER, HORIZONTAL_WALL, OTHER_HORIZONTAL_WALL, OTHER_VERTICAL_WALL, environment
from classes.Object import Object


class Map:  # Класс создания карты игры
    def __init__(self, all_sprites: pygame.sprite.Group, camera: Camera):
        for x in range(18):
            for y in range(14):
                Object(camera, (0, 0, 0, 0), x * 255 - 765, y * 255 - 765, GRASS_IMAGE.convert_alpha(),
                       group=environment)
        for x in range(12):
            for y in range(8):
                Object(camera, (0, 0, 0, 0), x * 255, y * 255, GRASS_IMAGE.convert_alpha(), group=environment)

        for i in range(8):
            other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 65, -300, OTHER_HORIZONTAL_WALL, group=environment)
            other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
            other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 382 / 2 + 65, -300, OTHER_HORIZONTAL_WALL,
                                    group=environment)
            other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
            Object(camera, (0, 0, 0, 0), 382 * i + 65, -256, HORIZONTAL_WALL, group=environment)

            other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 65, 1900, OTHER_HORIZONTAL_WALL, group=all_sprites)
            other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
            other_hor_wall = Object(camera, (0, 0, 0, 0), 382 * i + 382 / 2 + 65, 1900, OTHER_HORIZONTAL_WALL,
                                    group=all_sprites)
            other_hor_wall.image = pygame.transform.scale(other_hor_wall.image, (384 / 2, 384 / 2))
            Object(camera, (0, 0, 0, 0), 382 * i + 65, 1950, HORIZONTAL_WALL, group=all_sprites)

        Object(camera, (0, 0, 0, 0), -145, -300, TOWER, group=environment)
        Object(camera, (0, 0, 0, 0), 2975, -300, TOWER, group=environment)

        for i in range(6):
            Object(camera, (0, 0, 0, 0), -130, 382 * i - 100, OTHER_VERTICAL_WALL, group=environment)
            Object(camera, (0, 0, 0, 0), 2990, 382 * i - 100, OTHER_VERTICAL_WALL, group=environment)

        tower = Object(camera, (0, 0, 0, 0), -145, 2292 - 445, TOWER, group=all_sprites)
        tower.hitbox.h += 200
        tower = Object(camera, (0, 0, 0, 0), 2975, 2292 - 445, TOWER, group=all_sprites)
        tower.hitbox.h += 200

        left_corner = Object(camera, (0, 0, 0, 0), -345, -250, size=(500, 2300))
        left_corner.add_collision_with_player()
        top_corner = Object(camera, (0, 0, 0, 0), 55, -500, size=(3000, 500))
        top_corner.add_collision_with_player()
        right_corner = Object(camera, (0, 0, 0, 0), 3070, -250, size=(500, 2300))
        right_corner.add_collision_with_player()
        bottom_corner = Object(camera, (0, 0, 0, 0), 55, 2000, size=(3000, 500))
        bottom_corner.add_collision_with_player()
