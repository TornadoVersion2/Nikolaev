from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'helloWorld/index.html')


def about(request):
    return render(request, 'helloWorld/about.html')


def contact(request):
    return render(request, 'helloWorld/contact.html')


def services(request):
    return render(request, 'helloWorld/services.html')


def products(request):
    products_list = Product.objects.all()
    context = {
        'products': products_list
    }
    return render(request, 'helloWorld/products.html', context)
