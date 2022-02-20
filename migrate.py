from flask_migrate import Migrate
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from models import Advertisements, User

application = app
migrate = Migrate(application, db)
