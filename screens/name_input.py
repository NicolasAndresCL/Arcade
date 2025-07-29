import pygame
import os

FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")
MAX_NAME_LENGTH = 10

def get_player_name(screen, score):
    """Pantalla para ingresar nombre del jugador"""
    player_name = ""
    cursor_visible = True
    cursor_timer = 0
    
    # Cargar fuentes
    try:
        title_font = pygame.font.Font(FONT_PATH, 20)
        input_font = pygame.font.Font(FONT_PATH, 16)
        small_font = pygame.font.Font(FONT_PATH, 12)
    except:
        title_font = pygame.font.SysFont(None, 28)
        input_font = pygame.font.SysFont(None, 24)
        small_font = pygame.font.SysFont(None, 18)
    
    # Colores
    title_color = (255, 255, 255)
    input_color = (255, 255, 255)
    cursor_color = (255, 255, 0)
    score_color = (255, 215, 0)
    
    screen_width, screen_height = screen.get_size()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name.strip():
                        return player_name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return None
                elif len(player_name) < MAX_NAME_LENGTH:
                    # Solo permitir letras, números y espacios
                    if event.unicode.isalnum() or event.unicode == ' ':
                        player_name += event.unicode
        
        # Actualizar cursor
        cursor_timer += 1
        if cursor_timer >= 60:  # Cambiar cada 60 frames (1 segundo) - más lento
            cursor_visible = not cursor_visible
            cursor_timer = 0
        
        # Fondo
        screen.fill((0, 0, 20))
        
        # Título
        title_text = title_font.render("NEW HIGH SCORE!", True, title_color)
        title_rect = title_text.get_rect(center=(screen_width//2, 100))
        screen.blit(title_text, title_rect)
        
        # Mostrar score
        score_text = f"Score: {score:,}"
        score_surface = title_font.render(score_text, True, score_color)
        score_rect = score_surface.get_rect(center=(screen_width//2, 150))
        screen.blit(score_surface, score_rect)
        
        # Instrucciones
        instruction_text = "Enter your name:"
        instruction_surface = input_font.render(instruction_text, True, input_color)
        instruction_rect = instruction_surface.get_rect(center=(screen_width//2, 220))
        screen.blit(instruction_surface, instruction_rect)
        
        # Campo de entrada
        input_text = player_name
        if cursor_visible:
            input_text += "|"
        
        input_surface = input_font.render(input_text, True, input_color)
        input_rect = input_surface.get_rect(center=(screen_width//2, 280))
        screen.blit(input_surface, input_rect)
        
        # Dibujar un rectángulo de fondo para estabilizar el texto
        text_width = input_font.render(player_name + " ", True, input_color).get_width()
        background_rect = pygame.Rect(screen_width//2 - text_width//2 - 5, 280 - 15, text_width + 10, 30)
        pygame.draw.rect(screen, (0, 0, 20), background_rect)
        
        # Redibujar el texto sobre el fondo
        screen.blit(input_surface, input_rect)
        
        # Límite de caracteres
        limit_text = f"Max {MAX_NAME_LENGTH} characters"
        limit_surface = small_font.render(limit_text, True, input_color)
        limit_rect = limit_surface.get_rect(center=(screen_width//2, 320))
        screen.blit(limit_surface, limit_rect)
        
        # Instrucciones
        enter_text = "Press ENTER to save"
        enter_surface = small_font.render(enter_text, True, input_color)
        enter_rect = enter_surface.get_rect(center=(screen_width//2, 380))
        screen.blit(enter_surface, enter_rect)
        
        esc_text = "Press ESC to skip"
        esc_surface = small_font.render(esc_text, True, input_color)
        esc_rect = esc_surface.get_rect(center=(screen_width//2, 410))
        screen.blit(esc_surface, esc_rect)
        
        pygame.display.flip() 