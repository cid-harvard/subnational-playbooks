DEBUG = {{atlas_environment != 'prod'}}
SECRET_KEY = "{{atlas_session_key|password_hash('sha512')}}"

SENTRY_DSN = ""

SQLALCHEMY_ECHO = DEBUG
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

CACHE_TYPE = "simple"
CACHE_KEY_PREFIX = "colombia::"

DEBUG_TB_ENABLED = DEBUG
PROFILE = False
PORT = 8001
