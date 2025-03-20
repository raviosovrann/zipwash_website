# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wwvjl0s-*gi4dnre@x#8ukpo=!lqqpu(t4!w1r21!dp**#)_85'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zipwash',
        'USER': 'zipwashadmin',
        'PASSWORD': 'ZIPWASHADMIN2025!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}