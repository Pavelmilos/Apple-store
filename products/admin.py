from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):  # позволяет добовлять картинки непосредственно в разделе товаров
    model = ProductImage  # на основе модели
    extra = 0  # минимальное количество вкладок для загрузки картинок


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]  # отображение всех полей из базы данных

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    list_display = [field.name for field in Product._meta.fields]  # отображение всех полей из базы данных
    inlines = [ProductImageInline]  # вкладываем в  ProductAdmin

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    list_display = [field.name for field in ProductImage._meta.fields]  # отображение всех полей из базы данных

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
