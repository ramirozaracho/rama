from .base import *
 
DEBUG = False
ALLOWED_HOSTS = ['ramirozaracho.pythonanywhere.com']
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ramirozaracho$default',
        'USER': 'ramirozaracho',
        'PASSWORD': 'belinda36116001',
        'HOST': 'ramirozaracho.mysql.pythonanywhere-services.com',
        'PORT': '',
	}
}
