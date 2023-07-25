from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, id_item):
    product_shop = get_object_or_404(Product, id_item=id_item)
    context = {
        'object_list': product_shop,
        'title': 'Каталог'
    }
    return render(request, 'catalog/product.html', context)


def items(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Каталог'
    }
    return render(request, 'catalog/items.html', context)
