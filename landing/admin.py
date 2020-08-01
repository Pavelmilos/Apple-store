from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):  # позволяет настраивать поля в django-админке
    # list_display = ['name', 'email']
    list_display = [field.name for field in Subscriber._meta.fields]  # отображение всех полей из базы данных
    list_filter = ['email']  # создание фильтра по емейлу
    search_fields = ['name', 'email']  # поле поиска по имени и емейлу
    fields = ['email']  # отображать только поле емейл в /change/

    # exclude = ['email'] # исключить поле емейл в /change/

    class Meta:  # класс который содержит данные для класса SubscriberAdmin
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
