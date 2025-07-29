import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=8):
        super().__init__()
        # Crear proyectil
        width, height = 4, 12
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Color del proyectil
        bullet_color = (255, 255, 0)  # Amarillo
        glow_color = (255, 255, 255)  # Blanco para el brillo
        
        # Dibujar proyectil con efecto de brillo
        pygame.draw.rect(self.image, bullet_color, (0, 0, width, height))
        pygame.draw.rect(self.image, glow_color, (1, 1, width-2, height-2))
        
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        
    def update(self):
        # Mover proyectil hacia arriba
        self.rect.y -= self.speed
        
        # Eliminar proyectil si sale de pantalla
        if self.rect.bottom < 0:
            self.kill() 