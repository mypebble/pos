from base import *

DEBUG = True

MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE_CLASSES

INSTALLED_APPS += [
    'debug_toolbar',
]

OPENID_URL = 'localhost:8000/openid/xrds'
