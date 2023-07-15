from django.shortcuts import render


def main_view(request):
    return render(request, 'main_view.html')


def contacts(request):
    return render(request, 'contacts.html')
