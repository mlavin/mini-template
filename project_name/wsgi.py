"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os

import dotenv
from django.core.wsgi import get_wsgi_application


env = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(env):
    dotenv.read_dotenv(env)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

application = get_wsgi_application()
