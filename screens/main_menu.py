import pygame
import os
from screens.records import show_records

FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")

def show_main_menu(screen):
    """Muestra el menú principal del juego"""
    
    # Cargar fuentes
    try:
        title_font = pygame.font.Font(FONT_PATH, 32)
        menu_font = pygame.font.Font(FONT_PATH, 20)
        small_font = pygame.font.Font(FONT_PATH, 14)
    except:
        title_font = pygame.font.SysFont(None, 48)
        menu_font = pygame.font.SysFont(None, 32)
        small_font = pygame.font.SysFont(None, 24)
    
    # Colores
    title_color = (255, 255, 255)
    menu_color = (200, 200, 200)
    selected_color = (255, 215, 0)  # Dorado para opción seleccionada
    subtitle_color = (150, 150, 150)
    
    screen_width, screen_height = screen.get_size()
    
    # Opciones del menú
    menu_options = [
        {"text": "PLAY", "action": "play"},
        {"text": "HIGH SCORES", "action": "records"},
        {"text": "EXIT", "action": "exit"}
    ]
    
    selected_option = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    action = menu_options[selected_option]["action"]
                    if action == "records":
                        show_records(screen)
                    else:
                        return action
        
        # Fondo tipo universo
        screen.fill((0, 0, 20))
        
        # Título del juego
        title_text = title_font.render("SPACE SHOOTER", True, title_color)
        title_rect = title_text.get_rect(center=(screen_width//2, 100))
        screen.blit(title_text, title_rect)
        
        # Subtítulo
        subtitle_text = small_font.render("Arcade Game", True, subtitle_color)
        subtitle_rect = subtitle_text.get_rect(center=(screen_width//2, 140))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Opciones del menú
        menu_y = 250
        for i, option in enumerate(menu_options):
            color = selected_color if i == selected_option else menu_color
            text = menu_font.render(option["text"], True, color)
            text_rect = text.get_rect(center=(screen_width//2, menu_y + i * 60))
            screen.blit(text, text_rect)
            
            # Indicador de selección
            if i == selected_option:
                indicator_text = ">"
                indicator_surface = menu_font.render(indicator_text, True, selected_color)
                indicator_rect = indicator_surface.get_rect(center=(screen_width//2 - 100, menu_y + i * 60))
                screen.blit(indicator_surface, indicator_rect)
        
        # Instrucciones
        instructions = [
            "Use ARROW KEYS to navigate",
            "Press ENTER to select"
        ]
        
        for i, instruction in enumerate(instructions):
            instruction_surface = small_font.render(instruction, True, subtitle_color)
            instruction_rect = instruction_surface.get_rect(center=(screen_width//2, screen_height - 100 + i * 25))
            screen.blit(instruction_surface, instruction_rect)
        
        pygame.display.flip() 