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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tools.strip_html_comments.StripHtmlCommentsMiddleware'
)

ROOT_URLCONF = 'newtbase.urls'

TEMPLATE_DIRS = [
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "templates_blast"),
]

# TEMPLATE_CONTEXT_PROCESSORS = (
#     # 'django.core.context_processors.auth',
#     # 'django.core.context_processors.debug',
#     # 'django.core.context_processors.i18n',
#     # 'django.core.context_processors.media',
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/static_root/' #dbsettings.STATIC_ROOT
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../static"),
)

# # testing suit
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


DOWNLOAD_DATA = {
    "LvLm_tgm": os.path.join(BASE_DIR, "../db/ref_trans/ref_trans_LvLm.fa.tar.gz"),
    "Lh_tgm": os.path.join(BASE_DIR, "../db/ref_trans/ref_trans_Lh.fa.tar.gz"),
    "immune_gene": os.path.join(BASE_DIR, "../db/immune_genes/775_immune_genes.fas.tar.gz"),
}

# database as list of choice: overriding blastplus defaults
BLAST_DB_NUCL_CHOICE = (
(os.path.join(BASE_DIR, "../db/blast_db/LvLm/reference_transcriptome.fa"), "Transcriptome gene models-Lv/Lm",),)
# )(os.path.join(BASE_DIR, 'db/blast_db/Lh/reference_helveticus.fa'), "Transcriptome gene models-Lh", ),)

# BLAST database override for newtbase!
from blastplus import settings as blast_settings
blast_settings.BLAST_DB_NUCL_CHOICE = BLAST_DB_NUCL_CHOICE

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
