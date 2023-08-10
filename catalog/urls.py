from django.urls import path
from catalog.views import ContactsView, ItemsView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ItemsView.as_view(), name='base'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
