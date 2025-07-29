import asyncio
import pygame
import os

# Inicialización recomendada del mixer antes de pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

from entities.player import Player
from entities.enemy import Enemy
from screens.game_over import show_game_over
from screens.pause import show_pause_screen
from services.score import update_score
from services.difficulty import get_difficulty
from core.background import UniverseBackground
from entities.explosion import Explosion  # ✅ Importar antes para evitar import dinámico

FONT_PATH = os.path.join("assets", "PressStart2P-Regular.ttf")

def load_sound(name, volume=1.0):
    try:
        sound = pygame.mixer.Sound(os.path.join("assets", name))
        sound.set_volume(volume)
        return sound
    except Exception as e:
        print(f"Error cargando {name}: {e}")
        return None

async def run_game():
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    screen_width, screen_height = screen.get_size()

    # Música de fondo
    try:
        pygame.mixer.music.load(os.path.join("assets", "universe.wav"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"No se pudo cargar música de fondo: {e}")

    # Jugador y sprites
    player = Player(300, 400, screen_width, screen_height)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    background = UniverseBackground(screen_width, screen_height)

    game_state = {
        "running": True,
        "game_over": False,
        "score": 0,
        "bombs": 0,
        "next_bomb_score": 1000
    }

    spawn_timer = 0

    # Sonidos
    shoot_sound = load_sound("shoot.wav")
    destroy_sound = load_sound("enemy_destroyed.wav")
    explosion_sound = load_sound("explosion.wav")
    player_dead_sound = load_sound("player_dead.wav")  # 🔁 Corregido nombre

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets_fired = player.shoot()
                    if bullets_fired:
                        for bullet in bullets_fired:
                            bullets.add(bullet)
                            all_sprites.add(bullet)
                        if shoot_sound:
                            shoot_sound.play()
                elif event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                    if game_state["bombs"] > 0:
                        used = False
                        px, py = player.rect.center
                        for enemy in list(enemies):
                            ex, ey = enemy.rect.center
                            if (ex - px)**2 + (ey - py)**2 <= 300**2:
                                explosions.add(Explosion(ex, ey, color=(255,80,80), max_radius=40, duration=18))
                                enemy.kill()
                                used = True
                        if used and explosion_sound:
                            explosion_sound.play()
                        game_state["bombs"] -= 1
                elif event.key == pygame.K_RETURN:
                    pause_action = show_pause_screen(screen)
                    if pause_action == "menu":
                        return "menu"
                    elif pause_action == "exit":
                        pygame.quit()
                        return "exit"

        if game_state["running"]:
            background.update()
            background.draw(screen)

            difficulty = get_difficulty(game_state["score"])
            max_enemies = difficulty["max_enemies"]
            min_speed = difficulty["min_speed"]
            max_speed = difficulty["max_speed"]

            all_sprites.update()

            if pygame.sprite.spritecollideany(player, enemies):
                game_state["running"] = False
                game_state["game_over"] = True
                if player_dead_sound:
                    player_dead_sound.play()

            for bullet in bullets:
                hits = pygame.sprite.spritecollide(bullet, enemies, True)
                if hits:
                    bullet.kill()
                    for enemy in hits:
                        explosions.add(Explosion(enemy.rect.centerx, enemy.rect.centery, color=(255,200,50), max_radius=24, duration=14))
                    if destroy_sound:
                        destroy_sound.play()
                    game_state["score"] += len(hits) * 100

            for enemy in enemies:
                if enemy.rect.top > screen_height:
                    enemy.kill()

            spawn_timer += 500
            if spawn_timer >= 500:
                if len(enemies) < max_enemies:
                    new_enemy = Enemy(screen_width, min_speed, max_speed, difficulty["color"])
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                spawn_timer = 0

            update_score(game_state, amount=1)

            if game_state["score"] >= game_state["next_bomb_score"]:
                game_state["bombs"] += 1
                game_state["next_bomb_score"] += 1000

            all_sprites.draw(screen)

            try:
                score_font = pygame.font.Font(FONT_PATH, 16)
            except:
                score_font = pygame.font.SysFont(None, 16)

            score_text = score_font.render(f"Score: {game_state['score']}", True, (255, 255, 255))
            bomb_text = score_font.render(f"Bombs: {game_state['bombs']}", True, (255, 255, 0))
            screen.blit(score_text, (10, 10))
            screen.blit(bomb_text, (10, 30))

            explosions.update()
            explosions.draw(screen)

            pygame.display.flip()

        elif game_state["game_over"]:
            result = show_game_over(screen, game_state["score"])
            if result == "exit":
                pygame.mixer.music.stop()
                return "exit"

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                game_state.update({
                    "running": True,
                    "game_over": False,
                    "score": 0,
                    "bombs": 0,
                    "next_bomb_score": 1000
                })
                enemies.empty()
                bullets.empty()
                explosions.empty()
                all_sprites.empty()
                player = Player(300, 400, screen_width, screen_height)
                all_sprites.add(player)
                spawn_timer = 0
                background = UniverseBackground(screen_width, screen_height)

        clock.tick(60)
        await asyncio.sleep(0)

    return "menu"
