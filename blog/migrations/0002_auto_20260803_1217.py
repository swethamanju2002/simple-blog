import os
from django.db import migrations
from django.contrib.auth import get_user_model

def create_admin_user(apps, schema_editor):
    User = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "sweths")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "swethaharish2222@gmail.com")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    if password and not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'), # Make sure this matches your previous migration
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
