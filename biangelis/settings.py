import io
import os
import environ

from google.cloud import secretmanager
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool,False))
env_file = os.path.join(BASE_DIR,".env")

if os.path.isfile(env_file):
    env.read_env(env_file)
    # Gets gcp credentials for bucket
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        os.path.join(BASE_DIR, 'gcp.json'),
    )

elif os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    # Pull secrets from Secret Manager
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

    client = secretmanager.SecretManagerServiceClient()
    settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

    env.read_env(io.StringIO(payload))
else:
    raise Exception("No local .env or GOOGLE_CLOUD_PROJECT detected. No secrets found.")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['localhost','127.0.0.1','personal-448822.rj.r.appspot.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',

    'storages',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biangelis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'biangelis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

DATABASES["default"]["HOST"] = env('BD_ADDRESS')

'''
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('BD_NAME'),
        'HOST': env('BD_ADDRESS'),
        'USER': env('BD_USERNAME'),
        'PASSWORD': env('BD_PASSWORD')
    }
'''


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('pt', 'Portuguese'),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'base/locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/image/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


STORAGES = {
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
}

GS_PROJECT_ID = env("PROJECT_ID")
GS_BUCKET_NAME = env("BUCKET_NAME")
GS_FILE_OVERWRITE = False

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Emailing settings
