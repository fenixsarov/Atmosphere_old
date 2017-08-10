from django.db import models
from MainApp.models import Person, Request


# Create your models here.
class Status(models.Model):
    name = models.CharField(verbose_name='Название статуса', max_length=16, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status {}".format(self.name)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    # date = models.DateTimeField(verbose_name='Дата и время')
    # description = models.TextField(verbose_name='Описание заказа')
    # busy = models.BooleanField(verbose_name='Занятость', default=False)
    # # busy = models.DateTimeField(verbose_name='Занятость')
    # price = models.DecimalField(verbose_name='Стоимость', max_digits=6, decimal_places=2, default=0.0)
    # wish_list = models.TextField(verbose_name='Пожелания заказчика')
    # id_user = models.ForeignKey(Person)
    # id_request = models.ForeignKey(Request)

    client_name = models.CharField(verbose_name='Имя', max_length=32, blank=True, null=True, default=None)
    client_email = models.EmailField(verbose_name='email', blank=True, null=True, default=None)
    client_phone = models.CharField(verbose_name='Телефон', max_length=24, blank=True, null=True, default=None)
    comments = models.TextField(verbose_name='Комментарии к заказу', blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=2000.00)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order id {}, status  {}".format(self.id, self.status.name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class RequestInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    request = models.ForeignKey(Request, blank=True, null=True, default=None)
    # photosession = models.ForeignKey(Photosession, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Requests {}".format(self.id)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'