# Flask Application

This repository contains a Flask-based web application demonstrating the use of blueprints, database integration with SQLAlchemy, and a modular project structure.

## Features

Blueprints: Modular organization of routes for scalability.

SQLAlchemy: Integration with a relational database for data management.

Migrations: Database schema migrations using Flask-Migrate.

## Project Structure

The project is organized as follows:

flask/
│── blueprintapp/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── blueprints/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   ├── templates/
│   │   │   │   ├── core/
│   │   │   │   │   ├── index.html
│   │   ├── people/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   ├── templates/
│   │   │   │   ├── people/
│   │   │   │   │   ├── index.html
│   │   │   │   │   ├── create.html
│   │   ├── todos/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       ├── templates/
│   │           ├── todos/
│   │               ├── index.html
├── dbapplication/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── templates/
│       ├── index.html
├── instance/
│   ├── config.py
├── migrations/
├── .DS_Store
├── README.md
├── requirements.txt
├── run.py

* blueprintapp/: Contains the main Flask application utilizing blueprints for modular routing.

* dbapplication/: Another Flask application focusing on direct database interactions.

* instance/: Holds configuration files and instance-specific settings.

* migrations/: Directory for database migration files managed by Flask-Migrate.

* run.py: Script to run the Flask application.

## Setup Instructions

* Clone the Repository:
```
git clone https://github.com/AkibDa/flask.git
cd flask
```
* Create and Activate a Virtual Environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
* Install Dependencies:
```
pip install -r requirements.txt
```
8 Set Environment Variables:

For Linux/Mac:
```
export FLASK_APP=run.py
export FLASK_ENV=development
```
For Windows:
```
set FLASK_APP=run.py
set FLASK_ENV=development
```
* Initialize the Database:
```
flask db upgrade
```
* Run the Application:
```
flask run
```
* The application will be accessible at http://127.0.0.1:5000/.

## Notes

Ensure that the database configurations in config.py are set correctly before initializing the database.

To create new database migrations after modifying models:
```
flask db migrate -m "Description of changes"
flask db upgrade
```
## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Sk Akib Ahammed [ahammedskakib@gmail.com]
