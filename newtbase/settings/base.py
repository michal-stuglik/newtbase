"""
Django settings for newtbase project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "../")

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
    # 'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
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
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates_blast"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                # 'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newtbase',
        'USER': 'newtbase',
        'PASSWORD': 'newtbase',
        'HOST': 'db'
    }
}

# memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = '/app/static_root'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../static"),
    # '/app/static',
)

DOWNLOAD_DATA = {
    "LvLm_tgm": os.path.join(BASE_DIR, "../db/ref_trans/ref_trans_LvLm.fa.tar.gz"),
    "Lh_tgm": os.path.join(BASE_DIR, "../db/ref_trans/ref_trans_Lh.fa.tar.gz"),
    "immune_gene": os.path.join(BASE_DIR, "../db/immune_genes/775_immune_genes.fas.tar.gz"),
}

# database as list of choice: overriding blastplus defaults
# BLAST_DB_NUCL_CHOICE = (
#     (os.path.join(BASE_DIR, "../db/blast_db/LvLm/reference_transcriptome.fa"), "Transcriptome gene models-Lv/Lm",),
#     (os.path.join(BASE_DIR, '../db/blast_db/Lh/reference_helveticus.fa'), "Transcriptome gene models-Lh",),)

BLAST_DB_NUCL_LIST = [
    {
        "name": "Lv_Lm",
        "path": os.path.join(BASE_DIR, '../db/blast_db/LvLm/reference_transcriptome.fa'),
        "desc": "Transcriptome gene models-Lv/Lm",
        "annotated": True, },
    {
        "name": "Lh",
        "path": os.path.join(BASE_DIR, '../db/blast_db/Lh/reference_helveticus.fa'),
        "desc": "Transcriptome gene models-Lh",
        "annotated": False, },
]

BLAST_DB_NUCL_CHOICE = [(db["path"], db["desc"]) for db in BLAST_DB_NUCL_LIST]

# BLAST database override for newtbase!
from blastplus import settings as blast_settings

blast_settings.BLAST_DB_NUCL_CHOICE = BLAST_DB_NUCL_CHOICE
blast_settings.BLAST_DB_NUCL_LIST = BLAST_DB_NUCL_LIST

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'CET'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
