import os
from unipath import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

ALLOWED_HOSTS = ["*"]  # TODO Change later


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party apps
    'rest_framework',
    'webpack_loader',
    # local apps
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # # Joplin middleware
    # 'joplin.django_addons.middleware.RequestMiddleware',
)

ROOT_URLCONF = 'drf_react.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_react.wsgi.application'

####
# DATABASE
####

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

####
# INTERNATIONALIZATION
####

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

####
# STATIC FILES
####

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)

####
# WEBPACK
####

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-stats.json'),
    }
}


##################################################
# API Settings
##################################################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS':
        ('django_filters.rest_framework.DjangoFilterBackend',)
}

##################################################
# LRMS Settings
##################################################

# LOGIN_URL = "auth_login"
# LOGOUT_URL = "auth_logout"
# LOGIN_REDIRECT_URL = reverse_lazy("home")

TPOZ_ADMIN_USERNAME = 'admin'
TPOZ_ADMIN_PASSWORD = '11amcoke'

TPOZ_USERNAME = 'lrms_admin'
TPOZ_PASSWORD = 'letmein'

TPOZ_URL = "http://igarh7devrep.iga.local/dev"

DEFAULT_BACKEND = "joplin.django_addons.backend_resolvers.user_jupiter_backend"
default_backend = "joplin.django_addons.backend_resolvers.{0}".format(
    "user_jupiter_backend")
default_backend_type = 'joplin.backends.jupiter_backend.JupiterRequestsBackend'

JOPLIN_LOGIN_USERNAME_LOWERCASE = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SESS_KEY_AUTH_ID = "joplin_auth_id"
SESS_KEY_AUTH_TS = "joplin_auth_ts"


############################################################
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}