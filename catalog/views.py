from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from catalog.models import Product


# catalog/contacts.html - Шаблон для ContactsView.
# catalog/includes/inc_product.html - Шаблон для ProductDetailView.
# catalog/product_list.html - Шаблон для ProductListView.
# catalog/includes/inc_base.html - Шаблон для ItemsView.
class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/includes/inc_product.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/includes/inc_product.html'
    context_object_name = 'object_list'
    paginate_by = 10


class ItemsView(View):
    def get(self, request):
        context = {
            'object_list': Product.objects.all()[:3],
            'title': 'Каталог'
        }
        return render(request, 'catalog/includes/inc_base.html', context)
