from django.db import models


class Product(models.Model):
    pass

    def __str__(self):
        return "self.name"


class Category(models.Model):
    pass

    def __str__(self):
        return "self.name"
