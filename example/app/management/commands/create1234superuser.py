
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a superuser called "admin" with password "1234"'

    def handle(self, *args, **options):
        user = User.objects.filter(username='admin').first()
        if user:
            print('User "admin" already exists')
        else:
            User.objects.create_superuser('admin', 'someone@example.com', '1234')


