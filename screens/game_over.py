import pygame
import os
from services.records import is_high_score, add_record
from screens.name_input import get_player_name
from screens.records import show_records

FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")

def show_game_over(screen, score):
    """Muestra la pantalla de game over con sistema de records"""
    
    # Cargar fuentes
    try:
        title_font = pygame.font.Font(FONT_PATH, 24)
        score_font = pygame.font.Font(FONT_PATH, 20)
        button_font = pygame.font.Font(FONT_PATH, 16)
        small_font = pygame.font.Font(FONT_PATH, 12)
    except:
        title_font = pygame.font.SysFont(None, 32)
        score_font = pygame.font.SysFont(None, 28)
        button_font = pygame.font.SysFont(None, 24)
        small_font = pygame.font.SysFont(None, 18)
    
    # Colores
    title_color = (255, 0, 0)
    score_color = (255, 255, 255)
    button_color = (200, 200, 200)
    highlight_color = (255, 215, 0)
    
    screen_width, screen_height = screen.get_size()
    
    # Verificar si es un record
    is_record = is_high_score(score)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Si es record, pedir nombre
                    if is_record:
                        player_name = get_player_name(screen, score)
                        if player_name:
                            add_record(player_name, score)
                            records_result = show_records(screen)
                            if records_result == "exit":
                                return "exit"
                    return "menu"
                elif event.key == pygame.K_r:
                    # Mostrar records
                    records_result = show_records(screen)
                    if records_result == "exit":
                        return "exit"
        
        # Fondo
        screen.fill((0, 0, 20))
        
        # Título
        title_text = title_font.render("GAME OVER", True, title_color)
        title_rect = title_text.get_rect(center=(screen_width//2, 100))
        screen.blit(title_text, title_rect)
        
        # Score
        score_text = f"Score: {score:,}"
        score_surface = score_font.render(score_text, True, score_color)
        score_rect = score_surface.get_rect(center=(screen_width//2, 180))
        screen.blit(score_surface, score_rect)
        
        # Mensaje de record si aplica
        if is_record:
            record_text = "NEW HIGH SCORE!"
            record_surface = score_font.render(record_text, True, highlight_color)
            record_rect = record_surface.get_rect(center=(screen_width//2, 220))
            screen.blit(record_surface, record_rect)
        
        # Botones
        restart_text = "Press ENTER to restart"
        restart_surface = button_font.render(restart_text, True, button_color)
        restart_rect = restart_surface.get_rect(center=(screen_width//2, 300))
        screen.blit(restart_surface, restart_rect)
        
        records_text = "Press R to view records"
        records_surface = button_font.render(records_text, True, button_color)
        records_rect = records_surface.get_rect(center=(screen_width//2, 340))
        screen.blit(records_surface, records_rect)
        
        pygame.display.flip()
