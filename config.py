import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
DEBUG_TOOLBAR = False

HOST = '127.0.0.1'
PORT = 8000

SECRET_KEY = 'some_secret_key'

THREADS_PER_PAGE = 8

CSRF_ENABLED = True

CSRF_SESSION_KEY = "some_session_key"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

# Local overrides
# both SECRET_KEY and CSRF_SESSION_KEY should probably be overwridden on
# production. We should also decide if UUID is really the correct
# option for this. TODO
try:
    from config_local import *
except ImportError as e:
    pass
