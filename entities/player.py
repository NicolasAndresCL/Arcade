import pygame
from entities.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, screen_height, speed=10):
        super().__init__()
        # Crear nave espacial
        width, height = 24, 32
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Colores de la nave
        nave_color = (94, 234, 212)  # Azul claro
        nave_dark = (64, 184, 162)   # Azul más oscuro para detalles
        engine_color = (255, 165, 0)  # Naranja para los motores
        
        # Dibujar el cuerpo principal de la nave (triángulo)
        points = [(width//2, 0), (0, height), (width, height)]
        pygame.draw.polygon(self.image, nave_color, points)
        
        # Dibujar detalles de la nave
        # Cabina (círculo pequeño)
        pygame.draw.circle(self.image, nave_dark, (width//2, height//3), 4)
        
        # Motores (rectángulos en la parte inferior)
        pygame.draw.rect(self.image, engine_color, (width//4, height-8, 4, 8))
        pygame.draw.rect(self.image, engine_color, (3*width//4-4, height-8, 4, 8))
        
        # Alas laterales
        pygame.draw.polygon(self.image, nave_dark, [(0, height//2), (4, height//2+4), (4, height//2-4)])
        pygame.draw.polygon(self.image, nave_dark, [(width, height//2), (width-4, height//2+4), (width-4, height//2-4)])
        
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shoot_delay = 0  # Contador para delay entre disparos
        self.shoot_cooldown = 10  # Frames entre disparos

    def update(self):
        keys = pygame.key.get_pressed()
        self.handle_input(keys)
        
        # Actualizar delay de disparo
        if self.shoot_delay > 0:
            self.shoot_delay -= 1

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
            
    def shoot(self):
        """Dispara un proyectil si no está en cooldown"""
        if self.shoot_delay <= 0:
            self.shoot_delay = self.shoot_cooldown
            return Bullet(self.rect.centerx, self.rect.top)
        return None
