"""
Django settings for newtbase project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "../")

# Application definition
PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'newtbase',
    'blastplus',
    'django_nose',
    'coverage',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'tools.strip_html_comments.StripHtmlCommentsMiddleware'
)

ROOT_URLCONF = 'newtbase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates_blast"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/static_root/' #dbsettings.STATIC_ROOT
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../static"),
)


DOWNLOAD_DATA = {
    "LvLm_tgm": os.path.join(BASE_DIR, "../db/ref_trans/ref_trans_LvLm.fa.tar.gz"),
    "Lh_tgm": os.path.join(BASE_DIR, "../db/ref_trans/ref_trans_Lh.fa.tar.gz"),
    "immune_gene": os.path.join(BASE_DIR, "../db/immune_genes/775_immune_genes.fas.tar.gz"),
}

# database as list of choice: overriding blastplus defaults
BLAST_DB_NUCL_CHOICE = (
(os.path.join(BASE_DIR, "../db/blast_db/LvLm/reference_transcriptome.fa"), "Transcriptome gene models-Lv/Lm",),
(os.path.join(BASE_DIR, '../db/blast_db/Lh/reference_helveticus.fa'), "Transcriptome gene models-Lh", ),)

# BLAST database override for newtbase!
from blastplus import settings as blast_settings
blast_settings.BLAST_DB_NUCL_CHOICE = BLAST_DB_NUCL_CHOICE

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# # testing suit
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=newtbase, blastplus',
    '--cover-inclusive',
    '--verbosity=2',
]


CACHES = {
    "default": {
        "BACKEND": 'redis_cache.RedisCache',
        "LOCATION": "localhost:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "redis"
    }
}
