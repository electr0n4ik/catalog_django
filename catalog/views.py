from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from dotenv import load_dotenv
from pytils.translit import slugify

from catalog.forms import ProductForm, ProductVersionForm
from catalog.models import Product, Contacts, Blog, ProductVersion

from django.core.cache import cache
from catalog.models import Product, Contacts, Blog, ProductVersion, Category
from config.settings import CACHE_ENABLED

load_dotenv()


class ContactsView(View):

    def get(self, request):
        contact = Contacts.objects.get(pk=1)
        return render(request, 'catalog/contacts.html', context={'object': contact})

    def post(self, request):
        contact = Contacts.objects.get(pk=1)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        return render(request, 'catalog/contacts.html', context={'object': contact})


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    template_name = 'catalog/includes/inc_base.html'

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated:
            return
        context = super().get_context_data(**kwargs)
        for product in context['object_list']:
            active_version = ProductVersion.objects.filter(product=product, is_сurrent_version=True).first()
            product.active_version = active_version
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_publish=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('catalog:product_view', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.has_perm('catalog.set_published'):
            context['form'].fields.pop('is_publish')
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.user = self.request.user
            new_product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:inc_base')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.has_perm('catalog.set_published'):
            context['form'].fields.pop('is_publish')
        moderators = Group.objects.get(name="moderators").user_set.all()
        if self.request.user in moderators:
            context['form'].fields.pop('title')
            context['form'].fields.pop('img')
            context['form'].fields.pop('price')
        elif self.request.user == self.object.user:
            # Формирование формсета
            VersionFormSet = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)
            if self.request.method == 'POST':
                context['formset'] = VersionFormSet(self.request.POST, instance=self.object)
            else:
                context['formset'] = VersionFormSet(instance=self.object)
        else:
            return
        return context

    def form_valid(self, form):
        formset = self.get_context_data().get('formset')
        if formset.is_valid():
            count_is_сurrent_version = 0
            for f in formset:
                if formset.can_delete and formset._should_delete_form(f):
                    continue
                if f.cleaned_data.get('is_сurrent_version'):
                    count_is_сurrent_version += 1
                    if count_is_сurrent_version > 1:
                        form.add_error(None, "Не может быть больше одной текущей версии")
                        return self.form_invalid(form=form)
            formset.save()
            if form.cleaned_data.get('is_publish'):
                if not self.request.user.has_perm('set_published'):
                    form.add_error('is_publish', 'Публиковать могут только модераторы')
                    return self.form_invalid(form)
            return super().form_valid(form=form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:inc_base')

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated:
            return
        return super().get_context_data(**kwargs)


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
    template_name = 'blog/entry_detail.html'
    context_object_name = 'object'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content')
    context_object_name = 'object'
    template_name = 'blog/entry_form.html'

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:entry_detail', kwargs={'slug': self.object.slug})


class BlogUpdateView(UpdateView):
    model = Blog

    template_name = 'blog/entry_form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'  # URL, на который перенаправлять после успешного удаления
    template_name = 'blog/entry_confirm_delete.html'


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        if CACHE_ENABLED:
            key = f'categories_list'
            categories_list = cache.get(key)
            if categories_list is None:
                categories_list = Category.objects.all()
                cache.set(key, categories_list)
        else:
            categories_list = Category.objects.all()
        return categories_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
