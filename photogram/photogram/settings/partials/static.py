import os

from .base import PROJECT_ROOT_DIR
from .base import BASE_DIR

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "media")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
