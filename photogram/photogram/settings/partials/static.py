import os

from django.contrib.staticfiles.storage import CachedFilesMixin, ManifestFilesMixin

from .base import PROJECT_ROOT_DIR
from .base import BASE_DIR

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# collectsatic이 이루어지고 나서 저장될 경로
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")

# media(예를 들면 사진 같은거) 유저가 올리면 저장될 경로
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "media")

BASE_DIR2 = os.path.dirname(BASE_DIR)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR2, "static"),
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'application': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/photogram.css',
        },
    },
    'JAVASCRIPT': {
    }
}

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
