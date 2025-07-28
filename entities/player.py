import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, screen_height, speed=10):
        super().__init__()
        radius = 10
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (94, 234, 212), (radius, radius), radius)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        keys = pygame.key.get_pressed()
        self.handle_input(keys)

        # 🎯 Corrección de límites usando coordenadas reales
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
