# app/__init__.py
from flask import Flask
from app.config import Config
from app.routes.student import student_bp
from app.utils.database import db, configure_database
# import routes and models
from app import routes, models
from app.utils.response_utils import error_response, success_response

# create Flask app instance
app = Flask(__name__)

# configure the database
configure_database(app)

app.register_blueprint(student_bp)

@app.route('/')
def index():
    return success_response("Welcome to College Records Management System")

# handle 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return error_response('Not found')

# handle 500 errors
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return error_response('Internal server error')