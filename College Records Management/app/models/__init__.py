# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import models
from app.models.student import Student