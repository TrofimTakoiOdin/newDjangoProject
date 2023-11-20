from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Get user by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            self.stdout.write(self.style.SUCCESS(f'Successfully retrieved user with ID {pk}: {user}'))
        else:
            self.stdout.write(self.style.ERROR(f'User with ID {pk} does not exist'))

#  Как пользоваться командой?
#  python manage.py get_user <user_id>
