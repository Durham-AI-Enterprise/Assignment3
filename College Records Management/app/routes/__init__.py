# routes/__init__.py

from flask import Blueprint

# create a blueprint for student routes
student_bp = Blueprint('student', __name__)

# import student routes
from app.routes.student import *