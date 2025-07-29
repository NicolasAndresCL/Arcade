import asyncio
import pygame
from core.engine import run_game
from screens.main_menu import show_main_menu

async def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Space Shooter")
    
    while True:
        # Mostrar menú principal
        action = show_main_menu(screen)
        
        if action == "play":
            # Iniciar juego
            game_result = await run_game()
            if game_result == "exit":
                break
        elif action == "records":
            # Mostrar records
            records_result = show_records(screen)
            if records_result == "exit":
                break
        elif action == "exit":
            break
    
    pygame.quit()

asyncio.run(main())
