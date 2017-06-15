from django.db import models


class Person(models.Model):
    username = models.CharField(verbose_name='Логин', max_length=20, unique=True)
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
    email = models.CharField(verbose_name='e-mail', max_length=30)
    phone = models.CharField(verbose_name='м.телефон', max_length=11)

    password = models.CharField(verbose_name='Пароль', max_length=30)
    id_category = models.PositiveSmallIntegerField()


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)
    description = models.TextField(verbose_name='Описание')
    privileges = models.CharField(verbose_name='Привилегии', max_length=20)


class Privilege(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)


# Create your models here.
