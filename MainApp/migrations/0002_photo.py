# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
