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
    Progresión cada 500 puntos para mayor estabilidad.
    """
    if score < 500:
        return {"max_enemies": 8, "min_speed": 2, "max_speed": 4, "color": get_random_color()}
    elif score < 1000:
        return {"max_enemies": 15, "min_speed": 3, "max_speed": 6, "color": get_random_color()}
    elif score < 1500:
        return {"max_enemies": 22, "min_speed": 4, "max_speed": 8, "color": get_random_color()}
    elif score < 2000:
        return {"max_enemies": 28, "min_speed": 5, "max_speed": 10, "color": get_random_color()}
    elif score < 2500:
        return {"max_enemies": 35, "min_speed": 6, "max_speed": 12, "color": get_random_color()}
    elif score < 3000:
        return {"max_enemies": 42, "min_speed": 7, "max_speed": 14, "color": get_random_color()}
    elif score < 3500:
        return {"max_enemies": 48, "min_speed": 8, "max_speed": 16, "color": get_random_color()}
    elif score < 4000:
        return {"max_enemies": 55, "min_speed": 9, "max_speed": 18, "color": get_random_color()}
    elif score < 4500:
        return {"max_enemies": 62, "min_speed": 10, "max_speed": 20, "color": get_random_color()}
    else:
        return {"max_enemies": 70, "min_speed": 12, "max_speed": 22, "color": get_random_color()}
