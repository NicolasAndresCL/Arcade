import pygame
import os

FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")

def show_pause_screen(screen):
    """Muestra la pantalla de pausa"""
    
    # Cargar fuentes
    try:
        title_font = pygame.font.Font(FONT_PATH, 28)
        menu_font = pygame.font.Font(FONT_PATH, 18)
        small_font = pygame.font.Font(FONT_PATH, 14)
    except:
        title_font = pygame.font.SysFont(None, 36)
        menu_font = pygame.font.SysFont(None, 28)
        small_font = pygame.font.SysFont(None, 20)
    
    # Colores
    title_color = (255, 255, 255)
    menu_color = (200, 200, 200)
    selected_color = (255, 215, 0)
    overlay_color = (0, 0, 0, 128)  # Semi-transparente
    
    screen_width, screen_height = screen.get_size()
    
    # Opciones de pausa
    pause_options = [
        {"text": "RESUME", "action": "resume"},
        {"text": "MAIN MENU", "action": "menu"},
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
                    selected_option = (selected_option - 1) % len(pause_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(pause_options)
                elif event.key == pygame.K_RETURN:
                    return pause_options[selected_option]["action"]
                elif event.key == pygame.K_ESCAPE:
                    return "resume"
        
        # Crear overlay semi-transparente
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Panel de pausa
        panel_width, panel_height = 400, 300
        panel_x = (screen_width - panel_width) // 2
        panel_y = (screen_height - panel_height) // 2
        
        # Fondo del panel
        panel = pygame.Surface((panel_width, panel_height))
        panel.fill((30, 30, 50))
        pygame.draw.rect(panel, (100, 100, 150), (0, 0, panel_width, panel_height), 3)
        screen.blit(panel, (panel_x, panel_y))
        
        # Título
        title_text = title_font.render("PAUSED", True, title_color)
        title_rect = title_text.get_rect(center=(screen_width//2, panel_y + 50))
        screen.blit(title_text, title_rect)
        
        # Opciones del menú
        menu_y = panel_y + 120
        for i, option in enumerate(pause_options):
            color = selected_color if i == selected_option else menu_color
            text = menu_font.render(option["text"], True, color)
            text_rect = text.get_rect(center=(screen_width//2, menu_y + i * 50))
            screen.blit(text, text_rect)
            
            # Indicador de selección
            if i == selected_option:
                indicator_text = ">"
                indicator_surface = menu_font.render(indicator_text, True, selected_color)
                indicator_rect = indicator_surface.get_rect(center=(screen_width//2 - 80, menu_y + i * 50))
                screen.blit(indicator_surface, indicator_rect)
        
        # Instrucciones
        instructions = [
            "Use ARROW KEYS to navigate",
            "Press ENTER to select",
            "Press ESC to resume"
        ]
        
        for i, instruction in enumerate(instructions):
            instruction_surface = small_font.render(instruction, True, menu_color)
            instruction_rect = instruction_surface.get_rect(center=(screen_width//2, panel_y + panel_height - 60 + i * 20))
            screen.blit(instruction_surface, instruction_rect)
        
        pygame.display.flip() 