from django.core.management.base import BaseCommand
from myapp.models import Order

class Command(BaseCommand):
    help = "Get order by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Order ID")

    def handle(self, *args, **kwargs):
        order_id = kwargs['pk']
        order = Order.objects.filter(pk=order_id).first()

        if order is not None:
            self.stdout.write(self.style.SUCCESS(f'Successfully retrieved order with ID {order_id}'))
            self.stdout.write(f'Order details:\n{order}')
        else:
            self.stdout.write(self.style.WARNING(f'Order with ID {order_id} does not exist.'))

#  Как пользоваться?
#  python manage.py get_order <order_id>
