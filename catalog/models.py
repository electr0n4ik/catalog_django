import django
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from user.models import User

NULLABLE = {
    "null": True, "blank": True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, **NULLABLE, verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Версия продукта', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Наименование")
    description = models.CharField(max_length=200,
                                   **NULLABLE,
                                   verbose_name="Описание")
    photo = models.ImageField(upload_to='catalog/',
                              **NULLABLE,
                              verbose_name="Фото")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 **NULLABLE,
                                 verbose_name="Категория")
    price = models.IntegerField(**NULLABLE,
                                verbose_name="Цена")
    data_factory = models.DateField(**NULLABLE)
    data_update = models.DateField(**NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Версия продукта')
    version = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_сurrent_version = models.BooleanField(verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продукта'


class Blog(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Заголовок")
    slug = models.SlugField(unique=True,
                            verbose_name="Slug")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/',
                                verbose_name="Превью",
                                **NULLABLE)
    is_published = models.BooleanField(default=False,
                                       verbose_name="Признак публикации")
    view_count = models.PositiveIntegerField(default=0,
                                             verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"


class Contacts(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    number = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    office = models.CharField(max_length=150, verbose_name='Адрес офиса')

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
