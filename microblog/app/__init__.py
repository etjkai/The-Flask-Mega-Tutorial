from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Redirect users to login page
# Adds a query string argument to the URL, making the complete redirect URL /login?next=/index
login.login_view = "login"

# Routes (different URLs) will need to import app variable - used here to avoid circular imports
from app import routes, models, errors

