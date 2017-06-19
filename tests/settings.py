import os
import sys

from distutils.version import StrictVersion
import django
django_version_string = django.get_version()
if django_version_string.startswith('2.0.dev'):
    DJANGO_VERSION = StrictVersion('2.0')
else:
    DJANGO_VERSION = StrictVersion(django.get_version())
DJANGO_11 = StrictVersion('1.11')
DJANGO_18 = StrictVersion('1.8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

ADMINS = (
    ('test@example.com', 'Mr. Test'),
)

ALLOWED_HOSTS = [u'example.com']

SITE_ID = 1

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'tastypie.db'
TEST_DATABASE_NAME = ''

# for forwards compatibility
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'TEST_NAME': TEST_DATABASE_NAME,
    }
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tastypie',
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND = 'locmem://'
SECRET_KEY = 'verysecret'

# weaker password hashing shoulod allow for faster tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.CryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'py.warnings': {
            'level': 'ERROR',  # change to WARNING to show DeprecationWarnings, etc.
        },
    },
}

TASTYPIE_FULL_DEBUG = False

USE_TZ = True

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
