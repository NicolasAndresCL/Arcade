import pygame

def show_game_over(screen, score):
    font = pygame.font.SysFont(None, 48)
    text = font.render(f"Game Over - Score: {score}", True, (255, 0, 0))
    button_font = pygame.font.SysFont(None, 36)
    button_text = button_font.render("Volver a jugar [ENTER]", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(text, (100, 150))
    screen.blit(button_text, (100, 230))
    pygame.display.flip()
