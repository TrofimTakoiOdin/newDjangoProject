import logging
from datetime import datetime, timedelta
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from myapp.forms import ProductFormWidget
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


def product_update_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            # Handle form data
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            number = form.cleaned_data.get('number')

            # Handle image upload
            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            # Update product details
            product.name = name
            product.price = price
            product.description = description
            product.quantity = number
            product.image = image.name
            product.save()
            messages.success(request, 'Product updated successfully!')

    else:
        # Populate form with existing data
        form = ProductFormWidget(initial={
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'number': product.quantity,
        })

    return render(request, 'product_update.html', {'form': form, 'product': product})
