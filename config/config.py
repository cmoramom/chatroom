import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "thisissecret"
WTF_CSRF_ENABLED = True
SESSION_COOKIE_SECURE = False
REMEMBER_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_HTTPONLY = True
LOG_PATH=['/logs']


