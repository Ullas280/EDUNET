import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal_django.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

email = 'admin@example.com'
password = 'AdminPass123'

# Required fields on the custom user model: fullname, phoneNumber, role
fullname = 'Admin'
phone = '0000000000'
role = 'recruiter'

if not User.objects.filter(email=email).exists():
    user = User(email=email, fullname=fullname, phoneNumber=phone, role=role, is_staff=True, is_superuser=True)
    user.set_password(password)
    user.save()
    print('Superuser created:', email)
else:
    print('Superuser already exists:', email)
