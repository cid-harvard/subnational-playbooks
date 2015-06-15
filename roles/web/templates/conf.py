DEBUG = {{atlas_environment != 'prod'}}
SECRET_KEY = "{{atlas_session_key}}"

SENTRY_DSN = ""

SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

CACHE_TYPE = "simple"
CACHE_KEY_PREFIX = "colombia::"

DEBUG_TB_ENABLED = DEBUG
PROFILE = False
PORT = 8001
