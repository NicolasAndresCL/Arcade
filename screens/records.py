import pygame
import os
from services.records import get_records

FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")

def show_records(screen):
    """Muestra la pantalla de records"""
    records = get_records()
    
    # Cargar fuente
    try:
        title_font = pygame.font.Font(FONT_PATH, 24)
        record_font = pygame.font.Font(FONT_PATH, 16)
        small_font = pygame.font.Font(FONT_PATH, 12)
    except:
        title_font = pygame.font.SysFont(None, 32)
        record_font = pygame.font.SysFont(None, 24)
        small_font = pygame.font.SysFont(None, 18)
    
    # Colores
    title_color = (255, 255, 255)
    record_color = (200, 200, 200)
    highlight_color = (255, 215, 0)  # Dorado para el primer lugar
    button_color = (150, 150, 150)
    
    screen_width, screen_height = screen.get_size()
    
    # Opciones de la pantalla de records
    options = [
        {"text": "BACK TO MENU", "action": "menu"},
        {"text": "EXIT GAME", "action": "exit"}
    ]
    selected_option = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected_option]["action"]
                elif event.key == pygame.K_ESCAPE:
                    return "menu"
        
        # Fondo
        screen.fill((0, 0, 20))
        
        # Título
        title_text = title_font.render("HIGH SCORES", True, title_color)
        title_rect = title_text.get_rect(center=(screen_width//2, 50))
        screen.blit(title_text, title_rect)
        
        # Mostrar records
        y_position = 120
        for i, record in enumerate(records):
            # Color especial para el primer lugar
            color = highlight_color if i == 0 else record_color
            
            # Número de posición
            pos_text = f"{i+1}."
            pos_surface = record_font.render(pos_text, True, color)
            screen.blit(pos_surface, (100, y_position))
            
            # Nombre
            name_text = record["name"]
            name_surface = record_font.render(name_text, True, color)
            screen.blit(name_surface, (150, y_position))
            
            # Score
            score_text = f"{record['score']:,}"
            score_surface = record_font.render(score_text, True, color)
            score_rect = score_surface.get_rect()
            screen.blit(score_surface, (screen_width - score_rect.width - 100, y_position))
            
            y_position += 40
        
        # Instrucciones
        if not records:
            no_records_text = record_font.render("No records yet!", True, record_color)
            no_rect = no_records_text.get_rect(center=(screen_width//2, screen_height//2))
            screen.blit(no_records_text, no_rect)
        
        # Opciones de navegación
        y_position = screen_height - 120
        for i, option in enumerate(options):
            color = highlight_color if i == selected_option else button_color
            text = small_font.render(option["text"], True, color)
            text_rect = text.get_rect(center=(screen_width//2, y_position + i * 30))
            screen.blit(text, text_rect)
            
            # Indicador de selección
            if i == selected_option:
                indicator_text = ">"
                indicator_surface = small_font.render(indicator_text, True, highlight_color)
                indicator_rect = indicator_surface.get_rect(center=(screen_width//2 - 80, y_position + i * 30))
                screen.blit(indicator_surface, indicator_rect)
        
        # Instrucciones
        instructions = [
            "Use ARROW KEYS to navigate",
            "Press ENTER to select",
            "Press ESC to go back"
        ]
        
        for i, instruction in enumerate(instructions):
            instruction_surface = small_font.render(instruction, True, record_color)
            instruction_rect = instruction_surface.get_rect(center=(screen_width//2, screen_height - 50 + i * 20))
            screen.blit(instruction_surface, instruction_rect)
        
        pygame.display.flip() 