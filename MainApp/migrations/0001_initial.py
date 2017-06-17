# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avatar_img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Описание локации')),
                ('photo_header', models.ImageField(upload_to='', verbose_name='Фото для заголовка страницы')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(verbose_name='Текст новости')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('description', models.TextField(verbose_name='Описание заказа')),
                ('busy', models.BooleanField(default=False, verbose_name='Занятость')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Стоимость')),
                ('wish_list', models.TextField(verbose_name='Пожелания заказчика')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Логин')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('age', models.PositiveIntegerField(default=18, verbose_name='Возраст')),
                ('email', models.CharField(max_length=30, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=11, verbose_name='м.телефон')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('name', models.CharField(max_length=20, verbose_name='Наменование/подпись')),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='О фотографе')),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Person')),
                ('id_photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, verbose_name='Наименование')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='id_tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Tag'),
        ),
        migrations.AddField(
            model_name='order',
            name='id_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Request'),
        ),
        migrations.AddField(
            model_name='order',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Person'),
        ),
        migrations.AddField(
            model_name='news',
            name='id_newsmaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Person'),
        ),
        migrations.AddField(
            model_name='news',
            name='id_tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Tag'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Photo'),
        ),
        migrations.AddField(
            model_name='category',
            name='id_privileges',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Privilege'),
        ),
        migrations.AddField(
            model_name='avatar',
            name='id_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Person'),
        ),
    ]