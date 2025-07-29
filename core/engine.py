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
    explosions = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)
    
    # Inicializar fondo tipo universo
    background = UniverseBackground(screen_width, screen_height)

    # Estado del juego
    game_state = {
        "running": True,
        "game_over": False,
        "score": 0,
        "bombs": 0,
        "next_bomb_score": 1000
    }

    spawn_timer = 0

    # Cargar sonidos
    try:
        shoot_sound = pygame.mixer.Sound(os.path.join("assets", "shoot.wav"))
        destroy_sound = pygame.mixer.Sound(os.path.join("assets", "enemy_destroyed.wav"))
        explosion_sound = pygame.mixer.Sound(os.path.join("assets", "explosion.wav"))
    except Exception as e:
        shoot_sound = destroy_sound = explosion_sound = None

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
                        if shoot_sound:
                            shoot_sound.play()
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    # Usar bomba
                    if game_state["bombs"] > 0:
                        # Eliminar enemigos en radio de 300
                        player_center = player.rect.center
                        bomba_usada = False
                        for enemy in list(enemies):
                            if (enemy.rect.centerx - player_center[0]) ** 2 + (enemy.rect.centery - player_center[1]) ** 2 <= 300 ** 2:
                                from entities.explosion import Explosion
                                explosions.add(Explosion(enemy.rect.centerx, enemy.rect.centery, color=(255,80,80), max_radius=40, duration=18))
                                enemy.kill()
                                bomba_usada = True
                        if bomba_usada and explosion_sound:
                            explosion_sound.play()
                        game_state["bombs"] -= 1
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
                    for enemy in enemies_hit:
                        from entities.explosion import Explosion
                        explosions.add(Explosion(enemy.rect.centerx, enemy.rect.centery, color=(255,200,50), max_radius=24, duration=14))
                    if destroy_sound:
                        destroy_sound.play()
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

            # Ganar bomba solo cuando el score alcanza el siguiente múltiplo de 1000
            if game_state["score"] >= game_state["next_bomb_score"]:
                game_state["bombs"] += 1
                game_state["next_bomb_score"] += 1000

            # Dibujar sprites y score
            all_sprites.draw(screen)
            try:
                score_font = pygame.font.Font(FONT_PATH, 16)
            except:
                score_font = pygame.font.SysFont(None, 16)

            score_text = score_font.render(f"Score: {game_state['score']}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            # Mostrar bombas
            bomb_text = score_font.render(f"Bombs: {game_state['bombs']}", True, (255, 255, 0))
            screen.blit(bomb_text, (10, 30))

            # Actualizar y dibujar explosiones
            explosions.update()
            explosions.draw(screen)

            pygame.display.flip()

        elif game_state["game_over"]:
            result = show_game_over(screen, game_state["score"])
            if result == "exit":
                return "exit"

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # Reiniciar juego
                game_state.update({
                    "running": True,
                    "game_over": False,
                    "score": 0,
                    "bombs": 0,
                    "next_bomb_score": 1000
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

