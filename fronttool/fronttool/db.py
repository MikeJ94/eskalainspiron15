import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

