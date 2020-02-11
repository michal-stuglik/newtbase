__author__ = 'michal'

from newtbase.settings.base import *
from newtbase.settings.prod import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxx-xxx-xxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS += ['0.0.0.0']

#
# PROJECT_APPS = [
#     'django_nose',
#     'coverage',
# ]
#
# INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS
#
#
# # # testing suit
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#
#
# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=newtbase, blastplus',
#     '--cover-inclusive',
#     '--verbosity=2',
# ]
#

