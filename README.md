# 🕹️ Space Shooter Arcade – Modular, Escalable y Profesional

Proyecto base para un juego arcade en Pygame con estructura modular, sistema de menús, records, dificultad progresiva, efectos visuales y sonoros, y documentación clara para escalar funcionalidades y presentar en portafolio.

---

## 📦 Instalación

```bash
# Clona el repositorio
https://github.com/usuario/mi-juego-pygame.git
cd mi-juego-pygame

# Crea y activa el entorno virtual
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate   # Windows

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el juego
python main.py
```

## 🔧 Estructura del Proyecto
```
Arcade/
├── core/              # Lógica de juego principal (render, eventos, loop, engine)
├── entities/          # Clases de objetos del juego (jugador, enemigos, proyectiles, explosiones)
├── screens/           # Pantallas: menú, pausa, records, game over, entrada de nombre
├── services/          # Funciones auxiliares: dificultad, puntaje, records, spawn
├── assets/            # Recursos: sonidos, fuentes, imágenes
├── main.py            # Punto de entrada del juego, inicia todo el flujo
├── requirements.txt   # Librerías necesarias como pygame
├── settings.py        # Configuraciones globales
├── .gitignore         # Archivos ignorados por git
```
✔️ Separación por componentes ✔️ Modularidad para mantenimiento ✔️ Preparado para expansión (niveles, AI, power-ups)

## 🚀 Features
- Menú principal interactivo (Jugar, Records, Salir)
- Sistema de pausa (ENTER)
- Sistema de records con entrada de nombre (máx 10 caracteres)
- Dificultad progresiva hasta 100,000 puntos
- Bombas: obtén una bomba cada 1000 puntos y úsala con SHIFT para eliminar enemigos en área
- Explosiones animadas al destruir enemigos
- Efectos de sonido: disparo, destrucción, explosión
- Movimiento fluido y controles intuitivos
- Guardado y visualización de records (top 5)
- Reinicio y navegación fluida entre pantallas

## 🎮 Controles
- **Flechas**: Mover nave
- **Espacio**: Disparar
- **SHIFT**: Usar bomba
- **ENTER**: Pausa / Selección en menús
- **ESC**: Volver / Salir de menús
- **R**: Ver records en game over
- **Arriba/Abajo**: Navegar menús

## 💥 Efectos y Sonidos
- Explosiones animadas al destruir enemigos
- Sonido de disparo, destrucción y bomba (coloca archivos .wav en assets/)

## 🏆 Sistema de Records
- Ingresa tu nombre si logras un high score (máx 10 caracteres)
- Se guardan los 5 mejores puntajes
- Visualización de records desde el menú o game over

## 🗺️ Futuras mejoras
- [ ] Música de fondo
- [ ] Power-ups adicionales
- [ ] Niveles y jefes
- [ ] Integración con base de datos online
- [ ] Skins para la nave y enemigos

## 📄 Licencia
Este proyecto se distribuye bajo la licencia MIT. Ver el archivo LICENSE para más detalles.