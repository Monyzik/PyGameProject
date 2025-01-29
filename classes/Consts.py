import pygame

from classes.Animation import Animation

all_sprites = pygame.sprite.Group()
wall = pygame.sprite.Group()
objects = pygame.sprite.Group()
enemies = pygame.sprite.Group()

WIDTH, HEIGHT = 1600, 900
FPS = 60
TIME_PER_SHOOT = 0.5 * 1_000 #ms
TIME_PER_FRAME = 800 / FPS #ms
"""Enemy"""
MIN_ENEMY_SPEED = 330 #px per second
ENEMY_RUN_ANIMATION = Animation("animates/orc_walk_big.png", 8, 1)

"""Player"""
PLAYER_SPEED = 400 #px per second
PLAYER_HP = 100
PLAYER_DAMAGE = 10

PLAYER_IMAGE = "animates/B_witch_idle_big.png"
PLAYER_RUN_ANIMATION = Animation("animates/B_witch_run_big.png", 1, 8)
PLAYER_IDLE_ANIMATION = Animation("animates/B_witch_idle_big.png", 1, 6)

TIME_INVULNERABILITY = 0.3 * 1_000 #ms

"""Objects"""
DEFAULT_IMAGE = "images/default.png"
GRASS_IMAGE = "images/myGrass.png"


"""Bullets"""
BULLET_IMAGE = "images/bullet.png"
TIME_DURATION = 20 * 1_000 #ms
BULLET_SPEED = 800 #px per second
