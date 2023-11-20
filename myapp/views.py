import logging
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import User, Order, Product

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='log/django.log', filemode='w')


def home(request):
    html_content = """
    <h2>Добро пожаловать на мой первый Django-сайт!</h2>
    <p>Здесь вы найдете интересные вещи о моем проекте.</p>
    """

    logger.info(f"Home page is visited. Time of visit: {datetime.now()}")
    context = {'html_content': html_content}

    return render(request, 'myapp/home.html', context)


def about(request):
    html_content = """
    <h2>Обо мне</h2>
    <p>Привет! Меня зовут Арсений, и это мой первый Django-сайт. Я учусь работать с Django и 
    хочу создавать крутые веб-приложения.</p>
    """

    logger.info(f"'About' page is visited. Time of visit: {datetime.now()}")
    context = {'html_content': html_content}
    return render(request, 'myapp/about.html', context)


def basket(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user).all()
    products = Product.objects.filter(order__in=orders).distinct()
    products.reverse()
    return render(request, 'myapp/user_all_orders.html', {'user': user, 'orders': orders, 'products': products})


def sorted_basket(request, user_id, days_ago):
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    products = Product.objects.filter(order__customer=user, order__date_ordered__range=(before, now)).distinct()

    return render(request, 'myapp/user_all_products.html', {'user': user, 'products': products, 'days': days_ago})
