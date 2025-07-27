
import pygame

class Player:
    def __init__(self, x, y, width=20, height=20, color=(94, 234, 212), speed=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
