"""
Django settings for eventbrite project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m_6a@$+wqh_7d1skp^-#70+)7#glsdtie-3ypm9uw2d1^+dd03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'event',
    'user',
    'booking',
    'drf_spectacular',
    'eventManagment',
    'sslserver',
    # 'two_factor',
    # 'django_otp',
    # 'django_otp.plugins.otp_totp',
    # 'django_otp.plugins.otp_static',
    # 'django_otp_twilio',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    # 'two_factor.middleware.threadlocals.ThreadLocals',
    # 'two_factor.middleware.authy.AuthenticationStatusMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
]


ROOT_URLCONF = 'eventbrite.urls'

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

WSGI_APPLICATION = 'eventbrite.wsgi.application'


# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'Ismail-DB',
#             'ENFORCE_SCHEMA': False,
#             'CLIENT': {
#             'host':'mongodb+srv://ismail:512002@cluster0.swohyah.mongodb.net/?retryWrites=true&w=majority'
#             }
#         }
# }
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Z-DB',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_USER_MODEL='eventbrit.User'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'django.contrib.auth.backends.ModelBackend',  # default authentication backend
    ],

}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'Daniel.Aziz00@eng-st.cu.edu.eg'
# EMAIL_HOST_PASSWORD = 'Danie7889'
# EMAIL_PORT = 587
# EMAIL_USE_SSL = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'eventbrite2002@gmail.com'
EMAIL_HOST_PASSWORD = 'joghzolscsuucebv'
EMAIL_PORT = 587


# local email service backend
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
#EMAIL_USE_TLS = False
# run this cmd in another window python -m smtpd -n -c DebuggingServer localhost:1025
# and you will receive emails there


AUTH_USER_MODEL = 'user.user'

#ALLOWED_HOSTS = ['52.55.220.111','127.0.0.1']
# ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS = ['52.55.220.111']
ALLOWED_HOSTS = ['*']
# other settings ...

# AUTHY_API_KEY = 'your_authy_api_key'
# AUTHY_API_URL = 'https://api.authy.com'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
