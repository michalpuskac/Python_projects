# Rock Paper Scissors Game

This is a command-line **Rock, Paper, Scissors** game built in Python. It uses the [colorama](https://pypi.org/project/colorama/) library for colorful terminal output and [pyfiglet](https://pypi.org/project/pyfiglet/) for generating stylized text. The project is organized into modules to promote maintainability and scalability, and it includes automated tests using [pytest](https://pypi.org/project/pytest/).

## Features

- **Interactive Gameplay:** Play Rock, Paper, Scissors with an engaging CLI interface.
- **Visual Enhancements:** Enjoy dynamic ASCII art and colorized output.
- **Modular Structure:** Separation of game logic, entry point, and tests.
- **Automated Testing:** Ensured quality with tests covering key functionalities.

## Project Structure

```
    rock_pape_scissors/
    ├── src/
    │   ├── init.py                # Makes the src directory a package.
    │   ├── game.py                # Handles whole game logic.
    │   └── main.py                # Main entry point - running the game.
    ├── tests/
    |   ├── init.py                # Makes the tests directory a package.
    │   ├── test_game.py           # Pytest tests for game module.
    └── requirements.txt           # Project dependencies.
```

## Requirements

- Python 3.8+
- pip (Python package installer) 

    or 
- poetry (Python dependency manager)


## Installation

1. **Clone the repository:**
```bash
    git clone <https://github.com/michalpuskac/Python_projects.git>
    cd password_manager
```

2.	Set up a virtual environment (optional but recommended):
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.	Install the required dependencies:
```bash
    pip install -r requirements.txt
```

### Using Poetry
1. **Install Poetry:**
```bash
    pip install poetry
```

2. **Install dependencies:**
```bash
    poetry install
```

---
## Usage
1. **Poetry**
```bash
    poetry run python src/main.py
```

2. OR **Virtual enviroment**
```bash
    python src/main.py
```

The application will show base menu with instruction how to select or quit and prompt you for your choice of Rock/ Paper or Scissors. After your step computer will choose one by random and after immediate comparing will display result win/ lose or tie.

## Running tests
```bash
    # In virtual enviroment
    pytest tests/

    # In poetry navigate firt to tests folder
    cd tests
    poetry run pytest .
```

This command will discover and run all tests in the tests/ directory.


## Dependencies

 - [pyfiglet](https://pypi.org/project/pyfiglet/): For generating a stylized ASCII art banner.
 - [colorama](https://pypi.org/project/colorama/): For colorful terminal text.
 - [pytest](https://pypi.org/project/pytest/): For running the test suite.

All dependencies are listed in the requirements.txt or pyproject  file.

## License
This project is licensed under the MIT License.Feel free to use, modify, and distribute this application as per the terms of the license.

## Author - Michal Puškáč

This project is part of my portfolio, showcasing the basic python skills and concepts. If you have any questions, feedback, or would like to collaborate, feel free to get in touch!

---
- **LinkedIn**:(linkedin.com/in/michal-puškáč-94b925179)
- **GitHub**: (github.com/michalpuskac)

---