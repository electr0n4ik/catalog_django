from django.db import models

NULLABLE = {
    "null": True, "blank": True
}


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Наименование")
    description = models.CharField(max_length=200,
                                   **NULLABLE,
                                   verbose_name="Описание")

    def __str__(self):
        return self.name

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
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Blog(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Заголовок")
    slug = models.SlugField(unique=True,
                            verbose_name="Slug")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/',
                                verbose_name="Превью",
                                **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    is_published = models.BooleanField(default=False,
                                       verbose_name="Признак публикации")
    view_count = models.PositiveIntegerField(default=0,
                                             verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
