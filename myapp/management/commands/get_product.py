from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Get product by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Product ID")

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()

        if product is not None:
            self.stdout.write(self.style.SUCCESS(f"Product found: {product}"))
        else:
            self.stdout.write(self.style.WARNING(f"Product with ID {pk} not found."))

#  Как пользоваться?
#  python manage.py get_product <product_id>
