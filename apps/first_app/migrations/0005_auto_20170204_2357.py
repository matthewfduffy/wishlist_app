# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20170204_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
