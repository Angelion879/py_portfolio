"""
WSGI config for biangelis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from whitenoise import WhiteNoise
from .settings import env
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biangelis.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=env("STATIC_HOST"))
application.add_files("static/", prefix="static/")
