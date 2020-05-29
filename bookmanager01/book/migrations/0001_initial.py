# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-05-29 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='名字')),
                ('pub_date', models.DateField(null=True)),
                ('read_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('is_del', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'admin',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述信息')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo', verbose_name='图书')),
            ],
            options={
                'verbose_name': '人物信息',
                'db_table': 'peopleinfo',
            },
        ),
    ]
