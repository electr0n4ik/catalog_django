from itertools import product

from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = Product.objects.all()
        products.delete()

        product_list = [
            {'name': 'Апельсин', 'description': 'Сладкий и оранжевый'},
            {'name': 'Яблоко', 'description': 'Кислый и зеленый'},
            {'name': 'Киви', 'description': 'Сладкий и зеленый'},
        ]

        for element in product_list:
            Product.objects.create(**element)
