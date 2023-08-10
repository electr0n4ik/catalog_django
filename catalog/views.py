from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Blog


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


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/includes/inc_entry_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/includes/inc_entry_detail.html'
    context_object_name = 'object'

    def get_object(self, queryset=None):
        self.object = super(). get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogCreateView(CreateView):
    model = Blog

    template_name = 'blog/entry_form.html'


class BlogUpdateView(UpdateView):
    model = Blog

    template_name = 'blog/entry_form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'  # URL, на который перенаправлять после успешного удаления
    template_name = 'blog/entry_confirm_delete.html'
