from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="product Name")
        parser.add_argument("price", type=float, help="product price")
        parser.add_argument("description", type=str, help="product description")
        parser.add_argument("quantity", type=int, help="product quantity")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        price = kwargs['price']
        description = kwargs['description']
        quantity = kwargs['quantity']

        product = Product(name=name, price=price, description=description, quantity=quantity)
        product.save()

        self.stdout.write(f'Product created: {product}')

#  Как пользоваться командой?
#  python manage.py set_product product_name product_price product_description product_quantity