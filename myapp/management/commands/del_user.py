from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Delete user by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()

        if user is not None:
            user.delete()
            self.stdout.write(f"User with ID {pk} deleted successfully.")
        else:
            self.stdout.write(f"User with ID {pk} not found.")

#  Как пользоваться?
#  python manage.py del_user <user_id>
