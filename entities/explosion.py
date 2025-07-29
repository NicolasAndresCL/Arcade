import pygame
import math

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(255, 200, 50), max_radius=30, duration=20):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.max_radius = max_radius
        self.duration = duration
        self.frame = 0
        self.image = pygame.Surface((max_radius*2, max_radius*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.frame += 1
        if self.frame > self.duration:
            self.kill()
        else:
            self.image.fill((0, 0, 0, 0))
            progress = self.frame / self.duration
            radius = int(self.max_radius * progress)
            alpha = int(255 * (1 - progress))
            # Círculo principal
            pygame.draw.circle(self.image, self.color + (alpha,), (self.max_radius, self.max_radius), radius)
            # Círculo exterior (más difuso)
            if radius > 8:
                pygame.draw.circle(self.image, (255, 255, 255, int(alpha/2)), (self.max_radius, self.max_radius), int(radius*1.3), 2) 