# Currency Converter

Currency Converter is a Python-based application for converting between different currencies. It includes both a standalone application for macOS and a Python script for cross-platform use.

## Features

- Convert between various currencies using real-time exchange rates.
- Graphical User Interface (GUI) built with Tkinter.
- macOS-compatible `.dmg` file for easy installation.
- Supports running on Windows, macOS, and Linux using Python.

---

## Note
 On mac, if you do not want to bother with python files skip to **USAGE -> Option 1**

## Requirements

- Python 3.8 or higher.
- Tkinter (included by default in Python installations for macOS and Windows).
- The dependencies listed in `requirements.txt`.

---

## Installation

### 1. Install Python
Ensure Python 3.8+ is installed on your system. Download it from the official Python website: [Python.org](https://www.python.org/).

### 2. Install Tkinter (if not already installed)
Tkinter is often included with Python, but if it’s missing:
- **Windows/Mac**: Reinstall Python and ensure "Tkinter" is checked in the installation options.

- **Linux**: Install Tkinter via your package manager:

        sudo apt-get install python3-tk
  
3. Create a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies:

1. Create the virtual environment:
   
        python -m venv venv
or
        python3 -m venv venv

3. Activate the virtual environment:

- Windows:

        .\venv\Scripts\activate

- macOS/Linux:
  
        source venv/bin/activate

4. Install Dependencies

With the virtual environment activated, install the required packages:

        pip install -r requirements.txt


## Usage

Option 1: Using the macOS .dmg File

1. Download the Currency Converter.dmg file.
2. Open the .dmg file and drag the application to your Applications folder.
3. Run the application from the Applications folder.

Option 2: Running the Python Script (terminal mac os and windows)

1. Clone repository from github or downlod .zip file
2. Navigate to the directory containing the app.py file.
2. Ensure the virtual environment is activated and requirements installed.
3. Run the script:

        python app.py

## License

This project is licensed under the MIT License. See the LICENSE file for details.
