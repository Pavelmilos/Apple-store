from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    name = 'Bruce'  # переменная для отображения на html-странице (landing.html)
    current_day = '29.06.2020'
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():  # если метод запроса POST
        print(request.POST)  # вывод метода POST
        print(form.cleaned_data)  # вывод при помощи функции cleaned_data
        data = form.cleaned_data
        print(data['name'])  # вывод просто имени

        new_form = form.save()  # сохранение формы
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category_id=1)
    products_images_laptops = products_images.filter(product__category_id=2)
    return render(request, 'landing/home.html', locals())