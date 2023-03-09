"""
WSGI config for django_github_actions_aws project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

"""
By default, Elastic Beanstalk looks for a file named application.py in our project. It uses that file to run
 our application, but we don't have that file in our project. Do we? We need to tell Elastic Beanstalk to 
 use the wsgi.py file in our project to run our application instead.

Create a folder named .ebextensions in your project directory. In that folder create a config file. 
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_github_actions_aws.settings')

application = get_wsgi_application()
