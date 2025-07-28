import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, min_speed, max_speed, color):
        super().__init__()
        
        size = 40  # ancho y alto del sprite
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)

        # 🎨 Dibujar estrella sobre superficie
        self._draw_star(self.image, color, size)

        self.rect = self.image.get_rect(
            topleft=(random.randint(0, screen_width - size), 0)
        )
        self.speed = random.randint(min_speed, max_speed)

    def update(self):
        self.rect.y += self.speed

    def _draw_star(self, surface, color, size):
        cx, cy = size // 2, size // 2
        r1, r2 = size // 2 - 2, size // 5

        # Coordenadas aproximadas para estrella de 5 puntas
        points = []
        for i in range(10):
            angle = i * 36  # 360° / 10
            radius = r1 if i % 2 == 0 else r2
            x = cx + radius * pygame.math.Vector2(1, 0).rotate(angle).x
            y = cy + radius * pygame.math.Vector2(1, 0).rotate(angle).y
            points.append((x, y))

        pygame.draw.polygon(surface, color, points)
