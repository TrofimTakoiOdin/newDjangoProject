import random
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from myapp.models import User, Product, Order

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, help="Number of users to create")
        parser.add_argument("--orders", type=int, help="Number of orders to create")
        parser.add_argument("--products", type=int, help="Number of products to create")

    def handle(self, *args, **kwargs):
        num_users = kwargs.get('users')
        num_orders = kwargs.get('orders')
        num_products = kwargs.get('products')

        if not num_users:
            num_users = int(input("Enter the number of users to create: "))

        if not num_orders:
            num_orders = int(input("Enter the number of orders to create: "))

        if not num_products:
            num_products = int(input("Enter the number of products to create: "))

        self.create_fake_users(num_users)
        self.create_fake_products(num_products)
        self.create_fake_orders(num_orders)

    def create_fake_users(self, count):
        for _ in range(count):
            user = User(
                name=fake.name(),
                email=fake.email(),
                password=make_password(fake.password()),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            user.save()

    def create_fake_products(self, count):
        for _ in range(count):
            product = Product(
                name=fake.word(),
                price=fake.random_int(min=1, max=100) * 10,
                description=fake.text(),
                quantity=fake.random_int(min=1, max=100),
            )
            product.save()

    def create_fake_orders(self, count):
        users = User.objects.all()
        products = Product.objects.all()

        for _ in range(count):
            user = random.choice(users)
            order = Order(customer=user)
            total_price = 0

            for _ in range(random.randint(1, 7)):  # Number of products per order
                product = random.choice(products)
                total_price += float(product.price)
                order.total_price = total_price
                order.save()
                order.products.add(product)


#  Как пользоваться? Пример команды
#  python manage.py generate_fake_data --users 10 --orders 5 --products 20