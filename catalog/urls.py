from django.urls import path
from .views import (
    ContactsView,

    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    CategoriesListView,
    CategoryDetailView,

    BlogCreateView,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='inc_base'),

    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),

    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('categories/view/<int:pk>', CategoryDetailView.as_view(), name='view_category'),

    path('blog/', BlogListView.as_view(), name='entry_list'),
    path('blog/create/', BlogCreateView.as_view(), name='entry_form'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='entry_detail'),
    path('blog/<slug:slug>/update/', BlogUpdateView.as_view(), name='entry_update'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='entry_delete'),
]
