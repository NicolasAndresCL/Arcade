import random

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def get_difficulty(score):
    """
    Retorna la configuración de dificultad según el puntaje y color aleatorio.
    Progresión cada 500 puntos hasta 100,000.
    """
    # Valores base
    base_enemies = 8
    base_min_speed = 2
    base_max_speed = 4
    # Cada 500 puntos aumenta la dificultad
    level = min(score // 500, 184)  # 100,000 // 500 = 200, pero limitamos a 184 para no pasar de 100,000
    max_enemies = base_enemies + level * 2  # Sube 2 enemigos por nivel
    min_speed = base_min_speed + level // 10  # Sube 1 cada 10 niveles
    max_speed = base_max_speed + level // 5   # Sube 1 cada 5 niveles
    # Limitar máximos razonables
    max_enemies = min(max_enemies, 200)
    min_speed = min(min_speed, 40)
    max_speed = min(max_speed, 60)
    return {
        "max_enemies": max_enemies,
        "min_speed": min_speed,
        "max_speed": max_speed,
        "color": get_random_color()
    }
