from django.urls import path
from .views import (
    ContactsView,
    ItemsView,
    ProductDetailView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = 'catalog'

urlpatterns = [
    path('', ItemsView.as_view(), name='base'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

    path('blog/', BlogListView.as_view(), name='entry_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='entry_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='entry_create'),
    path('blog/<slug:slug>/update/', BlogUpdateView.as_view(), name='entry_update'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='entry_delete'),
]
