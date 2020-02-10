

PROJECT_APPS = [
    'django_nose',
    'coverage',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS


# # testing suit
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=newtbase, blastplus',
    '--cover-inclusive',
    '--verbosity=2',
]

