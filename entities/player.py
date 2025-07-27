import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=10):
        super().__init__()
        radius = 10
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)        
        pygame.draw.circle(
            self.image,
            (94, 234, 212),           # color del jugador
            (radius, radius),         # centro del círculo
            radius                    # radio
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def handle_input(self, keys):
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed

    def update(self):
        keys = pygame.key.get_pressed()
        self.handle_input(keys)
