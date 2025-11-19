import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_django.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

super_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))
print('superusers:', super_emails)
