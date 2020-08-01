from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline): # позволяет добовлять товары непосредственно в разделе заказа
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    list_display = [field.name for field in Status._meta.fields]  # отображение всех полей из базы данных

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    list_display = [field.name for field in Order._meta.fields]  # отображение всех полей из базы данных
    inlines = [ProductInOrderInline]

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    list_display = [field.name for field in ProductInOrder._meta.fields]  # отображение всех полей из базы данных

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)



class ProductInBasketAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    list_display = [field.name for field in ProductInBasket._meta.fields]  # отображение всех полей из базы данных

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = ProductInBasket


admin.site.register(ProductInBasket, ProductInBasketAdmin)
