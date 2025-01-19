import pygame

all_sprites = pygame.sprite.Group()
wall = pygame.sprite.Group()
objects = pygame.sprite.Group()
enemies = pygame.sprite.Group()


FPS = 60
TIME_PER_SHOOT = 0.5 * 1_000 #ms
TIME_PER_FRAME = 800 / FPS #ms
"""Enemy"""
MIN_ENEMY_SPEED = 330 #px per second

"""Player"""
PLAYER_SPEED = 400 #px per second
PLAYER_HP = 100
PLAYER_DAMAGE = 10
PLAYER_IMAGE = "animates/B_witch_idle_big.png"
TIME_INVULNERABILITY = 0.3 * 1_000 #ms


"""Bullets"""
TIME_DURATION = 20 * 1_000 #ms
BULLET_SPEED = 800 #px per second
