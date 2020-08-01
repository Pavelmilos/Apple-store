from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return '%s' % self.name

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True,
                            default=None)  # текстовое поле с обязательным параметром длина
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)  # значения создаются автоматически когда создается запись в Order
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True)  # значения автоматически изменяются при обновлении записи в Order

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return '%s, %s' % (self.price, self.name)

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)  # значения создаются автоматически когда создается запись в Order
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True)  # значения автоматически изменяются при обновлении записи в Order

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return '%s' % (self.id)

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
