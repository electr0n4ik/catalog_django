from itertools import product

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = Product.objects.all()
        products.delete()

        product_list = [
            {'name': 'Апельсин', 'description': 'Сладкий и оранжевый', "photo": "catalog/апельсин.png", "price": 100, "category_id": 1},
            {'name': 'Яблоко', 'description': 'Кислый и зеленый', "photo": "catalog/яблоко.jpeg", "price": 200, "category_id": 1},
            {'name': 'помидора', 'description': 'Красная', "photo": "catalog/помидора.png", "price": 300, "category_id": 2},
        ]

        category_list = [
            {'name': 'Фрукты', 'description': 'Обычно сладкие'},
            {'name': 'Овощи', 'description': 'Растут на грядках'},
        ]

        for element in product_list:
            Product.objects.create(**element)

        for element in category_list:
            Category.objects.create(**element)
