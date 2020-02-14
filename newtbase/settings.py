"""
Django settings for newtbase project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
"""

import os

# BLAST database override for newtbase!
from blastplus import settings as blast_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = bool(int(os.getenv('DEBUG', False)))
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',') if os.getenv('ALLOWED_HOSTS') else ['127.0.0.1', 'localhost']


# Application definition
PREREQ_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'newtbase',
    'blastplus',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'tools.strip_html_comments.StripHtmlCommentsMiddleware'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

COMPRESS_ENABLED = True
ROOT_URLCONF = 'newtbase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "newtbase/templates"),
            os.path.join(BASE_DIR, "newtbase/templates_blast"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = 'newtbase.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'NAME': os.getenv('POSTGRES_NAME'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = '/app/static_root'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DOWNLOAD_DATA = {
    "LvLm_tgm": os.path.join(BASE_DIR, "./db/ref_trans/ref_trans_LvLm.fa.tar.gz"),
    "Lh_tgm": os.path.join(BASE_DIR, "./db/ref_trans/ref_trans_Lh.fa.tar.gz"),
    "immune_gene": os.path.join(BASE_DIR, "./db/immune_genes/775_immune_genes.fas.tar.gz"),
}

BLAST_DB_NUCL_LIST = [
    {
        "name": "Lv_Lm",
        "path": os.path.join(BASE_DIR, './db/blast_db/LvLm/reference_transcriptome.fa'),
        "desc": "Transcriptome gene models-Lv/Lm",
        "annotated": True, },
    {
        "name": "Lh",
        "path": os.path.join(BASE_DIR, './db/blast_db/Lh/reference_helveticus.fa'),
        "desc": "Transcriptome gene models-Lh",
        "annotated": False, },
]

BLAST_DB_NUCL_CHOICE = [(db["path"], db["desc"]) for db in BLAST_DB_NUCL_LIST]

blast_settings.BLAST_DB_NUCL_CHOICE = BLAST_DB_NUCL_CHOICE
blast_settings.BLAST_DB_NUCL_LIST = BLAST_DB_NUCL_LIST

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'CET'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
