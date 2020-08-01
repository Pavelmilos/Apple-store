from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()  # поле имеющие тип email
    name = models.CharField(max_length=128)  # текстовое поле с обязательным параметром длина

    def __str__(self):  # позволяет в модели выводить название по умолчанию
        return 'Пользователь %s %s' % (self.name, self.email)

    class Meta: # позволяет изменить название в единстевнном и во множественном числе
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'
