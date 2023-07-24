from django.shortcuts import render


def main_view(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def item(request):
    return render(request, 'catalog/item.html')
