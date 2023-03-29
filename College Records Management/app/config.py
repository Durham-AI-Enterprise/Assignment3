import os

class Config:
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:root@localhost/college_records'
    SQLALCHEMY_TRACK_MODIFICATIONS = False