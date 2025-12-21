from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect
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
    errors = {}
    form_data = {
        'name': '',
        'description': '',
        'category': '',
        'price': '',
        'status': 'available',
    }

    if request.method == 'POST':
        form_data['name'] = request.POST.get('name', '').strip()
        form_data['description'] = request.POST.get('description', '').strip()
        form_data['category'] = request.POST.get('category', '').strip()
        form_data['price'] = request.POST.get('price', '').strip()
        form_data['status'] = request.POST.get('status', 'available')

        if not form_data['name']:
            errors['name'] = 'Укажите название продукта'
        if not form_data['description']:
            errors['description'] = 'Добавьте описание продукта'
        if not form_data['category']:
            errors['category'] = 'Укажите категорию продукта'

        price_value = None
        if not form_data['price']:
            errors['price'] = 'Укажите цену продукта'
        else:
            normalized_price = form_data['price'].replace(' ', '').replace(',', '.')
            try:
                price_value = Decimal(normalized_price)
                if price_value <= 0:
                    errors['price'] = 'Цена должна быть больше нуля'
            except (InvalidOperation, ValueError):
                errors['price'] = 'Неверный формат цены'

        status_values = {choice[0] for choice in Product.STATUS_CHOICES}
        if form_data['status'] not in status_values:
            errors['status'] = 'Неверный статус продукта'

        if not errors:
            Product.objects.create(
                name=form_data['name'],
                description=form_data['description'],
                category=form_data['category'],
                price=price_value,
                status=form_data['status'],
            )
            return redirect('products')

    products_list = Product.objects.all()
    context = {
        'products': products_list,
        'form_errors': errors,
        'form_data': form_data,
        'status_choices': Product.STATUS_CHOICES,
    }
    return render(request, 'helloWorld/products.html', context)


def add_product(request):
    return render(request, 'helloWorld/add_product.html')
