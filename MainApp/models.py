from django.db import models


# Very important tables
class Privilege(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=15, unique=True)
    description = models.TextField(verbose_name='Описание')
    id_privileges = models.ForeignKey(Privilege)

    def __str__(self):
        return self.name


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


class Avatar(models.Model):
    id = models.AutoField(primary_key=True)
    avatar_img = models.ImageField()
    id_person = models.ForeignKey(Person)


# Secondary tables
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=15)

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name='Фото')
    name = models.CharField(verbose_name='Наменование/подпись', max_length=20)
    id_person = models.ForeignKey(Person)
    id_tags = models.ForeignKey(Tag)


# Past-secondary tables
class News(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(verbose_name='Текст новости')
    date = models.DateField(verbose_name='Дата')
    id_newsmaker = models.ForeignKey(Person)
    id_tags = models.ForeignKey(Tag)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    email = models.EmailField(verbose_name='e-mail')
    phone = models.CharField(verbose_name='Телефон', max_length=11)

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


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='Дата и время')
    description = models.TextField(verbose_name='Описание заказа')
    busy = models.BooleanField(verbose_name='Занятость', default=False)
    # busy = models.DateTimeField(verbose_name='Занятость')
    price = models.DecimalField(verbose_name='Стоимость', max_digits=6, decimal_places=2, default=0.0)
    wish_list = models.TextField(verbose_name='Пожелания заказчика')
    id_user = models.ForeignKey(Person)
    id_request = models.ForeignKey(Request)


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name='О фотографе')
    id_person = models.ForeignKey(Person)
    id_photos = models.ForeignKey(Photo)

    def __str__(self):
        return "{}".format(self.id)

# Create your models here.
