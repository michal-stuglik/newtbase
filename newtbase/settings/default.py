"""Default settings file. """

from newtbase.settings.base import *

DBNAME = ''  # database-name-on-the-host
USER = ''  # user-name
PASSWORD = ''  # set database-password
HOST = 'xxx.xxx.xxx.xxx'  # set host IP address

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'set-key-here'  # set-secret-key-here

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'newtbase.db'),
    }
}
