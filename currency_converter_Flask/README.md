# Currency Converter Web Application

A Python-based currency conversion application using Flask and a custom currency converter class. Exchange rates are fetched from the Czech National Bank (CNB) API.



## Requirements

- Python 3.8+
- pip (Python package installer) 

    or 
- poetry (Python dependency manager)

## Installation

### Using a Virtual Environment

**1. Create a virtual environment:**

	python -m venv venv

**2. Activate the virtual environment:**

- On Windows:

		.\venv\Scripts\activate

- On macOS/Linux:

		source venv/bin/activate

**3. Install dependencies:**

	pip install -r requirements.txt
---

### Using Poetry

**1. Install Poetry:**

	pip install poetry

**2. Install dependencies:**

	poetry install

## Running the Application

**1. Start the Flask application**

- With a virtual environment:

		python app.py


- With Poetry:

		poetry run python app.py

**2. Open your browser and navigate to** http://127.0.0.1:5000

        
## License

This project is licensed under the MIT License. See the LICENSE file for details.
