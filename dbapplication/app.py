from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoid warnings

    db.init_app(app)
    
    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    print("✅ Flask app created successfully and routes registered!")  # Debugging message

    return app