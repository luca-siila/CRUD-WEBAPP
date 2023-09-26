import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://LucaNT:443251@209.145.55.0:3306/siil_dba_prod'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = '127.0.0.1:5000'
