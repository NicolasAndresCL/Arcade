import pygame
from entities.player import Player
from entities.enemy import Enemy
from screens.game_over import show_game_over
from services.score import update_score
from services.difficulty import get_difficulty

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    screen_width, screen_height = 640, 480
    player = Player(300, 400, screen_width, screen_height)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    game_state = {
        "running": True,
        "game_over": False,
        "score": 0
    }

    spawn_timer = 0  # 🕒 Temporizador para ritmo de enemigos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if game_state["running"]:
            screen.fill((30, 30, 30))

            # 🎚️ Dificultad basada en puntaje
            difficulty = get_difficulty(game_state["score"])
            max_enemies = difficulty["max_enemies"]
            min_speed = difficulty["min_speed"]
            max_speed = difficulty["max_speed"]

            # 🧠 Actualización de entidades
            all_sprites.update()

            # 💥 Detectar colisiones
            if pygame.sprite.spritecollideany(player, enemies):
                game_state["running"] = False
                game_state["game_over"] = True

            # 🧹 Eliminar enemigos fuera de pantalla
            for enemy in enemies:
                if enemy.rect.top > 480:
                    enemy.kill()

            # ⏱️ Spawn escalado según dificultad
            spawn_timer += 20
            if spawn_timer >= 4:
                if len(enemies) < max_enemies:
                    enemy = Enemy(640, min_speed, max_speed, difficulty["color"])
                    enemies.add(enemy)
                    all_sprites.add(enemy)
                spawn_timer = 0

            # 📈 Puntaje por supervivencia
            update_score(game_state, amount=1)

            # 🎨 Dibujar sprites y puntaje
            all_sprites.draw(screen)
            score_font = pygame.font.SysFont(None, 32)
            score_text = score_font.render(f"Score: {game_state['score']}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)

        elif game_state["game_over"]:
            show_game_over(screen, game_state["score"])
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # 🔄 Reiniciar juego completo
                game_state.update({
                    "running": True,
                    "game_over": False,
                    "score": 0
                })
                enemies.empty()
                all_sprites.empty()
                player = Player(300, 400, screen_width, screen_height)
                all_sprites.add(player)
                spawn_timer = 0

        clock.tick(60)
