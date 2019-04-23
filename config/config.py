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
LOG_PATH = ['/logs']


CHATBOT_API = ['http://127.0.0.1:8050/consume/api/']
API_TO_CONSUME = ['http://stooq.com/q/l/?s={0}&f=sd2t2ohlcv&h&e=csv']