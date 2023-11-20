from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Update user name by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")
        parser.add_argument("name", type=str, help="New user name")

    def handle(self, *args, **kwargs):
        user_id = kwargs['pk']
        new_name = kwargs['name']

        try:
            user = User.objects.get(pk=user_id)
            user.name = new_name
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated user name for ID {user_id}'))
            self.stdout.write(f'Updated user details:\n{user}')
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'User with ID {user_id} does not exist.'))

#  Как пользоваться?
#  python manage.py update_username <user_id> <new_name>
