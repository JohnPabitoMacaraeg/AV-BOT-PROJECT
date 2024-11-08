# main.py

import os
import django
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Initialize Django
django.setup()

application = get_wsgi_application()

# Import views to ensure they’re registered
from your_project.views import *
from your_project.models import *

if __name__ == '__main__':
    print("Django setup complete. You can now run your server with 'python manage.py runserver'.")
