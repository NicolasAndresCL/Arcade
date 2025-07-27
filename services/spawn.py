import pygame
import random
from entities.enemy import Enemy

def spawn_enemy(enemy_group, screen_width, screen_height, max_enemies=10):
    if len(enemy_group) < max_enemies:
        if random.random() < 0.15:  # Probabilidad de spawn
            enemy = Enemy(screen_width, screen_height)
            enemy_group.add(enemy)
