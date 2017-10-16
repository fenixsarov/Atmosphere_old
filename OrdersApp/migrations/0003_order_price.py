# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersApp', '0002_auto_20170810_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
