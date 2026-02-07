# ☄️ A Python Asteroid Game
A classic asteroid game built with Python and Pygame, where you navigate through an asteroid field, shooting incoming asteroids and surviving as long as possible.


## 🛠️ Requirements
- **Python**: 3.13 (Note: Developed with a pre-release version of Python 3.13. You may use Python 3.9 - 3.12 with compatible Pygame versions.)
- **package manager**: uv(recommended) or pip
- **Dependencies**: pygame==2.6.1

## 📦 Installation

### Using uv (Recommended)
if you have uv installed, the dependencies will be automatically managed:
```bash
# First clone or download the repository
git clone https://github.com/ProgrammerVenerable/AsteroidsGame
cd AsteroidsGame/

# Run the game (uv will handle dependencies automatically)
uv run main.py
```

If you don't have `uv`, you can install it globally with:
 ```bash
 # If you have pipx installed:
 pipx install uv
 # Or, using pip (might require admin/sudo for global install):
 pip install uv
 ```

### Using pip
If you prefer using pip:

```bash
# Clone or download the repository
git clone https://github.com/ProgrammerVenerable/AsteroidsGame
cd AsteroidsGame/

#It is recommended to use a Python virtual environment for managing dependencies.
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

# Run the game
python main.py
```

## 🎯 Controls
- **W** / **S**: Move forward / backward
- **A** / **D**: Rotate left / right
- **SPACE**: Shoot
- **Close Window**: Exit the game

## Game Features

- **Background**: A black game window will open (1280x720 pixels)
- **Asteroid Spawning**: Asteroids continuously spawn from random edges of the screen
- **Asteroid Splitting**: When shot, large asteroids split into medium ones and  medium ones to small, then gets destroyed when shot at small
- **Collision Detection**: Circle-based collision detection for ship-asteroid and shot-asteroid interactions
- **Shooting Cooldown**: There's a 0.3 second cooldown between shots to prevent spam
- **Scoring System**: earn points for destroying asteroids, high score is saved across sessions
- **Logging**: The game logs state and events to JSONL files (`game_state.jsonl` and `game_events.jsonl`) for the first 16 seconds of gameplay
- **FPS**: The game runs at 60 FPS for smooth gameplay

## 📸 Gameplay

![Gameplay](assets/screenshots/gameplay.gif)

## 📁 Project Structure

- `main.py` - Main game loop and entry point
- `player.py` - Player ship class with movement and shooting mechanics
- `asteroid.py` - Asteroid class with splitting behavior
- `asteroidfield.py` - Manages asteroid spawning from screen edges
- `shot.py` - Projectile class for player shots
- `circleshape.py` - Base class for circular game objects with collision detection
- `constants.py` - Game configuration constants (screen size, speeds, etc.)
- `logger.py` - Game state and event logging system
- `score.py` - Score functions that help with updating and checking score
- `data/score.txt` - Stores the highscore
- `pyproject.toml` - Project configuration and dependencies

## 🚧 Future Improvements

- Implement multiple lives and respawning
- Add a background image
- Add an explosion effect for the asteroids
- Add acceleration to the player movement

## Changelog

- v0.2 - Added scoring system with high score tracking
