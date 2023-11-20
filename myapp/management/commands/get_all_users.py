from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write("Users: ")
        for user in users:
            self.stdout.write(f'{user}\n')

#  Как пользоваться?
#  python manage.py get_all_users
