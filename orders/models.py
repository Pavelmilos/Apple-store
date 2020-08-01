from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)  # значения создаются автоматически когда создается запись в Order
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True)  # значения автоматически изменяются при обновлении записи в Order

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return 'Статус %s' % (self.name)

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)  # total price for all products in order
    customer_email = models.EmailField(blank=True, null=True, default=None)  # поле имеющие тип email
    customer_name = models.CharField(max_length=64, blank=True, null=True,
                                     default=None)  # текстовое поле с обязательным параметром длина
    customer_phone = models.CharField(max_length=28, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)  # значения создаются автоматически когда создается запись в Order
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True)  # значения автоматически изменяются при обновлении записи в Order

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return 'Заказ %s %s' % (self.id, self.status)

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)  # значения создаются автоматически когда создается запись в Order
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True)  # значения автоматически изменяются при обновлении записи в Order

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return '%s' % (self.product.name)

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):  # переопределение метода save
        price_per_item = self.product.price  # стоимость со стоимости товара
        self.price_per_item = price_per_item  # записываем переменную на саму запись
        self.total_price = int(self.nmb) * price_per_item  # считаем общую стоимость

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):  # использование post-save сигнала
    order = instance.order  # наш заказ (обращаемся к заказу через instance)
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)  # какие еще есть товары в заказе

    order_total_price = 0
    for item in all_products_in_order:  # прбегаем по всем товарам и считывем total_price
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)  # обновляет текущую запись при сохранении


post_save.connect(product_in_order_post_save, sender=ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)  # значения создаются автоматически когда создается запись в Order
    updated = models.DateTimeField(auto_now_add=False,
                                   auto_now=True)  # значения автоматически изменяются при обновлении записи в Order

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return '%s' % (self.product.name)

    class Meta:  # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):  # переопределение метода save
        price_per_item = self.product.price  # стоимость со стоимости товара
        self.price_per_item = price_per_item  # записываем переменную на саму запись
        self.total_price = int(self.nmb) * price_per_item  # считаем общую стоимость

        super(ProductInBasket, self).save(*args, **kwargs)