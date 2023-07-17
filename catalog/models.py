from django.db import models

NULLABLE = {
    "null": True, "blank": True
}


class Category(models.Model):
    name = models.CharField(max_length=100,
                            **NULLABLE,
                            verbose_name="Наименование")
    description = models.CharField(max_length=200,
                                   verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100,
                            **NULLABLE,
                            verbose_name="Наименование")
    description = models.CharField(max_length=200,
                                   verbose_name="Описание")
    photo = models.ImageField(upload_to='catalog/',
                              verbose_name="Фото")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 **NULLABLE,
                                 verbose_name="Категория")
    price = models.IntegerField(max_length=5,
                                **NULLABLE,
                                verbose_name="Цена")
    data_factory = models.DateField()
    data_update = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
