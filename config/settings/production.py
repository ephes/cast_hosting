import logging  # noqa

from .base import *  # noqa
from .base import env  # noqa

ALLOWED_HOSTS = ["django-cast.com", "staging.wersdoerfer.de", "staging.python-podcast.de"]

ADMIN_URL = "hidden_admin/"

# There has to be a LOGGING setting otherwise we get a 500, dunno why
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}
