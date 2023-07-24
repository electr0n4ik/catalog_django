from django.urls import path
from catalog.views import main_view, contacts, item


app_name = 'catalog'

urlpatterns = [
    path('', main_view, name='main_view'),
    path('contacts/', contacts, name='contacts'),
    path('item/', item, name='contacts'),
]
