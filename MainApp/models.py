from django.db import models

# Very important tables
class Privilege(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)
    description = models.TextField(verbose_name='Описание')
    id_privileges = models.ForeignKey(Privilege, verbose_name='Привилегии')

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Логин', max_length=20, unique=True)
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
    email = models.CharField(verbose_name='e-mail', max_length=30)
    phone = models.CharField(verbose_name='м.телефон', max_length=11)

    password = models.CharField(verbose_name='Пароль', max_length=30)
    id_category = models.ForeignKey(Category, verbose_name='Категория пользователя')


# Secondary tables
class Photo(models.Model):
    id = models.AutoField(primary_key=True)





# Create your models here.
