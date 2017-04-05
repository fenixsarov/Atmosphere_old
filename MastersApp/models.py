from django.db import models


class Masters(models.Model):
    username = models.CharField(verbose_name=u'Логин', max_length=32, unique=True)
    name = models.CharField(verbose_name=u'Имя', max_length=16)
    surname = models.CharField(verbose_name=u'Фамилия', max_length=16)
    description = models.TextField(verbose_name=u'О себе')
# Create your models here.
