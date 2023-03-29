# utils/database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# configure the database URI
db_uri ='mysql+pymysql://root:root@localhost/college_records'

# configure the database
def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)