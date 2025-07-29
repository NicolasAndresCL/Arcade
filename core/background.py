import pygame
import random

class Star:
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.original_x = x

    def update(self, screen_height):
        self.y += self.speed
        if self.y > screen_height:
            self.y = -10
            self.x = random.randint(0, 640)

    def draw(self, screen):
        # Dibujar estrella con efecto de brillo
        color = (255, 255, 255)
        if self.size > 1:
            # Estrellas más grandes son más brillantes
            brightness = min(255, 100 + self.size * 30)
            color = (brightness, brightness, brightness)
        
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)

class UniverseBackground:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.stars = []
        self.create_stars()
        
    def create_stars(self):
        # Crear estrellas de diferentes tamaños y velocidades
        for _ in range(100):  # 100 estrellas
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            speed = random.uniform(0.5, 2.0)
            size = random.randint(1, 3)
            self.stars.append(Star(x, y, speed, size))
    
    def update(self):
        for star in self.stars:
            star.update(self.screen_height)
    
    def draw(self, screen):
        # Fondo negro del universo
        screen.fill((0, 0, 20))  # Azul muy oscuro
        
        # Dibujar estrellas
        for star in self.stars:
            star.draw(screen) 