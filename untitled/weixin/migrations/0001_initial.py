# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methods', models.CharField(choices=[('B', '血检'), ('S', '唾检')], max_length=2)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=11)),
                ('qq', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('psd', models.CharField(max_length=32)),
                ('qq', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
