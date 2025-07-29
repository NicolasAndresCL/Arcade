import asyncio
import pygame
import os
from entities.player import Player
from entities.enemy import Enemy
from screens.game_over import show_game_over
from screens.pause import show_pause_screen
from services.score import update_score
from services.difficulty import get_difficulty
from core.background import UniverseBackground

# Carga de fuente embebida
FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")

async def run_game():
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    screen_width, screen_height = screen.get_size()

    # Inicialización de jugador y grupos de sprites
    player = Player(300, 400, screen_width, screen_height)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)
    
    # Inicializar fondo tipo universo
    background = UniverseBackground(screen_width, screen_height)

    # Estado del juego
    game_state = {
        "running": True,
        "game_over": False,
        "score": 0
    }

    spawn_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Disparar
                    bullet = player.shoot()
                    if bullet:
                        bullets.add(bullet)
                        all_sprites.add(bullet)
                elif event.key == pygame.K_RETURN:
                    # Pausar juego
                    pause_action = show_pause_screen(screen)
                    if pause_action == "menu":
                        return "menu"
                    elif pause_action == "exit":
                        pygame.quit()
                        return "exit"

        if game_state["running"]:
            # Actualizar y dibujar fondo tipo universo
            background.update()
            background.draw(screen)

            # Dificultad dinámica
            difficulty = get_difficulty(game_state["score"])
            max_enemies = difficulty["max_enemies"]
            min_speed = difficulty["min_speed"]
            max_speed = difficulty["max_speed"]

            # Actualizar sprites
            all_sprites.update()

            # Colisión jugador-enemigo
            if pygame.sprite.spritecollideany(player, enemies):
                game_state["running"] = False
                game_state["game_over"] = True
                
            # Colisión balas-enemigos
            for bullet in bullets:
                enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
                if enemies_hit:
                    bullet.kill()
                    # Sumar 100 puntos por cada enemigo eliminado
                    game_state["score"] += len(enemies_hit) * 100

            # Eliminar enemigos fuera de pantalla
            for enemy in enemies:
                if enemy.rect.top > screen_height:
                    enemy.kill()

            # Generación de enemigos
            spawn_timer += 60
            if spawn_timer >= 120:  # Cambiado de 60 a 120 para menos enemigos
                if len(enemies) < max_enemies:
                    new_enemy = Enemy(screen_width, min_speed, max_speed, difficulty["color"])
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                spawn_timer = 0

            # Actualizar score (solo por tiempo, los puntos por enemigos se suman en la colisión)
            update_score(game_state, amount=1)

            # Dibujar sprites y score
            all_sprites.draw(screen)
            try:
                score_font = pygame.font.Font(FONT_PATH, 16)
            except:
                score_font = pygame.font.SysFont(None, 16)

            score_text = score_font.render(f"Score: {game_state['score']}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()

        elif game_state["game_over"]:
            show_game_over(screen, game_state["score"])

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # Reiniciar juego
                game_state.update({
                    "running": True,
                    "game_over": False,
                    "score": 0
                })
                enemies.empty()
                bullets.empty()
                all_sprites.empty()
                player = Player(300, 400, screen_width, screen_height)
                all_sprites.add(player)
                spawn_timer = 0
                # Reiniciar fondo
                background = UniverseBackground(screen_width, screen_height)

        clock.tick(60)
        await asyncio.sleep(0)  # 👈 Necesario para Pygbag (no lo saques)
    
    return "menu"  # Retornar al menú cuando termine el juego

