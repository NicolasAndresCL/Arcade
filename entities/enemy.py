import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, min_speed, max_speed, color):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(
            topleft=(random.randint(0, screen_width - 20), 0)
        )
        self.speed = random.randint(min_speed, max_speed)

    def update(self):
        self.rect.y += self.speed
