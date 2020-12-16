from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'products': Product.objects.all(),
        'buttons': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def menu_buttons(request):
    context = {
        'buttons': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)



