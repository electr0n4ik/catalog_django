from django.urls import path
from catalog.views import contacts, items, product


app_name = 'catalog'

urlpatterns = [
    path('', items, name='base'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:id>/', product, name='product')
]
