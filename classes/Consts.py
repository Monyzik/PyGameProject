import pygame

from classes.Animation import Animation

all_sprites = pygame.sprite.Group()
environment = pygame.sprite.Group()
objects = pygame.sprite.Group()
enemies_hiboxes = pygame.sprite.Group()
enemies_arr = []

WIDTH, HEIGHT = 1600, 900
FPS = 60
TIME_PER_SHOOT = 0.5 * 1_000  # ms
"""Enemy"""
ENEMY_SPEED = 450  # px per second
ENEMY_DAMAGE = 15
ENEMY_HEALTH = 50
ENEMY_SPAWN_SPEED = 3 * 1_000  # ms

ENEMY_RUN_ANIMATION = Animation("animates/orc_walk_big.png", 8, 1)
ENEMY_HURT_ANIMATION = Animation("animates/orc_hurt.png", 4, 1)
ENEMY_DEATH_ANIMATION = Animation("animates/orc_death.png", 4, 1)
ENEMY_ATTACK_ANIMATION = Animation("animates/orc_attack01.png", 6, 1)

"""Player"""
PLAYER_SPEED = 400  # px per second
PLAYER_HP = 200
PLAYER_DAMAGE = 10

PLAYER_IMAGE: pygame.Surface = pygame.image.load("animates/B_witch_idle_big.png")
PLAYER_RUN_ANIMATION = Animation("animates/B_witch_run_big.png", 1, 8)
PLAYER_IDLE_ANIMATION = Animation("animates/B_witch_idle_big.png", 1, 6)
PLAYER_DEATH_ANIMATION = Animation("animates/B_witch_death.png", 1, 6)
PLAYER_TAKE_DAMAGE_ANIMATION = Animation("animates/B_witch_take_damage.png", 1, 3)

TIME_INVULNERABILITY = 0.3 * 1_000  # ms

"""Objects"""
DEFAULT_IMAGE: pygame.Surface = pygame.image.load("images/nothing.png")
GRASS_IMAGE: pygame.Surface = pygame.image.load('images/grass.png')
HORIZONTAL_WALL: pygame.Surface = pygame.image.load('images/horizontal_wall.jpg')
VERTICAL_WALL: pygame.Surface = pygame.image.load('images/vertical_wall.png')
OTHER_VERTICAL_WALL: pygame.Surface = pygame.image.load('images/other_vertical_wall.png')
OTHER_HORIZONTAL_WALL: pygame.Surface = pygame.image.load('images/other_horizontal_wall.png')
TOWER = pygame.image.load('images/tower.png')

"""Bullets"""
FIREBALL_ANIMATION = Animation("animates/fireball_animation_small.png", 5, 1)
FIREBALL_DESTROY = Animation("animates/fireball_destroy.png", 3, 1)
BULLET_IMAGE: pygame.Surface = pygame.image.load("images/bullet.png")
TIME_DURATION = 5 * 1_000  # ms
BULLET_SPEED = 800  # px per second
