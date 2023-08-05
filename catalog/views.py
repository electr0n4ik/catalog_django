from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product_shop = get_object_or_404(Product, pk=pk)
    context = {
        'object': product_shop
    }
    return render(request, 'catalog/includes/inc_product.html', context)

class ProductListView(ListView):

    model = Product


def items(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Каталог'
    }
    return render(request, 'catalog/includes/inc_base.html', context)
