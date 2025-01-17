import pygame

all_sprites = pygame.sprite.Group()
wall = pygame.sprite.Group()
objects = pygame.sprite.Group()
enemies = pygame.sprite.Group()

FPS = 60
TIME_PER_SHOOT = 0.5 * 1_000 #ms

"""Enemy"""
MIN_ENEMY_SPEED = 330 #px per second

"""Player"""
PLAYER_SPEED = 400 #px per second
PLAYER_HP = 100
PLAYER_DAMAGE = 10
PLAYER_IMAGE = "images/cat.png"
MAX_MOVING_COLLISION = PLAYER_SPEED * 1.1 / FPS
TIME_INVULNERABILITY = 0.3 * 1_000 #ms


"""Bullets"""
TIME_DURATION = 20 * 1_000 #ms
BULLET_SPEED = 800 #px per second
