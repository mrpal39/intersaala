### dev.py
from .defaults import *
### other development-specific stuff



DEBUG = True
ALLOWED_HOSTS = []




STATIC_URL = 'static/'
import os
STATICFILES_DIRS = os.path.join("static"),
STATIC_ROOT=os.path.join('staticfile')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

MEDIA_ROOT = 'media/'



