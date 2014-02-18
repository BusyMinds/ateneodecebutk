from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['ateneodecebu.tk','www.ateneodecebu.tk']

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'files/')

ADMINS = ('noelmartin@gmail.com',)

MANAGERS = ('noelmartin@gmail.com',)

DEFAULT_FROM_EMAIL = 'noelmartin@gmail.com'

SERVER_EMAIL = 'noelmartin@gmail.com'

USE_X_FORWARDED_HOST = True
