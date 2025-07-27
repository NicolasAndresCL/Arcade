# 🕹️ Mi Juego en Pygame – Skeleton Modular y Escalable

Proyecto base para un juego en Pygame con estructura modular, versionado profesional en Git, y documentación clara para escalar funcionalidades y presentar en portafolio.

---

## 📦 Instalación

```bash
# Clona el repositorio
git clone https://github.com/usuario/mi-juego-pygame.git
cd mi-juego-pygame

# Crea y activa el entorno virtual
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el juego
python main.py
```
## 🔧 Estructura del Proyecto
```
Arcade/
├── core/              # Lógica de juego principal (render, eventos, loop)
├── entities/          # Clases de objetos del juego (jugador, enemigos, proyectiles)
├── env/               # Entorno virtual (no versionar en Git, usar .gitignore)
├── services/          # Funciones auxiliares: colisiones, puntaje, sonidos, etc.
├── main.py            # Punto de entrada del juego, inicia todo el flujo
├── settings.py        # Configuraciones globales: tamaño pantalla, FPS, colores
├── requirements.txt   # Librerías necesarias como pygame
├── .gitignore         # Archivos ignorados por git
```
✔️ Separación por componentes ✔️ Modularidad para mantenimiento ✔️ Preparado para expansión (menús, niveles, AI)

## 🚀 Features
Movimiento fluido del personaje principal 🧍

Detección básica de colisiones 💥

Renderizado de sprites 📸

Estructura lista para niveles y menú de inicio 🗺️

## 💡 Futuras mejoras
[ ] Música de fondo y efectos 🎶

[ ] Sistema de puntaje 🧮

[ ] Niveles progresivos 🚧

[ ] Menú de inicio / pausa 🛑

[ ] Integración con base de datos para scores 🗃️

## 📄 Licencia
Este proyecto se distribuye bajo la licencia MIT. Ver el archivo LICENSE para más detalles.