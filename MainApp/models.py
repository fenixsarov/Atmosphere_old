from django.db import models
from django.utils.timezone import now


# Very important tables
class Privilege(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Privilege'
        verbose_name_plural = 'Privileges'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)
    description = models.TextField(verbose_name='Описание')
    id_privileges = models.ForeignKey(Privilege)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Логин', max_length=20, unique=True)
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
    email = models.EmailField()
    phone = models.CharField(verbose_name='м.телефон', max_length=11)

    password = models.CharField(verbose_name='Пароль', max_length=30)
    id_category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Avatar(models.Model):
    id = models.AutoField(primary_key=True)
    avatar_img = models.ImageField()
    id_person = models.ForeignKey(Person)

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'


# Secondary tables
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name='Фото')
    name = models.CharField(verbose_name='Наменование/подпись', max_length=20)
    id_person = models.ForeignKey(Person)
    id_tags = models.ForeignKey(Tag)

    def __str__(self):
        return "Name: {}, tag: {}".format(self.name, self.id_tags)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


# Past-secondary tables
class News(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(verbose_name='Текст новости')
    date = models.DateField(verbose_name='Дата')
    id_newsmaker = models.ForeignKey(Person)
    id_tags = models.ForeignKey(Tag)

    def __str__(self):
        return "{}".format(self.date)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    email = models.EmailField(verbose_name='e-mail')
    phone = models.CharField(verbose_name='Телефон', max_length=12)
    date = models.DateField(verbose_name='Дата', default=now, blank=False)

    def __str__(self):
        return "Заказчик: {} {}".format(self.name, self.surname)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name='Описание локации')
    photo_header = models.ImageField(verbose_name='Фото для заголовка страницы')
    id_photo = models.ForeignKey(Photo)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name='О фотографе')
    id_person = models.ForeignKey(Person)
    id_photos = models.ForeignKey(Photo)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

# Create your models here.
