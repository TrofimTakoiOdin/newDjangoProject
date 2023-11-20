from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create a User: "

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="User Name")
        parser.add_argument("email", type=str, help="User email")
        parser.add_argument("password", type=str, help="User password")
        parser.add_argument("phone", type=str, help="phone number")
        parser.add_argument("address", type=str, help="User address")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        password = kwargs['password']
        phone = kwargs['phone']
        address = kwargs['address']
        user = User(name=name, email=email, password=password, phone=phone, address=address)
        user.save()

        self.stdout.write(f'User created: {user}')

# Как пользоваться командой?
# python manage.py set_user <name> <email> <password> <phone> <address>
