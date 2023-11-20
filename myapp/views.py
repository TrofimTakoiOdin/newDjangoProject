import logging
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

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
