# core/engine.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from entities.player import Player

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player = Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2)

    running = True
    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.handle_input(keys)

        screen.fill((15, 118, 110))  # Teal 700
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
