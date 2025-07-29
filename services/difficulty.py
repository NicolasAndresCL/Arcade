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
    Progresión más gradual y suave.
    """
    if score < 50:
        return {"max_enemies": 5, "min_speed": 1, "max_speed": 3, "color": get_random_color()}
    elif score < 100:
        return {"max_enemies": 8, "min_speed": 2, "max_speed": 4, "color": get_random_color()}
    elif score < 200:
        return {"max_enemies": 12, "min_speed": 2, "max_speed": 5, "color": get_random_color()}
    elif score < 300:
        return {"max_enemies": 15, "min_speed": 3, "max_speed": 6, "color": get_random_color()}
    elif score < 400:
        return {"max_enemies": 18, "min_speed": 3, "max_speed": 7, "color": get_random_color()}
    elif score < 500:
        return {"max_enemies": 22, "min_speed": 4, "max_speed": 8, "color": get_random_color()}
    elif score < 600:
        return {"max_enemies": 25, "min_speed": 4, "max_speed": 9, "color": get_random_color()}
    elif score < 700:
        return {"max_enemies": 28, "min_speed": 5, "max_speed": 10, "color": get_random_color()}
    elif score < 800:
        return {"max_enemies": 32, "min_speed": 5, "max_speed": 11, "color": get_random_color()}
    elif score < 900:
        return {"max_enemies": 35, "min_speed": 6, "max_speed": 12, "color": get_random_color()}
    elif score < 1000:
        return {"max_enemies": 40, "min_speed": 6, "max_speed": 13, "color": get_random_color()}
    elif score < 1200:
        return {"max_enemies": 45, "min_speed": 7, "max_speed": 14, "color": get_random_color()}
    elif score < 1400:
        return {"max_enemies": 50, "min_speed": 8, "max_speed": 15, "color": get_random_color()}
    elif score < 1600:
        return {"max_enemies": 55, "min_speed": 9, "max_speed": 16, "color": get_random_color()}
    elif score < 1800:
        return {"max_enemies": 60, "min_speed": 10, "max_speed": 17, "color": get_random_color()}
    else:
        return {"max_enemies": 65, "min_speed": 11, "max_speed": 18, "color": get_random_color()}
